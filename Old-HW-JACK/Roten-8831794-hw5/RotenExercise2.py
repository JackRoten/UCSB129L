#!/usr/bin/env python3
#
# Jack Roten
# PERM#  8831794
# UCSB Physics 129L
# Homework 5
# Python -V = Python 3.7.1
#
# Exercise 2
#
# builds a pixel map by building up a series zn with z0 taken at the center
# of each pixel. Map is of the complex plane z=x+iy w/ 640 horizontal pixels
# and 400 vertical pixels
#-------------------------------------------------------------------------------
import numpy as np
import math
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# Parameter for the plot
horizontalSize = 640
verticalSize = 400
c = complex(-0.79, 0.156)
zMax = 2
nMax = 255*2
ymin, ymax = -1.6,1.6
xmin, xmax = -1, 1
xLength = xmax - xmin
yLength = ymax - ymin

julia = np.zeros((horizontalSize,verticalSize))
# looping all pixels
for i in range(horizontalSize):
	for j in range(verticalSize):
		n = 0
		# Maps a pixel to a point in the complex plane
		xComponent = i / horizontalSize * xLength + xmin
		yComponent = j / verticalSize * yLength + ymin
		z = complex(xComponent, yComponent)
		
		# iterations
		while abs(z) <= zMax and n < nMax:
			z = z**2 + c
			n += 1
		shade = 1 - np.sqrt(n/nMax)
		ratio = n / nMax
		julia[i,j] = ratio
		
# creating figure/image
fig, ax = plt.subplots()
ax.imshow(julia, interpolation='nearest', cmap=cm.viridis)
# starting at tick zero z_0 point
xTickLabel = np.linspace(xmin, xmax, xLength / 0.5)
ax.set_yticks([(x-xmin) / xLength * horizontalSize for x in xTickLabel])
ax.set_yticklabels(['{:.1f}'.format(xtick) for xtick in xTickLabel])
yTickLabel = np.linspace(ymin, ymax, yLength/0.5)
ax.set_xticks([(y-ymin) / yLength * verticalSize for y in yTickLabel])
ax.set_xticklabels(['{:.1f}'.format(ytick) for ytick in yTickLabel])
fig.show()

input("Press <Enter> to exit") 
