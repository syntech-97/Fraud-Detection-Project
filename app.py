from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle
from jinja2 import TemplateNotFound

# load the model from disk
filename = 'model.pkl'
try:
    with open(filename, 'rb') as model_file:
        clf = pickle.load(model_file)
except Exception as e:
    print(f"Error loading the model: {e}")
    clf = None

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.method == 'POST':
            me = request.form['message']
            # Validate and process input
            try:
                message = [float(x) for x in me.split(',')]
            except ValueError:
                return render_template('error.html', message='Error: Please enter valid numerical values separated by commas.')

            vect = np.array(message).reshape(1, -1)

            # Check if the model is loaded
            if clf:
                my_prediction = clf.predict(vect)
                return render_template('result.html', prediction=my_prediction)
            else:
                return render_template('error.html', message='Error: Model not loaded')

    except (Exception, TemplateNotFound) as e:
        return render_template('error.html', message=f'Error: {e}')


if __name__ == '__main__':
    app.run(debug=True)
