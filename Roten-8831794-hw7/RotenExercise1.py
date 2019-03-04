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
#
