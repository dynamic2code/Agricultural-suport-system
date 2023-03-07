import pandas as pd
import requests
import secret
from io import StringIO
import urllib.request
import sys

import csv
import codecs

def extracting_data():
    #weater data from timeline wether Api
    #get worning data from https://www.appsforagri.com/ it will help in comparing the needed condition and the current one
    location = input("enter your location: ")
    startDate = '2020-6-5'
    endDate = '2023-1-1'
    # response_future_weather = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=metric&include=days&key={secret.API_KEY}&contentType=csv'
    # response_past_weather = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{startDate}/{endDate}?unitGroup=metric&include=days&key={secret.API_KEY}&contentType=csv'
    # response_soil_temp = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Denver,CO?unitGroup=metric&key={secret.API_KEY}&contentType=csv&include=days&elements=datetime,temp,soiltemp01,soiltemp04,soiltemp10,soiltemp20')
    # response_soil_moisture = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Denver,CO?unitGroup=metric&key={secret.API_KEY}&contentType=csv&include=days&elements=datetime,soilmoisture01,soilmoisture04,soilmoisture10,soilmoisture20,soilmoisturevol01,soilmoisturevol04,soilmoisturevol10,soilmoisturevol20 ')
    # response_evaporation = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Denver,CO?unitGroup=metric&key={secret.API_KEY}&contentType=csv&include=days&elements=datetime,et0')
    try:
        ResultBytes = urllib.request.urlopen(
            f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}/{startDate}/{endDate}?unitGroup=metric&include=days&key={secret.API_KEY}&contentType=csv")

        # Parse the results as CSV
        CSVText = csv.reader(codecs.iterdecode(ResultBytes, 'utf-8'))
        print(CSVText)

    except urllib.error.HTTPError as e:
        ErrorInfo = e.read().decode()
        print('Error code: ', e.code, ErrorInfo)
        sys.exit()
    except urllib.error.URLError as e:
        ErrorInfo = e.read().decode()
        print('Error code: ', e.code, ErrorInfo)
        sys.exit()

    # weather soil temp, soil moisture, evaporation, wind speed, wind direction, direct normal radiation
    try:
        ResultBytes = urllib.request.urlopen(
            "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Nairobi/last30days?unitGroup=metric&elements=windspeed50%2Cwinddir50%2Cdniradiation%2Csoiltemp04%2Csoilmoisture04%2Cet0&include=days&key=YOUR_API_KEY&contentType=csv")

        # Parse the results as CSV
        CSVText = csv.reader(codecs.iterdecode(ResultBytes, 'utf-8'))

    except urllib.error.HTTPError as e:
        ErrorInfo = e.read().decode()
        print('Error code: ', e.code, ErrorInfo)
        sys.exit()
    except urllib.error.URLError as e:
        ErrorInfo = e.read().decode()
        print('Error code: ', e.code, ErrorInfo)
        sys.exit()




    #crop recomendation dataset from kaggel https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset?resource=download
    # N - ratio of Nitrogen content in soil
    # P - ratio of Phosphorous content in soil
    # K - ratio of Potassium content in soil
    # temperature - temperature in degree Celsius
    # humidity - relative humidity in %
    # ph - ph value of the soil
    # rainfall - rainfall in mm


extracting_data()
