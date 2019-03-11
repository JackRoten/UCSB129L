#!/usr/bin/env python3
#
# Jack Roten
# PERM#  8831794
# UCSB Physics 129L
# Homework 7
# Python -V = Python 3.7.1
#
# Exercise 1
#
#-------------------------------------------------------------------------------


import numpy as np
import matplotlib.pyplot as plt
import ccHistStuff as cc

# importing data
data = []
# x locations / where the detector is
x_detect = [2., 3., 5., 7.]
x1x0 = []
x2x0 = []
XavXo = []

''' straightTracks text has data in following format:
0	1	2	3	4	5	6	7	8	9 (columns)
X0 Y0 y00 y01 y02 y03 y10 y11 y12 y13
X0, Y0 = true common point of origin of pair (Y0 always 0)
yij = digitized coordinate of track i at detector j
j = 0/column3 & 6 x = 2;
j = 1/column4 & 7 x = 3;
j = 2/column5 & 8 x = 5;
j = 3/column6 & 9 x = 7 
All lengths in cm
'''
with open('straightTracks.txt', 'r') as f:
	data = [line.split() for line in f]
	
# calculating the curve fit/linear regression
i = 0
xAvg = []
while i < len(data):
	# for track 0
	x = [float(data[i][0]), 2.,3.,5.,7.]
	y_0 = [float(data[i][1]), float(data[i][2]), float(data[i][3]), float(data[i][4]), float(data[i][5])]
	m0, b0 = np.polyfit(x,y_0,1)
	xInter0 = -b0/m0
	x1x0.append(abs(float(data[i][0]) - xInter0))
	# for track 1
	y_1 = [float(data[i][1]), float(data[i][6]), float(data[i][7]), float(data[i][8]), float(data[i][9])]
	m1, b1 = np.polyfit(x,y_1,1)
	xInter1 = -b1/m1
	x2x0.append(abs(float(data[i][0]) - xInter1))
	xAvg.append((xInter0 + xInter1)/2)
	
	i += 1
	
#print(xAvg)

# calculate X average
i=0
while i < len(xAvg):
	XavXo.append(float(xAvg[i]) - float(data[i][0]))
	i += 1
	
	
#generate historgram

print('the mean of X1 and X2 = ', np.mean(x1x0))
seed = 12345
np.random.seed(seed)
fig, ax = plt.subplots()
contents, binEdges, _ = ax.hist(x1x0, np.linspace(-0.05,0.05), histtype='step', log=False, color='blue', label='X1-X0')
c2, bE2, _ = ax.hist(x2x0, np.linspace(-0.05,0.05), histtype='step', log=False, color='red', label='X2-X0')
#Had to change in ccHistStuff line 20 and line 21 to take in array
cc.statBox(ax, x1x0, binEdges)
cc.statBox(ax, x2x0, bE2)
cc.plotErr(ax, contents, binEdges, color='blue')
ax.set_xlim(binEdges[0], binEdges[-1])
#ax.set_ylim(0. , 1.4*np.max(contents))
ax.set_ylim(0. , 1.1*max( np.max(contents),np.max(c2) ))
ax.tick_params("both", direction='in', length=10, right=True)
ax.set_xticks(binEdges, minor=True)
ax.tick_params("both", direction='in', length=7, right=True, which='minor')
ax.set_title("X1-X0 and X2-X0")
fig.show()

# plotting x average
fig3, ax3 = plt.subplots()
c3, bE3, _ = ax3.hist(XavXo, np.linspace(-0.05,0.05), histtype='step', log=False, color='orange', label='Xav-X0')
cc.statBox(ax3, XavXo, bE3)
cc.plotErr(ax3, c3, bE3, color='purple')
ax3.set_xlim(bE3[0], bE3[-1])
ax3.set_ylim(0. , 1.4*np.max(c3))
ax3.tick_params("both", direction='in', length=10, right=True)
ax3.set_xticks(bE3, minor=True)
ax3.tick_params("both", direction='in', length=7, right=True, which='minor')
ax3.set_title("Xaverage - X0")
fig3.show()

input("Press any key to continue")
