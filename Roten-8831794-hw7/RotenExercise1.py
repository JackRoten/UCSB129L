#!/usr/bin/env python3


# 4 thin charged particle detectors at x =2,3,5,7cm have many 50 um wide
# strips that measure the y-coordinates of charged particles going through
# Note: if the width of the strip is w the y-coordinate uncertainty is w/sqrt(12
# Particles traveling along the y-axis in positive x direction decay some
# where in the detectors. You are interested in finding the x coordinate of the
# decay for a given pair of tracks. A simulation of many particle decays has
# been carried out and this simulated data is in file = straightTracks.txt
# make sure to look at the headers of the data
# X0, Y0 are the common point of origin of pair(Y0 is always 0)
# yij=digitzed corrdinate of track i at detector j
# all lengths in cm
#
# Using the yij and the known x positions of the four detectors to estimate X0.
# Do this by fittin gthe corrdinates of each track to a straight line.
# You can use either np.polyfit or curve_fit from scipy.optimize. From the
# straight line fit, for each pair, you can extract the intercepts of the two
# tracks with the y-axis: (X1 and X2). then check how well you are doing by
#
# making a histogram of
# X1-X0 and X2-X0 (put both on same histogram)
# Xav-X0 where Xav is the average of X1 and X2
# use ccHIstStuff.py box and put 100 bins between -500 and 500 um.
# We should find that Xav is usually a better estimate of X0 than X1 or X2
# 
# 
#
#


import pandas as pd
import scipy.optimize as sc
import numpy as np
import matplotlib.pyplot as plt

# file is in working directory
data = pd.read_csv("straightTracks.txt", sep=" ") 
data.columns = ['X0','Y0','y00','y01','y02','y03','y10','y11','y12','y13','0']
# Notice there is a '0' column this has no values and is irrelevnent to the
# data but is needed becuase there is a space at the end of each line
# so just don't use it for analyzing the data

# Will now use histogram example and ccHist to create a swell histogram
#

#plt.hist(data['X0'], bins =100)
#plt.title('X0')
#plt.show()

#plt.hist(data['y00'], bins =100)
#plt.title('y00')
#plt.show()

#plt.hist(data['y01'], bins =100)
#plt.title('y01')
#plt.show()

#plt.hist(data['y02'], bins =100)
#plt.title('y02')
#plt.show()

#plt.hist(data['y03'], bins =100)
#plt.title('y03')
#plt.show()

#plt.hist(data['y10'], bins =100)
#plt.title('y10')
#plt.show()

#plt.hist(data['y11'], bins =100)
#plt.title('y11')
#plt.show()

#plt.hist(data['y12'], bins =100)
#plt.title('y12')
#plt.show()

plt.hist(data['y13'], bins =50)
plt.title('y13')
plt.show()

# there are two tracks: a track 1 and a track 2
# these tracks will pass through four detectors
# We want to find the x corrdinate of the decay for a given pair of tracks

# will refer to tracks as yij, where the i component is the track number,
# here we have 0 and 1, so two tracks!!
# Next we will refer to j as the detector,

# So we should see a different distribution of signal for each combination
# I would think the track is diverging away from the origin in a linear fashion
# so we need to find that fashion?
# Are we going to look at the given distribution of data and estimate where the
# tracks are going? It seems that this would make some sense.
# But also at the same time this seems stupid... We'll he always gives up dumb
# problems. 
