#!/usr/bin/env python3
#
# Jack Roten
# PERM#  8831794
# UCSB Physics 129L
# Homework 5
# Python -V = Python 3.7.1
#
#  Exercise 1
#
#
#-------------------------------------------------------------------------------

# Write a function for the pendulum,
# length = length of rope
# use potential energy equation
# theta is the angle between the pendulum and the vertical
# alpha is the max angle of oscillation

import scipy
from scipy.integrate import quad
import numpy as np
import math
import matplotlib.pyplot as plt

pi = math.pi
a = 180
k = math.sin(a/2)
L = 1
g = 9.8
T_o = 2*pi*math.sqrt(L/g)
# L is the length of the pendulum and g is gravity
# a is the angle of the pendulum
# output of ratio of T/To
yVarr = []

# declare function
def t(b, a):
	#return ((2*T_o)/pi)*1/(math.sqrt(1 - k**2 * (math.sin(B))**2))
	return(2/pi)/math.sqrt(1-math.sin(a/2)**2*math.sin(b)**2)
	
#integral function 
for i in range(0,91):
	angle = pi * i /180
	yVarr.append(quad(t, 0, pi/2, args=(angle))[0])
	
#changing array to a numpy array to graph
a = np.arange(0, 91, 1)
pltA = np.array( a)
#res, err = quad(t,0,pi/2)
pltT = np.array( yVarr )
print(pltA)
print(pltT)
fig, ax = plt.subplots(figsize=(10,5))
ax.scatter(pltA, pltT)
#plt.plot( pltA, pltT/T_o, 's', color='b')
plt.xlabel(r'$\alpha$')
plt.ylabel( "T/To" )
plt.grid(False)
plt.xlim(0.0, 91.0)
plt.ylim(0.99, 1.19)
plt.show()
