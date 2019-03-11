#!/usr/bin/env python3
# Jack Roten
# PERM#  8831794
# UCSB Physics 129L
# Homework 7
# Python -V = Python 3.7.1
#
# Exercise 2
#
#This code uses an existing program plotDataset.py from Homework 4 solutions and modifies it to fit a chi squared plot to the first 25 bins of the histograplotDataset.py from Homework 4 solutions and modifies it to fit a chi squared plot defined to an exponential function to the first 25 bins of the histogramm
#
#-------------------------------------------------------------------------------


import numpy as np
import matplotlib.pyplot as plt
import ccHistStuff as cc
import math

# read the data set
x = np.load("dataSet.npy")


# Defining the exponential function
def func(x, p):
	return p[0]*np.exp(-p[1]*x)

#Defining partial derivative function for our exponential
def dydp(i, x, p):
	if i == 0:
		return np.exp(-p[1]*x)
	elif i == 1:
		return -x*p[0]*np.exp(-p[1]*x)


#Calculating chisq for bins of size 0.5 from 0 to 12.5
def fchisq(N, cent, p):
	return ((N-func(cent, p))**2/N).sum()	

#Taking bin values as our y avlues
y = []
centers = np.arange(0, 12.5, 0.5)

for i in centers:
	counts = 0
	for n in x:
		if n > i and n < i+0.5:
			counts += 1
	y.append(counts)
y = np.array(y)
#Error for bin values
#To avoid singular matrix error during chisq calculation step, we must offset our own error to make it not totally proportional to yi
invyerr = []
for yi in y:
	invyerr.append(12/(yi+1))
invyerr = np.array(invyerr)

#Calculate covariance matrix from bin error
W = np.diag((invyerr))
#Initial guessing parameters
p =[8000, 0.45]
y0 = func(centers, p)

#Iteration process for fitting histogram to reasonable values of p0 and p1
for i in range(20):
	At = np.array([dydp(0, centers, p), dydp(1, centers, p)])
	A = (At.T).copy()
	dy = (np.array([(y-y0),])).T
	# matrix multiplication
	temp = np.matmul(At, W)
	temp2 = np.matmul(temp, A)
	temp3 = np.linalg.inv(temp2)
	temp4 = np.matmul(temp3, At)
	temp5 = np.matmul(temp4, W)
	dpar = np.matmul(temp5, dy)

	p[0] += dpar[0][0]
	p[1] += dpar[1][0]
	
	y0 = func(centers, p)
	chisq = fchisq(y, centers, p)

# Plotting stuff (default: one subplot in x and one in y)
thisFigure, thisAxes = plt.subplots()

# the bin edges (nbins + 1 because of lower and upper edge)
nbins = 25
bins  = np.linspace(0, 12.5, nbins+1)

# the histogram
fig, ax = plt.subplots()
contents, binEdges, _ = ax.hist(x, bins, histtype='step', log=False, color='black')

# We were asked to add labels and stat box
ax.set_xlabel('X')
ax.set_ylabel('Entries per 0.5')
cc.statBox(ax, x, binEdges)

# This is purely esthetics (personal preference)
ax.tick_params("both", direction='in', length=10, right=True)
ax.set_xticks(binEdges, minor=True)
ax.tick_params("both", direction='in', length=7, right=True, which='minor')
ax.set_xlim(0, 12.5)
plt.plot(centers, func(centers, p), 'r-')
ax.plot()
fig.show()

#Printing calculated p0, p1, and chi squared values
print("chisq = %f" %(chisq))
print("p0 = %f, p1 = %f" %(p[0], p[1]))
input('press enter to display next figure')

#Scan over chisq out to 4 sigma
fig2, ax2 = plt.subplots()
p0min = p[0] - 10*np.sqrt(temp3[0][0])
p0max = p[0] + 10*np.sqrt(temp3[0][0])
p1min = p[1] - 10*np.sqrt(temp3[1][1])
p1max = p[1] + 10*np.sqrt(temp3[1][1])
nscan = 100
p0 = np.linspace(p0min, p0max, nscan)
p1 = np.linspace(p1min, p1max, nscan)
ax2.set_xlabel('p0')
ax2.set_ylabel('p1')
ax2.set_xlim(p0min, p0max)
ax2.set_ylim(p1min, p1max)
z = np.zeros( shape = (nscan, nscan) )
for i0 in range(0, nscan):
	this_p0 = p0[i0]
	for i1 in range(0, nscan):
		this_p1 = p1[i1]
		z[i0][i1] =  fchisq(y, centers, (this_p0,this_p1)) - chisq

CS = ax2.contour(p0, p1, z, [2.30, 5.99, 9.21])
fmt = {}
strs = ['68%', '95%', '99%']

for l,s in zip( CS.levels, strs ):
	fmt[l] = s
ax2.clabel(CS, inline=True, fmt=fmt, fontsize=10)

ax2.plot(p[0], p[1], 'ko')

ax2.grid()

fig2.show()
input("press enter to close program")
