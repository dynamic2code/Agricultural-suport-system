import pandas as pd
def extracting_data():

	file  = "kenya-climate-data-1991-2016-rainfallmm.csv"
	data = pd.read_csv(file)
#mean for all the years will be 
	mean_for_location = data["Rainfall - (MM)"].mean()
	print(mean_for_location)
#grouping the data by years to get the mean per year and get the climatic progression
	years = data.groupby("Year").count()
	print(years)
#grouping the data  into months to get the seasons of the location

extracting_data()
