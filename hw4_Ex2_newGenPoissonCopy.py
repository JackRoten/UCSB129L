#!/usr/bin/env python3
#
# Generate and plot Poisson numbers
# 
# CC 29 Jan 2019
#     5 Feb 2019  also return pvalue
#----------------------------------------
import argparse
import sys
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import ccHistStuff as cc

# Define the arguments
parser =  argparse.ArgumentParser(description="Generate and plot Poisson variable. Calculate pvalue of observed")
parser.add_argument('-m','--mean', help='Mean of the Poisson', required=True, type=float)
parser.add_argument('-g', '--boolean', help='A boolean. Default=False',
                    action='store_true')
parser.add_argument('-u', '--uncertainty', help ='Specify uncertainty of Mean of the Poisson', required=False, type =float, default=5.)
parser.add_argument('-n', '--nev', help='No. to generate. Default=10K', required=False, type=int, default=10000)
parser.add_argument('-L', '--Low', help='Minimum for plot', required=False, type=int)
parser.add_argument('-H', '--High', help='Maximum for plot', required=False, type=int)
parser.add_argument('-s', '--seed', help='Random seed. Default=10', required=False, type=int, default=1)
parser.add_argument('-o', '--obs',  help='Number of observed events', required=True, type=int)

# This is a dictionary containing the arguments
args = vars(parser.parse_args())

# Extract the arguments
nev    = args['nev']   # number of events to generate
seed   = args['seed']
obs    = args['obs']
myBool = args['boolean']
nsigma = 5.
uncert = args['uncertainty']


def whichMean(uncert):
    mean   = args['mean']  # mean
    isGaus = args['boolean']
    print(isGaus)
    if isGaus == True:
        #use fluctuating mean
        fluxVals = []
        for i in range(5):
            gaussianFxnPoints = np.random.lognormal(mean, uncert, 1)
            fluxVals.append(float(gaussianFxnPoints))
        return fluxVals
    else:
        #use normal mean 
        mean = []
        mean.append(args['mean'])
        return mean

meanVal = whichMean(uncert)
# meanVal returns either 
# 1. An array of 5 floats that are each fluctuated means or
# 2. An array of 1 float that is the expected mean without uncertainty 

def doTheRest(mean, nsigma):

    if args['Low'] == None:
        nMin = int(max(0., mean-nsigma*math.sqrt(mean)))
    else:
        nMin = args['Low']

    if args['High'] == None:
        nMax = int(max(0., mean+nsigma*math.sqrt(mean)))
    else:
        nMax = args['High']

    # Make sure we dont have to low a maximum
    if nMax < 6: nMax=6
    if nMax < 1.2*obs: nMax=1.2*obs
 
    # Initialize the random seed
    np.random.seed(seed)

    # Generate a bunch of poisson
    entries = np.random.poisson(mean, nev)

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
    contents, binEdges, _ = ax.hist(entries, np.linspace(nMin-0.5, nMax+0.5, nMax-nMin+2), histtype='step', log=False, color='black')
    cc.statBox(ax, entries, binEdges)
    ax.set_xlim(binEdges[0], binEdges[-1])
    ax.tick_params("both", direction='in', length=10, right=True)

    # show the figure
    fig.show()
    # plt.show()  (this would pause automatically)
    input("Press any key to continue")


if len(meanVal) < 4:
    mean = meanVal[0]
    doTheRest(mean, nsigma)
else:
    # Iteration needed
    count = 0
    for aMean in meanVal:
        print(count)
        doTheRest(aMean, nsigma)
        count += 1

