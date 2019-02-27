#!/usr/bin/env python3
#
# Jack Roten
# PERM#  8831794
# UCSB Physics 129L
# Homework 5
# Python -V = Python 3.7.1
#
# Homework 5, Exercise 6
#
#
#-------------------------------------------------------------------------------

#ask user input for tau value
tau = print(input("Please enter a tau value: "))

#low pass differential equation
def dVoutdt(t, Vout):
    t = np.linspace(0, len(t), 1000, endpoint=True)
    Vin = signal.square(2 * np.pi * .5 * t)
    return ((1/tau)*(Vin-Vout)) 
  
# Finds value of Vout for a given t using step size h 
# and initial value Vin at t0. 
def rungeKutta(t, Vout, t0, h): 
    # Count number of iterations using step size or 
    # step height h 
    n = (int)((t - t0)/h)  
    # Iterate for number of iterations 
    Vout = Vout 
    for i in range(1, n + 1): 
        "Apply Runge Kutta Formulas to find next value of y"
        k1 = h * dVoutdt(t, Vout) 
        k2 = h * dVoutdt(t + 0.5 * h, Vout + 0.5 * k1) 
        k3 = h * dVoutdt(t + 0.5 * h, Vout + 0.5 * k2) 
        k4 = h * dVoutdt(t + h, Vout + k3) 
  
        # Update next value of Vout
        Vout = Vout + (1.0 / 6.0)*(k1 + 2 * k2 + 2 * k3 + k4) 
  
        # Update next value of x 
        t0 = t0 + h 
    return Vout
  
# Driver method 
t0 = 0
Vout = 1
t = 10
h = 0.2
print ('The value of y at x is:', rungeKutta(t0, Vout, t, h)) 
