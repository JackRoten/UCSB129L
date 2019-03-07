#!/usr/bin/env python 3
#
# HOMEWORK 7 EXERCISE 1
# A program using the yij and the known x positions of the four detectors 
# to estimate X0.
#
# Rosio 03/03/19
#----------------------------------------------------------------------------

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import math
from scipy.optimize import curve_fit

'''
Each line of this file has information for one pair of tracks as follows:
X0 Y0 y00 y01 y02 y03 y10 y11 y12 y13

where:

X0, Y0 = true common point of origin of pair (Y0 always 0)

yij = digitized coordinate of track i at detector j

'''

'''
# Code below shows that each 'line' is considered to be the 10 values.



# Read a a file and assign, per space, each value to each variable
# at each -\ n- restart the assignment
filepath = 'campagnari_3/python/straightTracks.txt'  
with open(filepath) as myFileToRead:  
   line = myFileToRead.readline()
   cnt = 1
   while line:
       print("Line {}: {}".format(cnt, line.strip()))
       line = myFileToRead.readline()
       cnt += 1
'''

# Read a a file and assign, per space, each value to each variable
# at each \n restart the assignment

filepath = 'campagnari_3/python/straightTracks.txt'  
with open(filepath) as myFileToRead:

   for cnt, line in enumerate(myFileToRead):
       #print("Line {}: {}".format(cnt, line))
       splitLine = line.strip().split(' ')
       #print("Split Line ", cnt, ": ", splitLine)
       # Now splitLine is an array of 0-9 values 

       X0, Y0, y00, y01, y02, y03, y10, y11, y12, y13= [float(x) for x in splitLine]
       
       xVals = [2., 3., 5., 7.]

       uncertYVals = 50. * .0001 * (1./math.sqrt(12.))
       theUncertArr = [uncertYVals, uncertYVals, uncertYVals, uncertYVals]
       yValsT0 = [y00, y01, y02, y03]
       
       yValsT1 = [y10, y11, y12, y13]
       fitT0b, t0m = np.polyfit(xVals, yValsT0, 1, w=theUncertArr)
       fitT1b, t1m = np.polyfit(xVals, yValsT1, 1, w=theUncertArr)
       print("fitT0b:", fitT0b, '\n', "t0m:", t0m, '\n',"fitT1b:", fitT1b, '\n', "t1m:", t1m)

       plt.plot(xVals, yValsT0, '.')
       plt.plot(xVals, float(fitT0b) + float(t0m) * xVals, '-')
       plot.show()




'''
        import numpy as np
		from numpy.polynomial.polynomial import polyfit
		import matplotlib.pyplot as plt

		# Sample data
		x = np.arange(10)
		y = 5 * x + 10

		# Fit with polyfit
		b, m = polyfit(x, y, 1)

		plt.plot(x, y, '.')
		plt.plot(x, b + m * x, '-')
		plt.show()
'''










