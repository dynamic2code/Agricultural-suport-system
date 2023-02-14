import data_patterns
import pandas as pd
import csv

def extracting_data():
    file = "kenya-climate-data-1991-2016-rainfallmm.csv"
    data = pd.read_csv(file)
    mean_for_location = data['Rainfall - (MM)'].mean()
    print('This is the mean rainfall of the place so far', mean_for_location)
    years = []
    months = []

    with open(file, 'r') as f:
        rows = csv.reader(f)
        # me

        for row in rows:
            # print(row[0])
            if row[0] not in years:
                years.append(row[0])

            if row[1] not in months:
                months.append(row[1])
                #bbhb

    months.pop(0)
    years.pop(0)
    print("This are the unique years", years)
    print("this are the distinct months", months)

    columnList = years.insert(0,'month')
    monthsList = []
    for month in months:
        eachMonth = [month]
        with open(file, 'r') as f:
            rows = csv.reader(f)
            for row in rows:
                if row[1] == month:
                    eachMonth.append(row[2])
        monthsList.append(eachMonth)

    print(monthsList)
    #show parttens of the climate with  time
    # dataFrame = pd.DataFrame(columns = [columnList],
    #                          data= [monthsList])
    # print(dataFrame)


    #telling seasons
    #rainy season ,dry season and intermidiate

    rainnyMonths = []
    dryMonts = []
    intermidiateMonths = []






extracting_data()
