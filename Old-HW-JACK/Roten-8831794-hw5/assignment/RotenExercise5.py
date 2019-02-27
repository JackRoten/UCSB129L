#!/usr/bin/env python3
#
# Jack Roten
# PERM#  8831794
# UCSB Physics 129L
# Homework 5
# Python -V = Python 3.7.1
#
# Homework 5, Exercise 5
#
#
#-------------------------------------------------------------------------------

from math import cos



def func(x): 
    return x*cos(x)-0.5
   
# Prints root of func(x) 

def bisection(a,b): 
  
    if (func(a) * func(b) >= 0): 
        print("You have not assumed right a and b\n") 
        return
   
    c = a 
    while ((b-a) >= 0.0001): 
  
        # Find middle point 
        c = (a+b)/2
   
        # Check if middle point is root 
        if (func(c) == 0.0): 
            break
   
        # Decide the side to repeat the steps 
        if (func(c)*func(a) < 0): 
            b = c 
        else: 
            a = c 
              
    print("The value of root is : ","%.4f"%c) 
      

# Initial values assumed 
a =0.6100
b =0.7000
bisection(a, b) 
