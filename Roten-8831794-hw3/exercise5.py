#!/usr/bin/env python3
#
# exercise5.py
# 
#
"""
Want 10000 random #s between 0 and 1 

"""
#
#
# Jack Roten 06 Feb  19
#-------------------------------------------------------


from __future__ import division
import scipy
import random
import matplotlib.pyplot as plt
import numpy as np
import math as m


valuesX = []
for ii in range(10000):
    R = random.random()
    valuesX.append(ii)

valuesY = []
for jj in range(len(valuesX)):
    Y = (1+4*valuesX[jj])/3
    valuesY.append(jj)

    
#z = np.linspace(-10,10,1000)
#y = 1/(m.pi*(1+z**2)) #Theoretical Cauchy


#plt.plot(y,z)
plt.hist(valuesY, bins = 10, range = [0,1], normed=True)
plt.show()

