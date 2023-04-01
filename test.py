import csv
import urllib
from datetime import date, timedelta

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

    crop_to_plant = dict()

    print(crops[crop1])
    print(crops[crop2])

def price_data():
    state = []
    district = []
    market = []
    commodity = []
    min_price = []
    max_price = []

    zipped = list(zip(state, district, market, commodity, min_price, max_price))
    x_new = pd.DataFrame(zipped, columns=['state', 'district', 'market', 'commodity', 'min_price', 'max_price'])
    return x_new


def economic():
    model = joblib.load('price_prediction (1).h5')
    y_pred = model.predict(price_data())  # predicted target values

    price = y_pred[0]
    print(price)

#get crops activity and best conditions to accomplish them in


def get_future_weather():
    #get future weather to predict activities
    global report;
    report = dict()
    # location = input("location:")
    # try:
    #     ResultBytes = urllib.request.urlopen(
    #         f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=metric&include=events&key={secret.API_KEY}&contentType=csv")
    #
    #     # Parse the results as CSV
    #     # CSVText = csv.reader(codecs.iterdecode(ResultBytes, 'utf-8'))
    #     CSVText = csv.reader(ResultBytes.text.splitlines(), delimiter=',', quotechar='|')
    #
    #     tem = []
    #     hum = []
    #     for row in CSVText:
    #         # print(row)
    #         for column in row:
    #             if column == row[4]:
    #                 tem.append(column)
    #
    #         for column in row:
    #             if column == row[9]:
    #                 hum.append(column)
    #
    #     tem.pop(0)
    #     tempNew = [float(x) for x in tem]
    #     mean_temp = [np.mean(tempNew)]
    #     print(mean_temp)
    #
    #     hum.pop(0)
    #     humNew = [float(x) for x in hum]
    #     mean_hum = [np.mean(humNew)]
    #     print(mean_hum)
    #
    # except urllib.error.HTTPError as e:
    #     ErrorInfo = e.read().decode()
    #     print('Error code: ', e.code, ErrorInfo)
    #     sys.exit()
    # except  urllib.error.URLError as e:
    #     ErrorInfo = e.read().decode()
    #     print('Error code: ', e.code, ErrorInfo)
    #     sys.exit()
    response = requests.request("GET",
                                f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/today?unitGroup=metric&include=days&key={secret.API_KEY}&contentType=csv")
    if response.status_code != 200:
        print('Unexpected Status code: ', response.status_code)
        sys.exit()

        # Parse the results as CSV
    CSVText = csv.reader(response.text.splitlines(), delimiter=',', quotechar='|')

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
    report["mean_temp_today"] = [np.mean(tempNew)]
    # print(mean_temp_today)

    hum.pop(0)
    humNew = [float(x) for x in hum]
    report["mean_hum_today"] = [np.mean(humNew)]
    # print(mean_hum_today)

    response = requests.request("GET",
                                f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/last30days?unitGroup=metric&include=days&key={secret.API_KEY}&contentType=csv")
    if response.status_code != 200:
        print('Unexpected Status code: ', response.status_code)
        sys.exit()

        # Parse the results as CSV
    CSVText = csv.reader(response.text.splitlines(), delimiter=',', quotechar='|')

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
    report["mean_temp_past30"] = [np.mean(tempNew)]
    # print(mean_temp_past30)

    hum.pop(0)
    humNew = [float(x) for x in hum]
    report["mean_hum_past30"] = [np.mean(humNew)]
    # print(mean_hum_past30)


    response = requests.request("GET",
                                f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/last7days?unitGroup=metric&include=days&key={secret.API_KEY}&contentType=csv")
    if response.status_code != 200:
        print('Unexpected Status code: ', response.status_code)
        sys.exit()

        # Parse the results as CSV
    CSVText = csv.reader(response.text.splitlines(), delimiter=',', quotechar='|')

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
    report["mean_temp_past7"] = [np.mean(tempNew)]
    # print(mean_temp_past7)

    hum.pop(0)
    humNew = [float(x) for x in hum]
    report["mean_hum_past7"] = [np.mean(humNew)]
    # print(mean_hum_past7)


    response = requests.request("GET",
                                f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/last7days?unitGroup=metric&include=days&key={secret.API_KEY}&contentType=csv")
    if response.status_code != 200:
        print('Unexpected Status code: ', response.status_code)
        sys.exit()

        # Parse the results as CSV
    CSVText = csv.reader(response.text.splitlines(), delimiter=',', quotechar='|')

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
    report["mean_temp_future7"] = [np.mean(tempNew)]
    # print(mean_temp_future7)

    hum.pop(0)
    humNew = [float(x) for x in hum]
    report["mean_hum_future7"] = [np.mean(humNew)]
    # print(mean_hum_future7)

    response = requests.request("GET",
                                f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/next24hours?unitGroup=metric&include=days&key={secret.API_KEY}&contentType=csv")
    if response.status_code != 200:
        print('Unexpected Status code: ', response.status_code)
        sys.exit()

        # Parse the results as CSV
    CSVText = csv.reader(response.text.splitlines(), delimiter=',', quotechar='|')

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
    report["mean_temp_tomorrow"] = [np.mean(tempNew)]
    # print(mean_temp_tomorrow)

    hum.pop(0)
    humNew = [float(x) for x in hum]
    report["mean_hum_tomorrow"] = [np.mean(humNew)]
    # print(mean_hum_tomorrow)

    return report

def farming_activity(report):
    farming_activity = dict()
    #planting
    if (report["mean_temp_today"][0] >= 15):
        planting = dict()
        planting["planting_message"] = f'The temperature today is{ report["mean_temp_today"]} its a good day to plant'
        planting["planting_date"] = date.today()

        farming_activity.update(planting)

    elif(report["mean_temp_today"][0] < 15):
        if(report["mean_temp_tomorrow"][0] >= 15):
            planting = dict()
            planting["planting_message"] = f'The temperature tomorrow will be{report["mean_temp_tomorrow"]} its a good day to plant'
            planting["planting_date"] = date.today() + timedelta(1)

            farming_activity.update(planting)

    #watering
    if(report["mean_hum_today"][0] < 50):
        watering = dict()
        watering["watering_message"] = f"It is advisable for you to water the plants today"

        farming_activity.update(watering)

    else:
        watering = dict()
        watering["message"] = f"The weather conditions are great today it's not necessary to water the plants"

        farming_activity.update(planting)

    #pruning


    return farming_activity


extracting_data()
crop_recomendation()
# economic()
print(get_future_weather())
print(farming_activity(report))
