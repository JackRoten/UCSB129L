#!/usr/bin/env python3

import numpy as np
import math
import matplotlib
import random
import matplotlib.pyplot as plt

exactPi = math.pi
arr = [100, 1000, 10000, 100000]
for i in arr:
    
    N = i
    #x is a list
    x = np.random.uniform(0,1,2*N)


    #Every two numbers in the x-list are an ordered pair.
    #make a function that checks if the ordered pair lies 
    #in the circle. If the ordered pair does then increase
    #the counter

    def findFactorial(aNum):
        factorial = 1
        while aNum > 1:
            factorial = factorial * aNum
            aNum = aNum - 1
        return factorial
    


    def isInCircle(aList):
        counter = 0
        halfList = int(len(aList) / 2)
        for i in range(0, halfList):
            x = aList[i]
            difX = x-0.5
            y = aList[i+1]
            radius = 1
            xSq = pow(difX, 2)
            ySq = pow(y, 2)
            xSqPySq = xSq + ySq
            if xSqPySq > radius:
                inside =  False
            else:
                points = [x, y]
                print (points)
                inside = True
                counter += 1

                return (counter)


    def binomialDistFxn(theCount, N):
        estimatedF = theCount/N
        exactF = exactPi / 4
        estimatedPi = 4 * estimatedF
    
        #First find the factorials of theCount, N and their difference
        theCountFactorial = findFactorial(theCount)
        theNFactorial = findFactorial(N)
        theDifference = theCount - N
        theDifferenceFactorial = findFactorial(theDifference)
    
        #Use the factorial values with the Combination formula
        possibleCombos = theCountFactorial / (theNFactorial * theDifferenceFactorial)



        #---------Use either estimated F or exactF???------------------
    
        #f to the power of theCount
        fToThePow = pow(estimatedF, theCount)

        #(1-f) to the power of (N-theCount)
        oneMinusF = pow(1 - estimatedF, N - theCount)


        #binomial distribution calculation
        finalCalculation = (float(possibleCombos)) * (float(fToThePow)) * (float(oneMinusF))

        insideRoot = (estimatedF * (1 - estimatedF)) / N
   
        uncertaintyF = math.sqrt(insideRoot)

        piDiff = exactPi - estimatedPi
        anotherPiDiff = piDiff / exactPi
        percentDiffBtwnPis = anotherPiDiff * 100

        reversePi = estimatedPi - exactPi
        sigmaPi = 4 * uncertaintyF
        thePull = reversePi / sigmaPi
        print ("The pull is: ", thePull)
    
        return (finalCalculation, uncertaintyF, percentDiffBtwnPis)
    
    

    #How to make sure that n follows a binomial distribution?

    #call the function to take in a list and check if its
    #ordered pairs lie in the circle
    a = isInCircle(x)
    print ("The number of points inside the circle is: ", a)

    #pass in the counter return value of a into b,
    #which uses the counter and number of pairs to compute
    #the value of binom dist fxn
    b = binomialDistFxn(a, N)
    print(b)

