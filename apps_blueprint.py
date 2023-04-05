import csv
import os.path
import secrets
import sqlite3
import sys
from datetime import date, timedelta

import joblib
import numpy as np
import pandas as pd
import requests
from flask import Blueprint, render_template, request, redirect
from werkzeug.security import generate_password_hash, check_password_hash

import secret

current_dir = os.path.dirname(os.path.abspath(__file__))
app_blueprint = Blueprint('app_blueprint', __name__)

location = ''

@app_blueprint.route("/")
def login():
    return render_template("login.html")
@app_blueprint.route("/", methods = ["POST"])
def get_details():
    global location
    conn = sqlite3.connect('farmers.db')
    cur = conn.cursor()

    # Create the table if it doesn't exist
    cur.execute('''CREATE TABLE IF NOT EXISTS farmer (
                        id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        location TEXT NOT NULL,
                        land_size FLOAT NOT NULL
                )''')

    # Insert data into the table
    name = request.form['name']
    location = request.form['location']
    land_size = request.form['land_size']
    password = generate_password_hash(request.form['password'])
    cur.execute("INSERT INTO farmer (name, location, land_size, password) VALUES (?, ?, ?, ?)", (name, location, land_size, password))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    return redirect('/content')


@app_blueprint.route("/content")
def content():
    report = dict()
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

    hum.pop(0)
    humNew = [float(x) for x in hum]
    mean_hum = [np.mean(humNew)]
    # # Calculate the mean of the column

    n = [23]
    p = [23]
    k = [23]
    ph = [7]
    rainfall = [220]

    zipped = list(zip(n, p, mean_temp, mean_hum, ph, rainfall))
    x_new = pd.DataFrame(zipped, columns=['N', 'P', 'temperature', 'humidity', 'ph', 'rainfall'])

    #end of first prediction
    response = requests.request("GET",
                                f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=metric&include=days&key={secret.API_KEY}&contentType=csv")
    if response.status_code != 200:
        print('Unexpected Status code: ', response.status_code)
        sys.exit()

        # Parse the results as CSV
    CSVText = csv.reader(response.text.splitlines(), delimiter=',', quotechar='|')

    tem2 = []
    hum2 = []
    for row in CSVText:
        # print(row)
        for column in row:
            if column == row[4]:
                tem2.append(column)

        for column in row:
            if column == row[9]:
                hum2.append(column)

    tem2.pop(0)
    tempNew = [float(x) for x in tem2]
    mean_temp2 = [np.mean(tempNew)]
    # print(mean_temp)

    hum2.pop(0)
    humNew = [float(x) for x in hum2]
    mean_hum2 = [np.mean(humNew)]
    # print(mean_hum)
    n2 = [23]
    p2 = [23]
    k = [23]
    ph2 = [7]
    rainfall2 = [220]

    zipped = list(zip(n2, p2, mean_temp2, mean_hum2, ph2, rainfall2))
    x_new2 = pd.DataFrame(zipped, columns=['N', 'P', 'temperature', 'humidity', 'ph', 'rainfall'])
    # print(x_new)

    model = joblib.load('crop_prediction.h5')
    # make predictions on new data
    # x_new =   #new data as a list of feature vectors
    y_pred = model.predict(x_new)  # predicted target values
    y_pred2 = model.predict(x_new2)

    crops = ['rice', 'maize', 'chickpea', 'kidneybeans', 'pigeonpeas',
       'mothbeans', 'mungbean', 'blackgram', 'lentil', 'pomegranate',
       'banana', 'mango', 'grapes', 'watermelon', 'muskmelon', 'apple',
       'orange', 'papaya', 'coconut', 'cotton', 'jute', 'coffee']

    crop1 = y_pred[0]
    crop2 = y_pred2[0]

    report["crop prediction one "] = crops[crop1]
    report["crop prediction two "] = crops[crop2]

    #economic prediction

    # state = []
    # district = []
    # market = []
    # commodity = [crop1]
    # min_price = []
    # max_price = []
    #
    # zipped = list(zip(commodity, min_price, max_price))
    # x_new3 = pd.DataFrame(zipped, columns=['commodity', 'min_price', 'max_price'])
    #
    # model = joblib.load('price_prediction (1).h5')
    # y_pred = model.predict(x_new3)  # predicted target values
    #
    # price = y_pred[0]
    #
    # report["price"] = price

    #weather data for prediction
    response = requests.request("GET",
                                f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/today?unitGroup=metric&include=days&key={secret.API_KEY}&contentType=csv")
    if response.status_code != 200:
        print('Unexpected Status code: ', response.status_code)
        sys.exit()

        # Parse the results as CSV
    CSVText = csv.reader(response.text.splitlines(), delimiter=',', quotechar='|')

    tem_today = []
    hum_today = []
    for row in CSVText:
        # print(row)
        for column in row:
            if column == row[4]:
                tem_today.append(column)

        for column in row:
            if column == row[9]:
                hum_today.append(column)

    tem_today.pop(0)
    tempNew = [float(x) for x in tem_today]
    report["mean_temp_today"] = [np.mean(tempNew)]
    # print(mean_temp_today)

    hum_today.pop(0)
    humNew = [float(x) for x in hum_today]
    report["mean_hum_today"] = [np.mean(humNew)]
    # print(mean_hum_today)

    response = requests.request("GET",
                                f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/last30days?unitGroup=metric&include=days&key={secret.API_KEY}&contentType=csv")
    if response.status_code != 200:
        print('Unexpected Status code: ', response.status_code)
        sys.exit()

        # Parse the results as CSV
    CSVText = csv.reader(response.text.splitlines(), delimiter=',', quotechar='|')

    tem_last30 = []
    hum_last30 = []
    for row in CSVText:
        # print(row)
        for column in row:
            if column == row[4]:
                tem_last30.append(column)

        for column in row:
            if column == row[9]:
                hum_last30.append(column)

    tem_last30.pop(0)
    tempNew = [float(x) for x in tem_last30]
    report["mean_temp_past30"] = [np.mean(tempNew)]
    # print(mean_temp_past30)

    hum_last30.pop(0)
    humNew = [float(x) for x in hum_last30]
    report["mean_hum_past30"] = [np.mean(humNew)]
    # print(mean_hum_past30)


    response = requests.request("GET",
                                f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/last7days?unitGroup=metric&include=days&key={secret.API_KEY}&contentType=csv")
    if response.status_code != 200:
        print('Unexpected Status code: ', response.status_code)
        sys.exit()

        # Parse the results as CSV
    CSVText = csv.reader(response.text.splitlines(), delimiter=',', quotechar='|')

    tem_last7 = []
    hum_last7 = []
    for row in CSVText:
        # print(row)
        for column in row:
            if column == row[4]:
                tem_last7.append(column)

        for column in row:
            if column == row[9]:
                hum_last7.append(column)

    tem_last7.pop(0)
    tempNew = [float(x) for x in tem_last7]
    report["mean_temp_past7"] = [np.mean(tempNew)]
    # print(mean_temp_past7)

    hum_last7.pop(0)
    humNew = [float(x) for x in hum_last7]
    report["mean_hum_past7"] = [np.mean(humNew)]
    # print(mean_hum_past7)


    response = requests.request("GET",
                                f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/next7days?unitGroup=metric&include=days&key={secret.API_KEY}&contentType=csv")
    if response.status_code != 200:
        print('Unexpected Status code: ', response.status_code)
        sys.exit()

        # Parse the results as CSV
    CSVText = csv.reader(response.text.splitlines(), delimiter=',', quotechar='|')

    tem_next7 = []
    hum_next7 = []
    for row in CSVText:
        # print(row)
        for column in row:
            if column == row[4]:
                tem_next7.append(column)

        for column in row:
            if column == row[9]:
                hum_next7.append(column)

    tem_next7.pop(0)
    tempNew = [float(x) for x in tem_next7]
    report["mean_temp_future7"] = [np.mean(tempNew)]
    # print(mean_temp_future7)

    hum_next7.pop(0)
    humNew = [float(x) for x in hum_next7]
    report["mean_hum_future7"] = [np.mean(humNew)]
    # print(mean_hum_future7)

    response = requests.request("GET",
                                f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/next24hours?unitGroup=metric&include=days&key={secret.API_KEY}&contentType=csv")
    if response.status_code != 200:
        print('Unexpected Status code: ', response.status_code)
        sys.exit()

        # Parse the results as CSV
    CSVText = csv.reader(response.text.splitlines(), delimiter=',', quotechar='|')

    tem_next24 = []
    hum_next24 = []
    for row in CSVText:
        # print(row)
        for column in row:
            if column == row[4]:
                tem_next24.append(column)

        for column in row:
            if column == row[9]:
                hum_next24.append(column)

    tem_next24.pop(0)
    tempNew = [float(x) for x in tem_next24]
    report["mean_temp_tomorrow"] = [np.mean(tempNew)]
    # print(mean_temp_tomorrow)

    hum_next24.pop(0)
    humNew = [float(x) for x in hum_next24]
    report["mean_hum_tomorrow"] = [np.mean(humNew)]
    # print(mean_hum_tomorrow)

    # farming_activity = dict()
    # planting
    if report["mean_temp_today"][0] >= 15:
        # planting = dict()
        report["planting_message"] = f'The temperature today is{report["mean_temp_today"]} its a good day to plant'
        report["planting_date"] = date.today()

        # farming_activity.update(planting)
        # report

    elif (report["mean_temp_today"][0] < 15):
        if (report["mean_temp_tomorrow"][0] >= 15):

            report["planting_message"] = f'The temperature tomorrow will be{report["mean_temp_tomorrow"]} its a good day to plant'
            report["planting_date"] = date.today() + timedelta(1)



    # watering
    if report["mean_hum_today"][0] < 50:

        report["watering_message"] = f"It is advisable for you to water the plants today"

    else:

        report["message"] = f"The weather conditions are great today it's not necessary to water the plants"




    # print(report)
    html_output = ''
    for key, value in report.items():
        html_output += '<div><p><b>{}</b>: {}</p></div>'.format(key, value)
    # return html_output
    # divs = []
    # for key, value in report.items():
    #     divs.append(f"<div><strong>{key}:</strong> {value}</div>")
    #
    # html_data = ' '.join(divs)

    return render_template("content.html", html_data= html_output)

