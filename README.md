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

### <ins>Installation</ins>
### Install required packages:
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
  
### Download the dataset:
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


# Use Case-2
## BDD Test Case and Playwright Script Generator

This project generates Behavior-Driven Development (BDD) test cases and basic Playwright test scripts from user stories and acceptance criteria. It utilizes natural language processing (NLP) techniques to process text and a pre-trained language model to generate test cases automatically.

### Table of Contents

- Installation
- Usage
- Features
- Code explanation
- Technologies Used
- License
  
### <ins>Installation</ins>

  **Create a virtual environment:**

    python -m venv venv
    venv\Scripts\activate  # On Windows
    source venv/bin/activate # On macOS and Linux

  **Install the required dependencies:**

    pip install -r requirements.txt
   
    Create a `requirements.txt` file with the following contents:

    pandas
    nltk
    transformers
    torch

  **Download NLTK's `punkt` tokenizer:**

    The script automatically downloads the `punkt` tokenizer if it's not already present.

    python
    import nltk
    nltk.download('punkt')

 ### <ins>Usage</ins>

1.  **Run the Python script:**

    python generate_tests.py

    (Assuming the python file is called generate_tests.py)

2.  **View the output:**

    The script will print a Pandas DataFrame containing the user stories, acceptance criteria, generated BDD test cases, and Playwright scripts. It will also create a directory named `playwright_tests` containing the generated Playwright test scripts.

### <ins>Code Explanation</ins>
1.  **Data Preparation:**
    -   User stories and acceptance criteria are stored in lists.
    -   A Pandas DataFrame is created to organize the data.
    -   Acceptance criteria are tokenized using NLTK's `word_tokenize`.

2.  **BDD Test Case Generation:**
    -   The `distilgpt2` model is used to generate BDD test cases from user stories and acceptance criteria.
    -   A prompt is constructed to guide the model's output.
    -   The generated text is parsed to extract the BDD test case.

3.  **Playwright Script Generation:**
    -   Basic Playwright scripts are generated from the BDD test cases.
    -   The script creates a skeleton test with the test name derived from the BDD test case.
    -   The generated scripts provide a starting point for writing more detailed tests.

4.  **Output:**
The output includes:
    -   User stories and acceptance criteria.
    -   Generated BDD test cases.
    -   Corresponding Playwright test scripts saved in a dedicated directory.

### <ins>Technologies Used</ins>
 - Python
 - Pandas (for data manipulation)
 - NLTK (for natural language processing)
 - Transformers (for text generation using pre-trained models)
 - Playwright (for automated testing)
    
### <ins>Features</ins>
-  **User Story Input:** Define user stories that describe desired functionalities.
-  **Acceptance Criteria:** Specify acceptance criteria that outline conditions for success.
-  **BDD Test Case Generation:** Automatically generate BDD test cases based on user stories 
     and acceptance criteria using a pre-trained language model.
-  **Playwright Script Generation:** Create basic Playwright test scripts from generated BDD test cases for automated testing.

### <ins>License</ins>
This project is licensed under the MIT License.
