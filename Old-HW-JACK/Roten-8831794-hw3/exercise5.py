#!/usr/bin/env python3
#
# Author: Jack Roten
# Class: Phys 129L
# Homework 3
# Exercise 5
#
#
# Jack Roten 06 Feb  19
#-------------------------------------------------------


import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.mlab as mlab


np.random.seed(9112112)
r=np.random.random(10000)
x=(-1+np.sqrt(1+24*r))/4

plt.hist(x, bins = 10, range = [0,1], normed=True)

plt.show()
    
#z = np.linspace(-10,10,1000)
#y = 1/(m.pi*(1+z**2)) #Theoretical Cauchy


#plt.plot(y,z)
plt.hist(valuesY, bins = 10, range = [0,1], normed=True)
plt.show()

