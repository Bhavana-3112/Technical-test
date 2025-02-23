import numpy as np
import pandas as pd
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_squared_error, mean_absolute_error
from flask import Flask, request, jsonify
import joblib
from pmdarima import auto_arima

# Load the dataset (assuming it's in the same directory)
df = pd.read_csv("C:/Users/reddy/OneDrive/Documents/Bhavana/Use Case-1/Rainfall_data.csv")

# Preprocess the data
df['DATE'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
df.set_index('DATE', inplace=True)
df.drop(columns=['Year', 'Month', 'Day'], inplace=True)

# Split data into train and test sets (80% train, 20% test)
train_size = int(len(df) * 0.8)
train_data = df.iloc[:train_size]
test_data = df.iloc[train_size:]
# Function to evaluate model performance
def evaluate_model(model, test_data):
    predictions = model.predict(steps=len(test_data))
    mae = mean_absolute_error(test_data['Precipitation'], predictions)
    mse = mean_squared_error(test_data['Precipitation'], predictions)
    rmse = np.sqrt(mse)
    return mae, mse, rmse

# Train Holt-Winters model
hw_model = ExponentialSmoothing(train_data['Precipitation'], trend='add', seasonal='add', seasonal_periods=12).fit()
hw_mae, hw_mse, hw_rmse = evaluate_model(hw_model, test_data)

print("Holt-Winters Model:")
print(f"MAE: {hw_mae}, MSE: {hw_mse}, RMSE: {hw_rmse}")

# Train SARIMA model
sarima_model = auto_arima(train_data['Precipitation'], seasonal=True, m=12)
sarima_mae, sarima_mse, sarima_rmse = evaluate_model(sarima_model,test_data)

print("\nSARIMA Model:")
print(f"MAE: {sarima_mae}, MSE: {sarima_mse}, RMSE: {sarima_rmse}")

# Select the best model (based on RMSE)
best_model = hw_model if hw_rmse < sarima_rmse else sarima_model
joblib.dump(best_model, 'best_model.pkl')

# Flask app
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        model = joblib.load('best_model.pkl')
        start_date = pd.to_datetime(request.json.get('start_date'))
        steps = int(request.json.get('steps', 12))

        predictions = model.forecast(steps=steps)
        dates = pd.date_range(start=start_date, periods=steps, freq='MS') #monthly start frequency
        result = [{'date': date.isoformat(), 'prediction': pred} for date, pred in zip(dates, predictions.tolist())]

        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/evaluate', methods=['GET'])
def evaluate():
    try:
        model = joblib.load('best_model.pkl')
        mae, mse, rmse = evaluate_model(model, test_data)
        return jsonify({'mae': mae, 'mse': mse, 'rmse': rmse})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
