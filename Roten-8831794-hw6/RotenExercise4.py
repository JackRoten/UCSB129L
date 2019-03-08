#!/usr/bin/env python3
#
# Jack Roten
# PERM#  8831794
# UCSB Physics 129L
# Homework 6
# Python -V = Python 3.7.1
#
# Exercise 4
#
#-------------------------------------------------------------------------------

import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()

L = 100
n_x = 4
n_y = 4
k_x = np.pi/L
k_y = np.pi/L



# Make data.
X = np.arange(0, L, 0.25)
Y = np.arange(0, L, 0.25)
X, Y = np.meshgrid(X, Y)
phi = np.sin(n_x*k_x*X)*np.sin(n_y*k_y*Y)
pdf = phi**2
# R = np.sqrt(X**2 + Y**2)


# Plot the surface.
surf = plt.contourf(X, Y, pdf, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)



# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()
