#!/usr/bin/env python3
#
# Jack Roten
# PERM#  8831794
# UCSB Physics 129L
# Homework 6
# Python -V = Python 3.7.1
#
# Exercise 2
#
#-------------------------------------------------------------------------------


import argparse
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import ccHistStuff as cc

parser = argparse.ArgumentParser(description="add parameters")
parser.add_argument('-N','--NNumber', action='store', type=int, required=True, help='N values')
parser.add_argument('-mu','--muNumber', action='store', type=int, required=True, help='mu value')
parser.add_argument('-sigma','--sigmaNumber', action='store', type=float, required=True, help='sigma value')

args=vars(parser.parse_args())

# The function that multiplies the Gaussian
def ff(x,y,N):

    return np.exp(-x-y) * (x+y)**N

# parameters from problem
N       = args['NNumber'] # i.e. 5
mu      = args['muNumber'] # i.e. 25
sigma   = args['sigmaNumber'] # i.e. .5 
x1      = -3.
x2      = 15.
npoints = 100            # number of points in x to plot
ntoy    = 1000           # for MC integration of y
dx      = (x2-x1)/100
xar     = np.linspace(x1, x2, npoints) # the points in x to plot

# init random number
np.random.seed(1234567)

# an array for f(x) initialized to zero
far = np.zeros(npoints)
i = 0
for x in xar:
    y      = np.random.normal(mu, sigma, ntoy)  # pick y
    y      = y[ y> 0 ]      # require y>0
    thisN  = len(y)         # how many "usable" y's do we really have?       
    ftoy   = ff(x, y, N)    
    far[i] = (1./thisN) * ftoy.sum()
    i      = i + 1

# now the plot

confPlus = mu+1.96*math.sqrt(mu/N)
confMinus = mu-1.96*math.sqrt(mu/N)

print(confPlus)
print(confMinus)

fig, ax = plt.subplots()
ax.plot(xar, far, color = 'r')
plt.axvline(x = confPlus)
plt.axvline(x = confMinus)
ax.set_xlim(x1,x2)
ax.set_ylim(0)
ax.grid(True, which='both')
fig.show()
input("press enter to continue")


# [x] takes arguments for N, mu, and sigma
# [] calculate 95% Baysean Confidence Level lower limit on S--- what is this?? 
#  What is the
# [x] S>0 to limit pdf I think this already taken care of
# [] normalize properly??
# []What is the value of S for which you can say that all true values of S can
# be excluded with at least 95% confidence? Make a not of your results for N=5
# N=1 when mu=3 and sigma=0.5

# [] what the heck is S?? I think S is where the x value is within 95% of the
# distrubution


# based off pg26 "Measurements and their Uncertainties" book:
# 95% of the measurements lie within +/-1.96sigma
# there is a mean, and standard deviation(n-1), 1.96 value, and 1/sqrt(N)factor
#
# 95% confidence level = (mean) +/- 1.96*sigma(n-1)/sqrt(N)
#
# It would be nice to better understand why this is.
#
