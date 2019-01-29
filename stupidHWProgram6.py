#!/usr/bin/env python3
#
# stupidHWProgram6.py
#
# Winter 2019 129L
# Homework Exercise 6
#
# Ask for number and return the prime factors of that number, with their
# relative powers. 
#
# Jack Roten 25 Jan 19
#----------------------------------------------------------------------------
from collections import Counter

def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def prime_list(m):
    num = prime_factors(m)
    counter = Counter(num)
    for key,val in counter.items():
        print(key, 'to the power ', val)

    

userInput = int(input("Please enter an integer: "))
prime_list(userInput)
