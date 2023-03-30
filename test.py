import csv

import pandas as pd
import sklearn
import sys

import joblib
import numpy as np
import requests

import secret

import csv
import codecs


def extracting_data():
    # weater data from timeline wether Api
    # get worning data from https://www.appsforagri.com/ it will help in comparing the needed condition and the current one
    global location
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
    CSVText = csv.reader(response.text.splitlines(), delimiter=',', quotechar='|')
    # CSVText = csv.reader(codecs.iterdecode(response, 'utf-8'))
    tem = []
    hum = []
    for row in CSVText:
        # print(row)
        for column in row:
            if column == row[3]:
                tem.append(column)

        for column in row:
            if column == row[9]:
                hum.append(column)

    tem.pop(0)
    tempNew = [float(x) for x in tem]
    mean_temp = [np.mean(tempNew)]
    # print(mean_temp)

    hum.pop(0)
    humNew = [float(x) for x in hum]
    mean_hum = [np.mean(humNew)]
    # print(mean_hum)


    #
    # humidity = CSVText[1:, 9].astype(float)
    #
    # # Calculate the mean of the column
    # mean_humidity = np.mean(humidity)
    #
    n = [23]
    p = [23]
    k = [23]
    ph = [7]
    rainfall = [220]

    zipped = list(zip(n, p, mean_temp, mean_hum, ph, rainfall))
    x_new = pd.DataFrame(zipped, columns=['N', 'P', 'temperature', 'humidity', 'ph', 'rainfall'])
    # print(x_new)

    return x_new

def extracting_data2(location):
    # weater data from timeline wether Api
    # get worning data from https://www.appsforagri.com/ it will help in comparing the needed condition and the current one
    # location = data
    startDate = '2022-6-5'
    endDate = '2023-1-1'

    response = requests.request("GET",
                                f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=metric&include=days&key={secret.API_KEY}&contentType=csv")
    if response.status_code != 200:
        print('Unexpected Status code: ', response.status_code)
        sys.exit()

        # Parse the results as CSV
    CSVText = csv.reader(response.text.splitlines(), delimiter=',', quotechar='|')
    # CSVText = csv.reader(codecs.iterdecode(response, 'utf-8'))
    tem = []
    hum = []
    for row in CSVText:
        # print(row)
        for column in row:
            if column == row[4]:
                tem.append(column)

        for column in row:
            if column == row[9]:
                hum.append(column)

    tem.pop(0)
    tempNew = [float(x) for x in tem]
    mean_temp = [np.mean(tempNew)]
    # print(mean_temp)

    hum.pop(0)
    humNew = [float(x) for x in hum]
    mean_hum = [np.mean(humNew)]
    # print(mean_hum)


    #
    # humidity = CSVText[1:, 9].astype(float)
    #
    # # Calculate the mean of the column
    # mean_humidity = np.mean(humidity)
    #
    n = [23]
    p = [23]
    k = [23]
    ph = [7]
    rainfall = [220]

    zipped = list(zip(n, p, mean_temp, mean_hum, ph, rainfall))
    x_new2 = pd.DataFrame(zipped, columns=['N', 'P', 'temperature', 'humidity', 'ph', 'rainfall'])
    # print(x_new)

    return x_new2



def crop_recomendation():
    # load the saved model
    model = joblib.load('crop_prediction.h5')
    # make predictions on new data
    # x_new =   #new data as a list of feature vectors
    y_pred = model.predict(extracting_data())  # predicted target values
    y_pred2 = model.predict(extracting_data2(location))

    crops = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
       'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
       'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
       'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']

    crop1 = y_pred[0]
    crop2 = y_pred2[0]
    print(crops[crop1])
    print(crops[crop2])



# extracting_data()
crop_recomendation()