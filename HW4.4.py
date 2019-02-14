#!/usr/bin/env python 3
#
#takes f(x,y)=g(x,y)p(x,y), where only p(x,y) is a properly normalized pdf.
#Markov chain generated according to p(x,y) to compute the integral of prob 3
#
#CR 02/12/19
#----------------------------------------------------------------------------
import numpy as np
import math
import random

#PDF def

def p(x,y):
    return (x+y)/7

#Proposal fns

def proposal(x):
    step=1
    return x-step/2+step*np.random.random()

def proposal(y):
    step=1
    return y-step/2+step*np.random.rand()


#initialize random no.
np.random.seed(134569)

#Parameters of chain
xstart=1
ystart=1
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

def g(x,y):
    return 7 * (x+y)

def f(x,y):
    return g(x,y) * p(x,y)










 
        




        

    




    

            
        
            

    
            

        


        

        
        




    


