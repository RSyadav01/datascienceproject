import pandas as pd
import numpy as np
import os
from src.Datascience.pipeline.prediction_pipeline import PredictionPipeline
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])  ## route to display the home page
def homepage():
    return render_template("index.html")

@app.route('/train', methods=['GET'])  # route to train the pipeline
def training():
    os.system("python main.py")
    return "Training Successful"

@app.route('/predict', methods=['POST', 'GET'])  # route from web UI
def index():
    if request.method == 'POST':
        try:
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])

            # Convert input data to NumPy array
            data = np.array([
                fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, 
                free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol
            ]).reshape(1, 11)

            # Load prediction pipeline and predict
            obj = PredictionPipeline()
            predict_result = obj.predict(data)

            return render_template("results.html", prediction=str(predict_result))

        except Exception as e:
            return "Something is wrong"

    else:
        render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)