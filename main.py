import pandas as pd
import csv
import requests
import secret


def extracting_data():
    location = input("enter your location: ")
    StartDate = ''
    EndDate = ''
    response = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{location}?unitGroup=metric&include=days&key={secret.API_KEY}&contentType=csv')
    print(response.status_code)


extracting_data()
