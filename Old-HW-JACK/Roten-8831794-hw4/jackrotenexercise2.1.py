#!/usr/bin/env python3
#
# Jack Roten
# PERM#  8831794
# UCSB Physics 129L
# Homework 4
# Python -V = Python 3.7.1
#
# Exercise 2
#
#
#-------------------------------------------------------------------------------

#Imports:
import argparse
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import ccHistStuff as cc


# Define the arguments --------------------
''' 
Improvments here might inlcude putting all these arguments into a class or 
object in another file, to be more clean
'''

parser =  argparse.ArgumentParser(description="Generate and plot Poisson variable. Calculate pvalue of observed")

#required argument in order to get the mean
parser.add_argument('-m','--mean', help='Mean of the Poisson', required=True, type=float)

#optional to add a number different than 10000
parser.add_argument('-n', '--nev', help='No. to generate. Default=10K', required=False, type=int, default=10000)

#optional to create a minimum value for the plot
parser.add_argument('-L', '--Low', help='Minimum for plot', required=False, type=int)


#optional to create a maximum for the plot
parser.add_argument('-H', '--High', help='Maximum for plot', required=False, type=int)


#optional to give a random see number
parser.add_argument('-s', '--seed', help='Random seed. Default=10', required=False, type=int, default=1)


#required specification for the number of observed events
parser.add_argument('-o', '--obs',  help='Number of observed events', required=True, type=int)

#required argument for the uncertainty on the mean of of a poisson distribution
parser.add_argument('-u', '--un', help='uncertainty on mean of poisson', required=True, type=float)

#Boolean switch, if not specified will be false and a LogNormal distribution
#will be specified so add "-g" to get a gaussian distribution
parser.add_argument('-g', '--gaussian', help="if given uses Gaussian else use LogNormal, default LogNormal", action='store_true')

# This is a dictionary containing the arguments
args = vars(parser.parse_args())

#-----------------------------

# Extract the arguments
mean   = args['mean']  # mean drawn from Gaussian of logNormal
nev    = args['nev']   # number of events to generate from Poisson
seed   = args['seed']  # seed number
obs    = args['obs']   # observed number of events
un     = args['un']    # uncertainty in distribution
gorln  = args['guassian'] # boolean to specify if LogNormal or Gaussian
nsigma = 5.            # plot to \pm 5 sigma if not specified

#-------------------------------


'''

conditional statements based on optional user input

'''


# if the argument is provided then the value is used, else it is calulated
if args['Low'] == None:
    nMin = int(max(0., mean-nsigma*math.sqrt(mean)))
else:
    nMin = args['Low']

# if the argument is provided then the value is used, else it is calulated
if args['High'] == None:
    nMax = int(max(0., mean+nsigma*math.sqrt(mean)))
else:
    nMax = args['High']


# the histogram --------


# Initialize the random seed
np.random.seed(seed)
# Generate a bunch of poisson, providing the mean and the number of events
entries  = np.linspace(nMin-0.5, nMax+0.5, nMax-nMin+2)


if args['guassian'] == None:
    entries = np.random.lognormal(math.log(mean), math.log(1+sigma/mean) , N)
    labelplot = 'LogNormal'
else:
    entries = np.random.normal(mean, sigma, N)
    labelplot = 'Guassian'

contents, binEdges, _ = ax.hist(entries, b  , histtype='step',label=labelplot, log=False, color='blue')
cc.statBox(ax, entries, binEdges)
ax.set_xlim(binEdges[0], binEdges[-1])
ax.tick_params("both", direction='in', length=10, right=True)

#--------------------

    
# Make sure we dont have to low a maximum, good safety net to have
if nMax < 6: nMax=6 
if nMax < 1.2*obs: nMax=1.2*obs



#-------------------------------



# Generate a bunch of poisson, providing the mean and the number of events
#entries = np.random.poisson(mean, nev)



# Calculate the pvalue
boolArray = entries >= obs   # an array of True/False
nTail = boolArray.sum()      # the number of trues in the array
print("-------------------------------")
if nTail == 0:
    print("Not a single try with at least %d entries" %obs)
    print("Cannot calculate very small pvalue")
else:
    pvalue = nTail/nev
    nsigma = stats.norm.ppf(1-pvalue)
    print("pvalue        = ", pvalue)
    print("which corresponds to")
    print("No. of sigmas = ", nsigma)
    print("This number of sigma (n) is from the tail integral of a gaussian distribution.")
    print("In other words, for a gaussian of mean=0 and sigma=1, the integral from")
    print("n to infinity would be equal to ", pvalue)
print("-------------------------------")
    
# Define 1x1 figure
fig, ax = plt.subplots(1,1)

# the histogram

# show the figure
fig.show()
#plt.show() #(this would pause automatically)
input("Press any key to continue")

