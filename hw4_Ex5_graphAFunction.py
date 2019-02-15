#!/usr/bin/env python3
import math
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import random

mu = 3
sigma = 0.5
N = 5
# mathematical function we calculate
def myFunct(x, y):
	return (math.exp(-(x+y))*((x+y)**N))


def gaussianPdf(mu, sigm):
	# drawing samples from the Gaussian distribution
	# y value to be 1000
	gaussPdf = np.random.lognormal(mu, sigma, 1000)
	#gaussPdf is an array with 1000 values
	return gaussPdf

# GaussPdf is an array with 1000 values each is a value of Y
gaussPdf = gaussianPdf(mu, sigma)

#To do 100 integrals
xMin = -3
xMax = 15
incrementBy = (xMax-xMin)/100

# Now calculate many integrals over y, ea. @ fixed x
# where x is from -3 to 15
arrXs = []
xNum = -3
lastNum = 15

while xNum < 15:
	arrXs.append(xNum)
	xNum += incrementBy
arrXs.append(lastNum)

arrWAvgGs = []
# Integral formula
for valX in arrXs:
	total = 0
	for valY in gaussPdf:
		gOfY = myFunct(valX, valY)
		total += gOfY
	gOfYDivNumPicksAtThisX = total / len(gaussPdf)
	arrWAvgGs.append(gOfYDivNumPicksAtThisX)

# Take the array with integral values and plot it to it's x value.
fig,ax = plt.subplots(1)

# create some x data and some integers for the y axis
x = np.array(arrXs)
y = np.array(arrWAvgGs)

# plot the data
ax.plot(x,y)
plt.show()

# tell matplotlib which yticks to plot 
ax.set_yticks(arrXs)

# labelling the yticks according to your list
ax.set_yticklabels(arrWAvgGs)










