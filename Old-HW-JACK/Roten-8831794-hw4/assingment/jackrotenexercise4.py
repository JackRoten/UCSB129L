#!/usr/bin/env python3
#
# Jack Roten
# PERM#  8831794
# UCSB Physics 129L
# Homework 4
# Python -V = Python 3.7.1
#
# Exercise 4
#
#
#-------------------------------------------------------------------------------

import numpy as np
import math
import random



def p(x,y):
    #defines function for p
    return (x+y)/7

def g(x,y):
    #defines funtion for g
    return 7 * (x+2*y)

def f(x,y):
    #defines function for f
    return g(x,y) * p(x,y)

#Proposal fns

def proposal(x):
    step=0.5
    return x-step/2+step*np.random.random()

def proposal(y):
    step=0.5
    return y-step/2+step*np.random.rand()


#initialize random no.
np.random.seed(134569)

#Parameters of chain
xstart=0.5
ystart=3
n=100000
nBurn=10000

#initialize chain as list
xlist=[xstart]
ylist=[ystart]

#do n+nBurn-1 steps
for i in range(n+nBurn-1):
    xp= proposal(xlist[-1])
    yp= proposal(ylist[-1])
    fnow=p(xlist[-1],ylist[-1])
    fnext=p(xp,yp)

    if xp <0 or xp>1 or yp<2 or yp>4:
        continue
    



    if np.random.random() < fnext/fnow:
        xlist.append(xp)
        ylist.append(yp)
    

    else:
        xlist.append(xlist[-1])
        ylist.append(ylist[-1])

        #put list into array, remove burn in part

xr=np.array(xlist[nBurn : ])
yr=np.array(ylist[nBurn : ])

print ("x values" , xr)
print ("y values" , yr)


 #Performing Integration using Markov Chain
 #--------------------------------------------------------

var1=g(xr,yr)
integral=(var1.sum())/len(xr)
print("integral",integral)
