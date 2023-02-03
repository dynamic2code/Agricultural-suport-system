import pandas

class GettingData:
    def __init__(self):
        self.file = "kenya-climate-data-1991-2016-rainfallmm.csv"
    
    def extractingData(self):
        with open(self.file, 'r') as file:
            rows = csv.reader(file)
            for row in rows:
                year = row[0]
                month = row[1]
                monthlyAvarage = row[2]
        print(month)
        print("he")


obj = GettingData()
obj.extractingData