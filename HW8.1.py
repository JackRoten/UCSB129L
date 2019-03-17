#!/usr/bin/env python 3
#
#Fit dataset of HW5 prob 3 to a background pdf and a signal component using an NLL fit
#
#CR 03/13/19
#--------------------------------------------------------------------------
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import special
import ccHistStuff as cc
from iminuit import Minuit


# Read the masses into an array 
mass = np.loadtxt("mass.txt")

# How many do we have, what is the max and min
#    print( len(mass) )
#    m1 = np.amax(mass)
#    m2 = np.amin(mass)
#    print(m1,m2)
# From te tests above, looks like 200 entries
# between 100 and 200?
# A reasonable binning may be 20 bisn
x1 = 100.
x2 = 200.
nb = 20
bins = np.linspace(x1, x2, nb+1)

# plot now
f, a = plt.subplots()
c, b, _ = a.hist(mass, bins, histtype='step')
cc.statBox(a, mass, b)
a.set_xlim(b[0], b[-1])
a.tick_params("both", direction='in', length=10, right=True)
a.set_xticks(b, minor=True)
a.tick_params("both", direction='in', length=7, right=True, which='minor')
f.show()

input("Carriage return to continue....")

#Doing the NLL fit

#not sure what an npz file is and why he is using it
#I think what we can do is make    files like these with the code for the histogram from
#HW5 which also contain the chosen pdf functions and signal function

# Flag to include/exclude the systematics 
# on the background shape
shapeSyst = True

# Read the arrays that were prepared for us separately
# b_pdf    = the default background hist pdf 
# b1_pdf   = 1st alternative to hist b_pdf
# b2_pdf   = 2nd alternative to hist b_pdf
# s_pdf    = the hist pdf for signal
# binCen   = the center of the hist bins
# binEdges = the edges of the bins
# The arrays were saved with this command:
# np.savez("histForMinuitFit.npz", b_pdf, b1_pdf, b2_pdf, s_pdf, d, binCen, binEdges,
#           b_pdf=b_pdf, b1_pdf=b1_pdf, b2_pdf=b2_pdf, s_pdf=s_pdf, d=d,
#          binCen=binCen, binEdges=binEdges)
npzfile  = np.load("histForMinuitFit.npz")#this would be our histogram from the HW
b_pdf    = npzfile['b_pdf']#chose a function that will generate a bunch of data for
#background
b1_pdf   = npzfile['b1_pdf']#both b1 and b2 are functions that we chose to do the fit
b2_pdf   = npzfile['b2_pdf']#should be decaying functions or lines with neg slope
s_pdf    = npzfile['s_pdf']#s should be gaussian function
d        = npzfile['d']
binCen   = npzfile['binCen']
binEdges = npzfile['binEdges']

# All pdfs should already be normalized to 1.
# But just in case, normalize them again
b_pdf  = b_pdf  / b_pdf.sum()
b1_pdf = b1_pdf / b1_pdf.sum()
b2_pdf = b2_pdf / b2_pdf.sum()
s_pdf  = s_pdf  / s_pdf.sum()


# Now comes the negative log likelihood function
#
# d, s_pdf, b_bdf, b1_pdf, b2_pdf are np.arrays 
# d      = contents of data histogram 
# s_pdf  = contents of signal pdf histogram 
# b_pdf  = contents of default background pdf histogram
# b1_pdf = contents of alternative 1 to b_pdf
# b2_pdf = contents of alternative 2 too b_pdf
# S      = number of signal events
# B      = number of background events
# alpha  = parameter to interpolate between pdfs
# Assume that pdf's are normalized, eg s_pdf.sum()=1

def NLL(S,B,alpha):#wtf is alpha and S and B are 
    
    # alpha=0  ---> use b_pdf
    # alpha=1  ---> use b1_pdf
    # alpha=-1 ---> use b2_pdf
    # (and smoothly interpolates vs. alpha)
    if alpha>0:
        new_b_pdf = b_pdf + alpha*(b1_pdf-b_pdf)
    else:
        new_b_pdf = b_pdf - alpha*(b2_pdf-b_pdf)    
    # should be already normalized, but make sure
    new_b_pdf = new_b_pdf / new_b_pdf.sum()  
    temp = d * np.log(S*s_pdf + B*new_b_pdf)
    return S + B - temp.sum() + alpha*alpha/2.

# Setup the fitter.  S, B, alpha are the initial guesses
# print_level=0 --> suppress print of intermediate information 
# errordef = 0.5   because for NLL 1 sigma errors are  from
#                  NLL-NLL(at minimum) = 0.5
# error_S, error_B, alpha: are initial steps to look for minimum
# We fix alpha=0 if shapeSyst=False
m = Minuit(NLL, S=10., B=500., alpha=0., print_level=1,
           errordef=0.5, error_S=1.0, error_B=1.0, error_alpha=0.1,
           fix_alpha=(not shapeSyst))

# Run the fitter
m.migrad()
m.minos()
m.print_param()

# Profile scan of the fitted function (NLL).
# At each FIXED value of S, fit again for B,
# extract the NLL at the minimum, subtract 
# the NLL at the GLOBAL minimum, and plot it
xxx, yyy, _ = m.mnprofile('S', subtract_min=True, bins=100, bound=(0,60))

# m.mnprofile does all the work... 
# Now we just plot the results
# deltaNLL = 0.5 (2, 4.5 ) corresponds to 1 (2, 3) sigma
fig3, ax3 = plt.subplots()
ax3.plot(xxx,yyy,linestyle='solid', color='b')
ax3.set_xlim(min(xxx), max(xxx))
ax3.set_ylim(0.)
ax3.set_xlabel('S')
ax3.set_ylabel('deltaNLL')
ax3.plot([min(xxx), max(xxx)], [0.5, 0.5], linestyle='dashed', color='red')
ax3.plot([min(xxx), max(xxx)], [2.0, 2.0], linestyle='dashed', color='red')
ax3.plot([min(xxx), max(xxx)], [4.5, 4.5], linestyle='dashed', color='red')
fig3.show()

# Show the data...first get fit parameters
fittedB = m.values['B']
fittedS = m.values['S']
fitteda = m.values['alpha']
if fitteda>0:
    bf_pdf = b_pdf + fitteda*(b1_pdf-b_pdf)
else:
    bf_pdf = b_pdf - fitteda*(b2_pdf-b_pdf)
bf_pdf = bf_pdf / bf_pdf.sum()
    
# Then plot stacked histograms of S and B
# lists with the data, colors, and labels of the two hist 
blah   = [binCen, binCen]
colors = ['blue', 'red']
names  = ['Background', 'Signal']
w2     = [fittedB*bf_pdf, fittedS*s_pdf]

fig42, ax42 = plt.subplots()
ax42.hist(blah, binEdges, histtype='stepfilled', log=True,
          color=colors, stacked='True', label=names, weights=w2, alpha=0.4)
ax42.errorbar(binCen, d, yerr=np.sqrt(d), linestyle='none', marker='o', 
              color='black', markersize=4)
ax42.set_ylim(0.1)
ax42.set_xlim(binEdges[0], binEdges[-1])
ax42.legend()
ax42.set_ylabel("Number of events")
fig42.show()
input('Enter something to quit')
