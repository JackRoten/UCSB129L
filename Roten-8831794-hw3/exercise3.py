#!/usr/bin/env python3
#
# Author: Jack Roten
# Class: Phys 129L
# Homework 3
# Exercise 3
#
# Plot historgram of Most Significant Digits of 2009 USA census data
#
#
#--------------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('CensusTownAndCityPopulation.csv')
dateData = df["7_2009"] #gives value columns

intMSDList = [] 
for ii in range(len(dateData)):
    strData = str(dateData[ii]) #single out one value from column and casts value to string
    strData = strData.replace(',','') #takes out commas
    strMSD = strData[0] #selects Most Significant Digit
    intMSD = int(strMSD) #casts string to integer
    intMSDList.append(intMSD) #populates list!

bins = 9 #sets # of bins on histogram (should = 9 bc 1,..,9)
plt.hist(intMSDList, bins, color = 'r') #initialize and plot data)
plt.title("Most significant digit recurrence") 
plt.xlabel("Most Significant Integer Values")
plt.ylabel("Recurrence")
plt.show() 
