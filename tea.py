import pandas as pd
import csv


def extracting_data():
    # file = "kenya-climate-data-1991-2016-rainfallmm.csv"
    # data = pd.read_csv(file)
    # # mean for all the years will be
    # mean_for_location = data["Rainfall - (MM)"].mean()
    # print(mean_for_location)
	file = "kenya-climate-data-1991-2016-rainfallmm.csv"
	data = pd.read_csv(file)
	mean_for_location = data['Rainfall - (MM)'].mean()
	print('This is the mean rainfall of the place so far',mean_for_location)
	years =[]
	months = []
	
	with open(file,'r'):
		rows = csv.reader(file)
		for row in rows:
			if row[0] not in years:
				years.append(row[0])
				
			if row[1] not in months:
				months.append(row[1])
				
	years.pop(0)
	months.pop(0)
	print("This are the unique years",years)
	print("this are the distinct months",months)
							
    # grouping the data by years to get the mean per year and get the climatic progression
    # years = data.groupby("Year").count()
    # print(years)
    # # getting all the unique years and months for grouping pourposes
    # years = []
    # with open(file, 'r') as file:
    #     rows = csv.reader(file)
    #     for row in rows:
    #         if row[0] not in years:
    #             years.append(row[0])
    #             years.pop(0)
    # print(years)
# grouping the data  into months to get the seasons of the location

extracting_data()
