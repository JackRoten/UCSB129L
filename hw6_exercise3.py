#!/usr/bin/env python3
#
# This is a plot of the function
# f(x) = Integral [exp(-x-y) * (x+y)^N G(y | mu sigma) dy]
# where G is a Gaussian for y of mean=mu and std dev=sigma
# with y>0
#
# It is plotted betwee x1 and x2
#
# HOMEWORK 6 EXERCISE 3
# This program also calculates the 95% CL
# through the method of Frequent Analysis
#
# Rosio 23 Feb 2019
#--------------------------------
import math
import argparse
import numpy as np
import matplotlib.pyplot as plt
import scipy
import scipy.stats as stats
import ccHistStuff as cc

# Define the arguments
parser =  argparse.ArgumentParser(description="Get the required parameters")
parser.add_argument('-N','--numberOfCounts', help='Enter the number(#) of counts as -N #', required=True, type=int)
parser.add_argument('-u','--uncertainty', help='Enter the uncertainty as -u #', required=True, type=float)
parser.add_argument('-m','--mean', help='Enter the mean as -m #', required=True, type=int)
# This is a dictionary containing the arguments
args = vars(parser.parse_args())

# Extract the arguments
N = args['numberOfCounts'] 
mu = args['uncertainty'] 
sigma = args['mean'] 
n = 10

# The function that multiplies the Gaussian
def ff(x,y,N):
    return np.exp(-x-y) * (x+y)**N

# parameters from problem
x1      = 0.
x2      = 11.
npoints = 100            # number of points in x to plot
ntoy    = 1000           # for MC integration of y
dx      = (x2-x1)/100
xar     = np.linspace(x1, x2, npoints) # the points in x to plot

# init random number
np.random.seed(1234567)

# an array for f(x) initialized to zero
far = np.zeros(npoints)

i 	   = 0
sValsWFract = []
for s in xar:
    B      = np.random.normal(mu, sigma, ntoy)  # pick y
    B      = B[ B > 0 ]      # require B>0
    thisN	= len(B) # usable B's
    for aB in B:
    	newMu = s + aB
    	aPos = np.random.poisson(newMu, n) #pick n # of counts
    	aPos1 = aPos[aPos < N] #aPos is an array of the counts
    	# fraction value of those which are n < N 
    	frac = len(aPos1)/len(aPos)
    	# an array with the s value j and the corresponding fraction value as j + 1
    	#anArray = [s, frac]
    	#sValsWFract.extend(anArray)
    	sValsWFract.append(s)
    	sValsWFract.append(frac)      
    ftoy   = ff(s, B, n)    
    far[i] = (1./thisN) * ftoy.sum()
    i      = i + 1

excludeSVals = []
for j in range(len(sValsWFract)):
	if sValsWFract[j] < 0.05:
		excludeSVals.append(sValsWFract[j-1])

print("95 %'CL limit (smallest excluded value of S) is: ", min(excludeSVals)) 


# now the plot
fig, ax = plt.subplots()
ax.plot(xar, far)
ax.set_xlim(x1,x2)
ax.set_ylim(0)
ax.grid(True, which='both')
fig.show()
input("Press any key to exit")
