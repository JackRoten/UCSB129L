#!/usr/bin/env python3
#
# Author: Jack Roten
# Class: Phys 129L
# Homework 3
# Exercise 4
# 
# Color map of probability distribution function 
#
#
# Jack Roten 08 Feb  19
#-------------------------------------------------------

#Import all needed packages for ploting 3D surface
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np

# Initialize values
L = 100 #Arbitrarily choosen
n_x = 2 
n_y = 5
k_x = np.pi/L 
k_y = np.pi/L 



# Make data.
X = np.arange(0, L, 0.25)
Y = np.arange(0, L, 0.25)
X, Y = np.meshgrid(X, Y)
phi = np.sin(n_x*k_x*X)*np.sin(n_y*k_y*Y)
pdf = phi**2

# Plotting the surface
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(X, Y, pdf, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)
ax.set_zlim(-.05, 1.01) #sets z axis limits
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
fig.colorbar(surf, shrink=0.5, aspect=5)
plt.show()

