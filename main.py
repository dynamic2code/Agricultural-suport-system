import numpy as np
import pandas as pd
import requests
import secret
from io import StringIO
import urllib.request
import sys
import joblib
import requests
import sys

import csv
import codecs
from flask import Flask, request, jsonify

app = Flask(__name__)
def hello():
    return "where I start"

def extracting_data():
    #weater data from timeline wether Api
    #get worning data from https://www.appsforagri.com/ it will help in comparing the needed condition and the current one
    location = input("enter your location: ")
    # location = data
    startDate = '2022-6-5'
    endDate = '2023-1-1'

    response = requests.request("GET",
                                f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=metric&include=days&key={secret.API_KEY}&contentType=csv")
    if response.status_code != 200:
        print('Unexpected Status code: ', response.status_code)
        sys.exit()

        # Parse the results as CSV
    CSVText = csv.reader(response.text.splitlines(), delimiter=',', quotechar='"')

    temp = CSVText[1:, 2].astype(float)

    # Calculate the mean of the column
    mean_temp = np.mean(temp)

    humidity = CSVText[1:, 9].astype(float)

    # Calculate the mean of the column
    mean_humidity = np.mean(humidity)

    n = 23
    p = 23
    k = 23
    ph = 7
    rainfall = 220

    x_new = [n, p, k, mean_temp, mean_humidity, ph, rainfall]

def crop_recomendation(x_new):
    # load the saved model
    model = joblib.load('crop_prediction.h5')
    # make predictions on new data
    # x_new =   #new data as a list of feature vectors
    y_pred = model.predict(x_new)  # predicted target values

    return y_pred


def process_data():
    data = request.get_json()

    # Process the data
    # result = []
    # for item in data:
    #     result.append({
    #         'name': item['name'],
    #         'age': item['age'] * 2,
    #     })

    # Return the result
    if data:
        return 'its done'
    # return jsonify(result)
@app.route("/")
def execute():
    hello()
    process_data()
    return "Done"

if __name__ == "__main__":
  app.run()


    #crop recomendation dataset from kaggel https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset?resource=download
    # N - ratio of Nitrogen content in soil
    # P - ratio of Phosphorous content in soil
    # K - ratio of Potassium content in soil
    # temperature - temperature in degree Celsius
    # humidity - relative humidity in %
    # ph - ph value of the soil
    # rainfall - rainfall in mm


