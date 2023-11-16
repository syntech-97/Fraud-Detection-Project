# Credit Card Fraud Detection Web App

Welcome to the Credit Card Fraud Detection Web App! This application utilizes a machine learning model to predict whether a given set of features represents a fraudulent credit card transaction. Users can input the 30 feature values through a user-friendly web form, and the application provides instant prediction results.

## Directory Structure

```
|-- static
|   |-- styles.css
|-- templates
|   |-- error.html
|   |-- home.html
|   |-- result.html
|-- app.py
|-- train_model.ipynb
|-- model.pkl
|-- valid_values.csv
|-- fraud_values.csv
```

## Setup and Usage

### Install Dependencies:

```bash
pip install Flask pandas numpy scikit-learn
```

### Run the Flask Application:

```bash
python app.py
```

### Open the Web Application:

Open your web browser and navigate to [http://localhost:5000/](http://localhost:5000/).

### Make Predictions:

Enter the 30 feature values in the provided text area and click the "Predict" button.

## Files

- **app.py:** Main Flask application file handling web requests, loading the machine learning model, and rendering templates.
- **train_model.ipynb:** Jupyter Notebook containing the code used to train the machine learning model.
- **model.pkl:** Pickle file containing the trained machine learning model.
- **valid_values.csv:** CSV file with valid feature values for testing the application.
- **fraud_values.csv:** CSV file with fraudulent feature values for testing the application.

## Web Templates

### home.html

The home page template where users can input the 30 feature values.

### result.html

The result page template displaying the prediction result based on the machine learning model.

### error.html

The error page template displayed in case of any errors during input processing or model loading.

## Styling

The application uses a simple CSS file located in the static directory to style the web pages.

## Notes

- Appropriate error messages are displayed to the user in case of issues with model loading or input validation.

Feel free to explore the application at [https://syntech97.pythonanywhere.com/](https://syntech97.pythonanywhere.com/) and experience the Credit Card Fraud Detection in action!
