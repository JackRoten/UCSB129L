#!/usr/bin/env python3
#
# jack Roten
# PERM#  8831794
# UCSB Physics 129L
# Homework 7
# Python -V = Python 3.7.1
#
# Exercise 1
#
#--------------------------------------------------------------------------

''' 
Right now this is only code for a single backgrond function along with 
a guassian function added together with NLL and then inputed into iminuit
Next steps:

1. Use the optimized values from iminuit to impose S + B ontop of the histogram
and also prvide error bars for each bin. 

2. Do this for two other functions(once we can do one, the others should not
be too bad!!)

'''

import pprint
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import special
from scipy.stats import powerlaw
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


# I think we want to replace the .npz with the mass.txt file, need mass and
# x1, x2, nb, bins

## All histogram and other graphing code is commented out
###----------------------------------------------------------------

# plot now
# f, a = plt.subplots()
# c, b, _ = a.hist(mass, bins, histtype='step')
# cc.statBox(a, mass, b)
# a.set_xlim(b[0], b[-1])
# a.tick_params("both", direction='in', length=10, right=True)
# a.set_xticks(b, minor=True)
# a.tick_params("both", direction='in', length=7, right=True, which='minor')
# f.show()

#input("Carriage return to continue....")

###-----------------------------------------------------------------

# initializing global paramters

# parameters normalized
a= -1.03e-5# make this more correct
b=0.01155 # make this more correct
mu=155
sigma=5
g_norm = 10

# creation of numpy array for x values
x_values=np.linspace(100, 200, 200)

# background function definition 
def b_pdf(x, a, b):
    return a*x+b

# signal guassian definition
def s_pdf(x, mu, sig):
    return g_norm*np.exp(-np.power(x - mu, 2.) / (2 * np.power(sig, 2.)))

# creates arrays for b_pdf and s_pdf
b_pdf=b_pdf(x_values,a ,b)
s_pdf=s_pdf(x_values,mu,sigma)


# Negative Log likelihood fit from notes: 
# "ExtendedNLLexample" slide: 22
def NLL(S,B,a,b):
    temp = np.log(S*s_pdf + B*b_pdf) 
    return S + B - temp.sum() + a*a/2. + b*b/2.

m = Minuit(NLL, S=70., B=130., a=-1.03e-5,b=0.01155, print_level=1,
           errordef=0.5, error_S=1.0, error_B=1.0, error_a=0.1, error_b=0.1)

m.migrad() # this line runs a fitting operation, will print out some crazy numbers
m.minos() # this is an operation to calculate the error on the fit, will print out some crazy numbers
m.print_param() # this prints out the parameters we want to see
