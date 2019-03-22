#!/usr/bin/env python3
#
# Jack Roten
# PERM#  8831794
# UCSB Physics 129L
# Homework 8
# Python -V = Python 3.7.1
#
# Exercise 2
#
#--------------------------------------------------------------------------


from math import sqrt
import LVector as lv
import numpy as np

# function which calculates the energy and momentum of the 2 daughter particles 
def NRG_P(mass_parent, mass_daughter1, mass_daughter2):
    E1 = (mass_parent**2+mass_daughter1**2-mass_daughter2**2)/(2*mass_parent)
    E2 = (mass_parent**2+mass_daughter2**2-mass_daughter1**2)/(2*mass_parent)
    p1 = p2 = sqrt(E1**2-mass_daughter1**2)
    return E1, E2, p1, p2

# mass values for the first decay sequence
B = 5.28
D = 2.01
pion = 0.1396

# calling above function and passing in values for particle masses, creates a list 
BParticleDecayInfo = NRG_P(B, D, pion)

# each value from function
E_D = BParticleDecayInfo[0]
E_pion = BParticleDecayInfo[1]
p_D = BParticleDecayInfo[2]
p_pion = BParticleDecayInfo[3]

# outputed values
print (E_D, E_pion, p_D, p_pion)


#--> I was unable to finish this last problem as too much time was taken on learning the concepts and implementation of problem 1. After learning the basics of finding the values for a momentum four vector I calculated these based on the reference: http://www.phys.ufl.edu/~avery/course/4390/f2015/lectures/relativistic_kinematics_2.pdf .

#--> Next steps I would take:
#1. find energies and momenta for the other decay sequences
#2. understand how to rotate vectors with given class methods then implement this
#3. understand how to boost vectors with given class methods then implement this
#4. understand how to iterate this process for random, statistically determined values based off of different distributions, which relate to a sphere.
#5. check that this all comforms to the checkDecayChain.py program and prints oout graphs that look simplar to what is expected.
