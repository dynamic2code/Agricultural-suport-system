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

    for row in CSVText:
        # process the row here
        print(row)

        # try:
    #     ResultBytes = urllib.request.urlopen(
    #         f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{startDate}/{endDate}?unitGroup=metric&include=days&key={secret.API_KEY}&contentType=csv")
    #
    #     # Parse the results as CSV
    #     CSVText = csv.reader(codecs.iterdecode(ResultBytes, 'utf-8'))
    #     print(CSVText)
    #
    # except urllib.error.HTTPError as e:
    #     ErrorInfo = e.read().decode()
    #     print('Error code: ', e.code, ErrorInfo)
    #     sys.exit()
    # except urllib.error.URLError as e:
    #     ErrorInfo = e.read().decode()
    #     print('Error code: ', e.code, ErrorInfo)
    #     sys.exit()
    #
    # # weather soil temp, soil moisture, evaporation, wind speed, wind direction, direct normal radiation
    # try:
    #     ResultBytes = urllib.request.urlopen(
    #         f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Nairobi/last30days?unitGroup=metric&elements=windspeed50%2Cwinddir50%2Cdniradiation%2Csoiltemp04%2Csoilmoisture04%2Cet0&include=days&key={secret.API_KEY}&contentType=csv")
    #
    #     # Parse the results as CSV
    #     CSVText = csv.reader(codecs.iterdecode(ResultBytes, 'utf-8'))
    #
    # except urllib.error.HTTPError as e:
    #     ErrorInfo = e.read().decode()
    #     print('Error code: ', e.code, ErrorInfo)
    #     sys.exit()
    # except urllib.error.URLError as e:
    #     ErrorInfo = e.read().decode()
    #     print('Error code: ', e.code, ErrorInfo)
    #     sys.exit()
    #
    #     X_new = [[...], [...], ...]
    # return x_new
    #crop recomendation dataset from kaggel https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset?resource=download
    # N - ratio of Nitrogen content in soil
    # P - ratio of Phosphorous content in soil
    # K - ratio of Potassium content in soil
    # temperature - temperature in degree Celsius
    # humidity - relative humidity in %
    # ph - ph value of the soil
    # rainfall - rainfall in mm
def crop_recomendation(X_new):
    # load the saved model
    model = joblib.load('crop_prediction.h5')
    # make predictions on new data
    #X_new =   new data as a list of feature vectors
    y_pred = model.predict(X_new)  # predicted target values

    return y_pred

extracting_data()

