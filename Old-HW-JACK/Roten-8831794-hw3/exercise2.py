#!/usr/bin/env python3
#
# Author: Jack Roten
# Class: Phys 129L
# Homework 3
# Exercise 2
#
# Numerical calculation of the prime of a given function.
#
#--------------------------------------------------------------------

def f(x):
    return x**2-x**3

def fprime(x,h):
    return (f(x+h)-f(x))/h

def fprime2(x,h):
    return (f(x+h)-f(x-h))/(2*h)

for i in range(1,4):
    h = 1/(10**(3*i))
    print("for x=1 and h=",h, "f_prime with the first method is:", fprime(1,h))

    print("for x=1 and h=",h, "f_prime2 with the second method is:", fprime2(1,h))
    print()
    

