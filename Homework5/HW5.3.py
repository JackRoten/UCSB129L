#!/usr/bin/env python3
#
#Reads a text file with mass values of e+,e- pairs
#then makes a histogram of x
#
# CR 02/19/19
#------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
from ccHistStuff import statBox, plotErr


dataArray=np.loadtxt('mass.txt')


bins=16
binEdges= [0,17]

# Plot histogram of data and log scale on y axis. 
fig = plt.figure() # create a plot object
ax = fig.add_subplot(1,1,1) # Add a plot space (in this case the whole window)
hist = plt.hist(dataArray, bins = bins) # histogram plot
plt.xlabel('mass(GeV/c^2)')
plt.ylabel('number of particles with mass x')

statBox(ax, dataArray, binEdges) # adds statistics box to graph
plt.show() # have to tell python to show the plot!!




    
    
