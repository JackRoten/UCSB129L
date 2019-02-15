#!/usr/bin/env python3
#
# Jack Roten
# PERM#  8831794
# UCSB Physics 129L
# Homework 4
# Python -V = Python 3.7.1
#
# Exercise 3
#
#
#-------------------------------------------------------------------------------

import random
import numpy as np

# define fn
def f(x,y):
    return (x+2*y)*(x+y)


N=100000 # 100K MC points
x0=0 # lower x bound
x1=1 # upper  x bound
y0=2 # lower y bound
y1=4# upper y bound

x = x0 + (x1-x0) * np.random.random(N)
y = y0 + (y1-y0) * np.random.random(N)
f = f(x,y)
areas = f*((x1-x0)*(y1-y0))/N

integral= sum(areas)
print("integral" ,integral)

        


