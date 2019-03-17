#!/usr/bin/env python3
#
# 
# 
#
# RR 19 Feb 2019
#   
# Homework 5  
#-------------------------------------------
import argparse
import math
import numpy as np
import matplotlib.pyplot as plt
import scipy.constants

# Define the arguments
parser =  argparse.ArgumentParser(description="Get the desired RC Time Constant Tau")
parser.add_argument('-T','--tau', help='The RC Time Constant', required=True, type=float)

# This is a dictionary containing the arguments
args = vars(parser.parse_args())

# Extract the arguments
tau = args['tau'] 

# initial value of vOut is 0 at t=0 for vOut0


# initial step height
h = .1

# total time in microseconds
totT = 100

# initial time in microseconds
t_0 = 0

# arr is an array of time in increments of 0.05
finalT = 100
i = 0
arr = []

while i < finalT:
	arr.append(i)
	i += 0.05

# set vIn to pass onto lowPassFilterDifEq
# length of the array is 2000
a = 0
b = 1
c = 2
vInArr = []
j = 0

for val=arr[j] in arr:
	if a <= val < b:
		vIn = 1
		vInArr.append(vIn)
		if j >= 19:
			a += 2
			b += 2
			c += 2


		j+= 1
	else:
		vIn = -1
		vInArr.append(vIn)
		j+=1

print(vInArr)


# Finds value of vOut for a given t using step size h 
# and initial value vOut0 at t0. 
def rungeKutta(t, t0, vOut0): 



	# equation that is satisfied by the low-pass filter
	# definition
	def lowPassFilterDifEq(theT, vOut, vIn): 
    	vOutNew = (1 / tau) * (vIn - vOut)
    	return vOutNew



    # Count number of iterations using step size or 
    # step height h 
    n = (int)((t - t0)/h)  

    # Iterate for number of iterations 
    vOut = vOut0 

    for i in range(1, n + 1): 
        "Apply Runge Kutta Formulas to find next value of vOut"
        k1 = h * lowPassFilterDifEq(t0, vOut) 
        k2 = h * lowPassFilterDifEq(t0 + 0.5 * h, vOut + 0.5 * k1) 
        k3 = h * lowPassFilterDifEq(t0 + 0.5 * h, vOut + 0.5 * k2) 
        k4 = h * lowPassFilterDifEq(t0 + h, vOut + k3) 
  
        # Update next value of vOut
        vOut = vOut + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4) 
  
        # Update next value of t 
        t0 = t0 + h 
    return vOut 

#----------------------------------------
# Trouble updating the vIn as either 0 or 1 as the time was incremented 
# then would have been able to pass vIn into the lowPassFilterDifEq
# then take the return function of the diffEq and use it to calc the k1, k2, k3, k4 values
# would need to repeat this process for the total number of time values
# then we could plot the transient going away from 0 to 10 microseconds and the 
# steady state solution from 90 to 100 microseconds 

