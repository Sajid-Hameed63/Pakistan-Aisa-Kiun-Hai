import csv
import matplotlib.pyplot as plt
from array import *

with open('Gapminder.csv', 'r') as myFile:
    data = list(csv.reader(myFile, delimiter=','))

def dataTypeConversion(rawList, dataType):
    convertedList = []
    previousValue = 0
    for item in rawList:
        if item != '':
            convertedList.append(dataType(item))
            previousValue = dataType(item)
        else:
            convertedList.append(previousValue) # replacing missing value with previous value
    return convertedList

def fetchIndices(data, columnIndex, searchItem):
    listRowIndices = []

    for i in range(len(data)):
        if data[i][columnIndex] == searchItem:
            listRowIndices.append(i)
    
    return listRowIndices

def fetchColumnData(data, columnIndex, hasHeader):
    listData = []

    for i in range(len(data)):
        listData.append(data[i][columnIndex])
    if hasHeader:
        return listData[1:]
    else:
        return listData

def fetchData(data, columnIndex, listRowIndices):
    listDataValues = []

    for i in range(len(listRowIndices)):
        listDataValues.append(data[listRowIndices[i]][columnIndex])
    return listDataValues

#to fetch indices of pakistan in csv file
paksitanIndices = fetchIndices(data,0,'Pakistan')
years = dataTypeConversion(fetchData(data,4,paksitanIndices),int)

countries = set(fetchColumnData(data,0,True))
indicators = data[0][6:]

Countries_Dictionary = {}

#collecting data of every country about its each indicator and storing it in Countries_Dictionary
for countryName in countries:
    countryIndices = fetchIndices(data,0,countryName)
    for Indicator_Name in indicators:
        Countries_Dictionary[(countryName,Indicator_Name)] = dataTypeConversion(fetchData(data,data[0].index(Indicator_Name),countryIndices),float)


#List of countries and indicators at which i will analyze
Countries = ['Pakistan','India','United States of America','China','Germany','Japan','Bangladesh','Turkey','United Kingdom']
PositiveIndicators = ['AgriculturalLand','DemocracyScore','Exports','Imports','IncomePerPerson','Oilconsumptionperperson','Ratioofgirlstoboysinprimaryandsecondaryeducation','Renewablewater','TotalhealthspendingperpersonUS','Tradebalance','Urbanpopulationgrowth','Longtermunemploymentrate']
##############NegativeIndicators =['Poverty','Murderedmen','Murderedwomen']

#Function to calculate average of selected indicators of a particular country and then coverting it in Positivepoints
def MarksCalculatorThroughPositiveIndicators(Country):

    IndicatorsAverage = []
    for i in PositiveIndicators:
        Val = 0
        List1 = Countries_Dictionary[(Country,i)]
        for j in List1:
            Val = Val + j
        IndicatorsAverage.append(int(Val/16))
        Val = 0
    for j in IndicatorsAverage:
        Val = Val + j

    return Val





#Function to Calculate average of selected indicators of selected Countries and then coverting them in points.
def PositivePointCalculator():

    PositivePointsOfCountries = []
    for Country1 in Countries:
        Value1 = MarksCalculatorThroughPositiveIndicators(Country1)
        PositivePointsOfCountries.append(Value1)

    return PositivePointsOfCountries

#Ploting overall ranking graph Of all countries depending on the selected Positive indicators.
plt.figure()
plt.ylabel("Marks")
plt.xlabel("Countries")
plt.bar(Countries,PositivePointCalculator(),label="Final graph for Positive Calculated Points")
#plt.bar(Countries,NegativePointsCalculator(),label="Negative Points")
plt.legend()
plt.title("On bases of OverAll Indicator's Marks")


#Graphs of indicators
for Indicator_Name in PositiveIndicators:
    plt.figure()
    plt.plot(years, Countries_Dictionary[('Pakistan',Indicator_Name)], 'green', label="Pakistan")
    plt.plot(years, Countries_Dictionary[('India',Indicator_Name)], 'red', label="India")
    plt.plot(years, Countries_Dictionary[('United States of America',Indicator_Name)], 'blue', label="USA")
    plt.plot(years, Countries_Dictionary[('China',Indicator_Name)], 'black', label="China")
    plt.plot(years, Countries_Dictionary[('Germany',Indicator_Name)], 'orange', label="Germany")
    plt.plot(years, Countries_Dictionary[('Japan',Indicator_Name)], 'yellow', label="Japan")
    plt.plot(years, Countries_Dictionary[('Bangladesh',Indicator_Name)], 'yellow', label="Bangladesh")
    plt.plot(years, Countries_Dictionary[('Turkey',Indicator_Name)], 'cyan', label="Turkey")
    plt.plot(years, Countries_Dictionary[('United Kingdom',Indicator_Name)], 'magenta', label="UK")
    plt.title(Indicator_Name)
    plt.legend(loc="best")



plt.show()
