#!/usr/bin/env python3
#
#Performs MC integration with f(x,y)=(x+2y)(x+y) using 100K MC points
#
#CR 02/11/19
#------------------------------------------------------------------------
import random
import numpy as np

# define fn
def f(x,y):
    return (x+2*y)*(x+y)
N=100000
x0=0
x1=1
y0=2
y1=4

x = x0 + (x1-x0) * np.random.random(N)
y = y0 + (y1-y0) * np.random.random(N)
f = f(x,y)
areas = f*((x1-x0)*(y1-y0))/N

integral= sum(areas)
print("integral" ,integral)

        



