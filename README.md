# Use Case-1
## Rainfall Prediction Model (API for monthly data forecasting)
This project aims to build a simple API for rainfall prediction model using time series analysis techniques. It utilizes the Holt-Winters Exponential Smoothing and SARIMA models to forecast future precipitation based on historical rainfall data. The model is exposed through a Flask web application, allowing users to make predictions and evaluate model performance. 

### Table of Contents

- Installation
- Usage
- Endpoints
- Model Evaluation
- Technologies Used
- License

### Installation
### <ins>Install required packages:</ins>
Make sure you have Python installed, then install the necessary libraries using pip:
 
    pip install -r requirements.txt
    Create a `requirements.txt` file with the following contents:

    numpy
    pandas
    statsmodels
    scikit-learn
    Flask
    joblib
    pmdarima
  
### <ins>Download the dataset:</ins>
Ensure that you have the ("Rainfall_data.csv") file in the root directory of the project.

### <ins>Usage</ins>

1.  **Run the Flask application:**

    ```bash
    python app.py
    ```

    The API will start running on `http://127.0.0.1:5000/`.

2.  **Make predictions using the `/predict` endpoint:**

    Send a POST request with the following JSON payload:

    ```json
    {
      "start_date": "YYYY-MM-DD",
      "steps": 12
    }
    ```

    -   `start_date`: The starting date for the prediction (YYYY-MM-DD format).
    -   `steps`: The number of months to predict (optional, defaults to 12).



3.  **Evaluate the model using the `/evaluate` endpoint:**

    Send a GET request to:
    ```bash
    [http://127.0.0.1:5000/evaluate](https://www.google.com/search?q=http://127.0.0.1:5000/evaluate)
    ```

    This will return the Mean Absolute Error (MAE), Mean Squared Error (MSE), and Root Mean Squared Error (RMSE) of the selected model.

### <ins>API Endpoints</ins>

-   **`/predict` (POST):**
    -   Predicts rainfall for a given number of months starting from a specified date.
    -   Requires JSON payload with `start_date` and `steps` (optional).
    -   Returns a JSON array of predictions with dates.
-   **`/evaluate` (GET):**
    -   Evaluates the performance of the selected model on the test dataset.
    -   Returns MAE, MSE, and RMSE as JSON.

### <ins>Data Preparation</ins>

The `Rainfall_data.csv` dataset should have the following columns:

-   `Year`: The year of the rainfall measurement.
-   `Month`: The month of the rainfall measurement.
-   `Day`: The day of the rainfall measurement.
-   `Precipitation`: The amount of rainfall.

The script preprocesses the data by:

-   Combining the Year, Month, and Day columns into a datetime index.
-   Splitting the data into training (80%) and testing (20%) sets.

### <ins>Model Selection</ins>

The script trains both Holt-Winters and SARIMA models and evaluates their performance using MAE, MSE, and RMSE. The model with the lowest RMSE is selected as the best model and saved to `best_model.pkl` using `joblib`.

### <ins>Technologies Used</ins>
- Python
- Flask (for web framework)
- NumPy (for numerical operations)
- Pandas (for data manipulation)
- Statsmodels (for statistical modeling)
- Scikit-learn (for performance metrics)
- Joblib (for model serialization)
- Pmdarima (for automatic ARIMA modeling)

### <ins>License</ins>

This project is licensed under the [MIT License](LICENSE).
