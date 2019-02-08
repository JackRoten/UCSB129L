#!/usr/bin/env python3
#
# exercise4.py
# 
# Color map of probability distribution function 
#
#
# Jack Roten 06 Feb  19
#-------------------------------------------------------


from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')
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
#Z = np.sin(R)

# Plot the surface.
surf = ax.plot_surface(X, Y, pdf, cmap=cm.coolwarm,
                       linewidth=0, antialiased=False)

# Customize the z axis.
ax.set_zlim(-1.01, 1.01)
ax.zaxis.set_major_locator(LinearLocator(10))
ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

# Add a color bar which maps values to colors.
fig.colorbar(surf, shrink=0.5, aspect=5)

plt.show()

