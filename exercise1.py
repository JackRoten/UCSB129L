#!/usr/bin/env python3

import numpy as np
import math
import matplotlib
import random
import matplotlib.pyplot as plt

N = int(input("Enter the number of pairs: "))
#x is a list
x = np.random.uniform(0,1,2*N)


#Every two numbers in the x-list are an ordered pair.
#make a function that checks if the ordered pair lies 
#in the circle. If the ordered pair does then increase
#the counter



def isInCircle(aList):
    counter = 0
    halfList = int(len(aList) / 2)
    for i in range(0, halfList):
        x = aList[i]
        y = aList[i+1]
        radius = 1
        xSq = pow(x, 2)
        ySq = pow(y, 2)
        xSqPySq = xSq + ySq
        if xSqPySq > radius:
            inside =  False
        else:
            points = [x, y]
            print (points)
            outside = True
            counter += 1

    return (counter, N)


def binomialDistFxn(theCount, ):
    estF = theCount
    

#How to make sure that n follows a binomial distribution?


#call the function to take in a list and check if its
#ordered pairs lie in the circle
a = isInCircle(x)
print (a)

#pass in the counter return value of a into b,
#which uses the counter and number of pairs to compute
#the value of binom dist fxn
b = binomialDistFxn(a)






'''
stuff i don't know i'll need 
-------------------------------------
#plt.scatter(x,y)
#plt.show
   
#count, bins, ignored = plt.hist(x, 15, normed = True)
#plt.plot(bins, np.ones_like(bins), linewidth = 2, color = 'r')
#plt.show()
'''
