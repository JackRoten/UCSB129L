#!/usr/bin/env python3
#
#Generates 10,000 numbers between 0 and 1 w/ pdf f(x)dx=(1+4x)/3
#plots numbers in histogram w/ bins of delta x=0.1
#Then curve g(x)=Af(x) is superimposed on the histogram
#
#CR 02/06/19
#------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import random
import matplotlib.mlab as mlab


np.random.seed(9112112)
r=np.random.random(10000)
x=(-1+np.sqrt(1+24*r))/4

plt.hist(x, bins = 10, range = [0,1], normed=True)

plt.show()
