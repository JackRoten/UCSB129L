import argparse
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats
import ccHistStuff as cc

parser = argparse.ArgumentParser(description="add parameters")
parser.add_argument('-N','--NNumber', action='store', type=int, required=True, help='5')
parser.add_argument('-mu','--muNumber', action='store', type=int, required=True, help='3')
parser.add_argument('-sigma','--sigmaNumber', 'action=store', type=float, required=True, help='0.5')

args=vars(parser.parse_args())

# The function that multiplies the Gaussian
def ff(x,y,N):
	return (np.exp(-x-y) * (x+y)**N)

# parameters from problem
N       = args['NNumber'] # i.e. 5
mu      = args['muNumber'] # i.e. 3
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