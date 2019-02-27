#!/usr/bin/env python3
#
# Jack Roten
# PERM#  8831794
# UCSB Physics 129L
# Homework 4
# Python -V = Python 3.7.1
#
# Homework 5, Exercise 3
#
#
#-------------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from ccHistStuff  import statBox, plotErr


#dataSet = np.load("dataSet.npy")#Loads numpy data set

# need to load a txt file, simply a list of numbers!! not too bad hopefully
dataSet = np.loadtxt('mass.txt')

#print(dataSet)
dataArray = np.array(dataSet) #creats a 1D  array populated with dataSet data 
bins = 17#
binEdges = [0,20]

# Plot histogram of data and log scale on y axis. 

fig = plt.figure() # create a plot object
ax = fig.add_subplot(1,1,1) # Add a plot space (in this case the whole window)
hist = plt.hist(dataArray, bins = bins, normed=True) # histogram plot

ax.set_yscale('log') #linear to log on y (allows us to visualize distribution better)

statBox(ax, dataArray, binEdges) # adds statistics box to graph
plt.show() # have to tell python to show the plot!!

## Problem: this is not ploting a histogram at the moment,
# Good: Numpy array is imported correctly
# Good: a figure is being created

# Bad: histo bars are not showinup on graph
