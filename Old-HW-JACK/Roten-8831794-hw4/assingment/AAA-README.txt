#### Run instructions ####

Jack Roten
PERM# 8831794
UCSB Physiscs 129L
Homework 4
Python -V = Python 3.7.1

All Packages used:
import numpy as np			   to install: $ pip install numpy
import matplotlib.pyplot as plt		   to install: $ pip install matplotlib
import pandas as pd	    		   to install: $ pip install pandas
from ccHistStuff  import statBox, plotErr  py file is in immediate direcotory
import argparse	  	 	  	   comes with python
import sys				   comes with python
import math				   comes with python
import scipy.stats as stats		   to install: $ pip install scipy
import ccHistStuff as cc		   py file in immediate directory


--------------------------------------------------------------------------------

Exercise 1
----------
# Uses .npy data set: "dataSet.npy", included in immediate directory.

Specific Packages: numpy, matplotlib.pyplot, ccHistStuff.statBox, and
ccHistStuff.plotErr(in imediate directory)


BASH input:
$ ./jackrotenexercise1.py


Output 1
----------

ouputs histogram with statistics box


--------------------------------------------------------------------------------

Exercise 2
----------
Specific Packages: argparse, sys, math, numpy, matplotlib, scipy.stats, ccHistStuff.

BASH input:
$ ./jackrotenexercise2.py -m 5 -o 100 -g -u 1.1


Output 2
----------

will print out N=5, the reapeated experiments, plots and also print(example):

-------------------------------
pvalue        =  0.9891
which corresponds to
No. of sigmas =  -2.29383462031
This number of sigma (n) is from the tail integral of a gaussian distribution.
In other words, for a gaussian of mean=0 and sigma=1, the integral from
n to infinity would be equal to  0.9891
-------------------------------
Press any key to continue

5 times to provide 5 different trials

--------------------------------------------------------------------------------

Exercise 3
----------
Specific Packages: random and numpy as np

BASH input:
$ ./jackrotenexercise3.py


Output 3
----------

integral 46.999412052



--------------------------------------------------------------------------------

Exercise 4
----------
Specific Packages: numpy as np, math ,random

BASH input:
$ ./jackrotenexercise4.py


Output 4
----------

x values [ 0.5621075   0.48804404  0.54001443 ...,  0.28044067  0.42267716
  0.66185902]
y values [ 2.6274249   2.41749249  2.33552111 ...,  3.10797188  3.19301335
  3.21144174]
integral 46.5069844405



--------------------------------------------------------------------------------
Exercise 5
----------
Specific Packages: math, scipy.stats import norm, matplotlib.pyplot as plt,
numpy as np and random


BASH input:
$ ./jackrotenexercise5.py


Output 5
----------

Ouputs graph


--------------------------------------------------------------------------------
