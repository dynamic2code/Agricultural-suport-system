import requests

class Getdata:
    def __init__(self,location, landSize, income) -> None:
        self.location = location
        self.landSize = landSize
        self.income = income

    def getuserinput(self):
        self.location = input('Enter your location (give string): ')
        self.landSize = int(input('Enter your land size in Acers (give a number): '))
        self.income = int(input('Enter your estimated income per year: '))
        
        # verifying the input to avoid errors 

        try:
            type(self.location) == str 
            type(self.landSize) == int
            type(self.income)   == int
        except:
            wrongInput = "Your input were out of range. \n Ensure your input marches with the direction"

            print(wrongInput)

class GetWetherdata():
    # return the wether condition 
    def guageClimate():
        pass
    def getInfoWithAPI():
        # use the location to get the wether soil and any other needed conditions
        # wether =
        pass
class CompareWithCropRequirments():
     pass

class EconomicFactor():
    pass

class BestPracticeActivities():
    pass