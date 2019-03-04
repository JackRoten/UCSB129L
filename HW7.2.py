#!/usr/bin/env python 3
#
#Performs Chi^2 fit of a histogram to exponential function= f(x)=p0e^(-p1/x)
#
#CR 03/04/19
#-----------------------------------------------------------------------------
import numpy as np
import matplotlib.pyplot as plt
import ccHistStuff as cc

# read the data set
x = np.load("dataSet.npy")

# Plotting stuff (default: one subplot in x and one in y)
thisFigure, thisAxes = plt.subplots()

# the bin edges (nbins + 1 because of lower and upper edge)
nbins = 40
bins  = np.linspace(0, 20, nbins+1)

# the histogram
fig, ax = plt.subplots()
contents, binEdges, _ = ax.hist(x, bins, histtype='step', log=True, color='black')

# We were asked to add labels and stat box
ax.set_xlabel('X')
ax.set_ylabel('Entries per 0.5')
cc.statBox(ax, x, binEdges)

# This is purely esthetics (personal preference)
ax.tick_params("both", direction='in', length=10, right=True)
ax.set_xticks(binEdges, minor=True)
ax.tick_params("both", direction='in', length=7, right=True, which='minor')
ax.set_xlim(0, 20)

fig.show()
input('Enter something to exit: ')
