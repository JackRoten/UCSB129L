#!/usr/bin/env python3
#
# Author: Jack Roten
# Class: Phys 129L
# Homework 3
# Exercise 6
#
# random w
# 
#
#--------------------------------------------------------------------
  
import turtle
import numpy as np
import matplotlib.pyplot as plt
import random

def randomWalk(length):
    steps = []
    x,y = 0,0
    walkx,walky = [x],[y]
    for i in range(length):
        new = random.randint(1,4)
        if new == 1:
            x += 1
        elif new == 2:
            y += 1
        elif new ==3 :
            x += -1
        else :
            y += -1
        walkx.append(x)
        walky.append(y)
    return [walkx,walky]

walk = randomWalk(1000)

for x, y in zip(*walk):
    #multiply by 10, since 1 pixel differences are hard to see
    turtle.goto(x*10,y*10)
    
turtle.exitonclick()
