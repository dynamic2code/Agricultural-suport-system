import pandas as pd
import csv
import requests
import secret


def extracting_data():
    #weater data from timeline wether Api
    #get worning data from https://www.appsforagri.com/ it will help in comparing the needed condition and the current one
    location = input("enter your location: ")
    StartDate = ''
    EndDate = ''
    response_future_weather = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=metric&include=days&key={secret.API_KEY}&contentType=csv')
    response_past_weather = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=metric&include=days&key={secret.API_KEY}&contentType=csv')
    response_soil_temp = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Denver,CO?unitGroup=metric&key={secret.API_KEY}&contentType=csv&include=days&elements=datetime,temp,soiltemp01,soiltemp04,soiltemp10,soiltemp20')
    response_soil_moisture = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Denver,CO?unitGroup=metric&key={secret.API_KEY}&contentType=csv&include=days&elements=datetime,soilmoisture01,soilmoisture04,soilmoisture10,soilmoisture20,soilmoisturevol01,soilmoisturevol04,soilmoisturevol10,soilmoisturevol20 ')
    response_evaporation = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Denver,CO?unitGroup=metric&key={secret.API_KEY}&contentType=csv&include=days&elements=datetime,et0')
    print(response_future_weather.status_code)

    #crop recomendation dataset from kaggel https://www.kaggle.com/datasets/atharvaingle/crop-recommendation-dataset?resource=download
    # N - ratio of Nitrogen content in soil
    # P - ratio of Phosphorous content in soil
    # K - ratio of Potassium content in soil
    # temperature - temperature in degree Celsius
    # humidity - relative humidity in %
    # ph - ph value of the soil
    # rainfall - rainfall in mm


extracting_data()
