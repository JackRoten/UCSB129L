#!/usr/bin/env python3
#
# Jack Roten
# PERM#  8831794
# UCSB Physics 129L
# Homework 8
# Python -V = Python 3.7.1
#
# Exercise 1
#
#--------------------------------------------------------------------------




import math
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt
from scipy import special
import ccHistStuff as cc
from iminuit import Minuit
# define some background pdf's
def b_pdf(x,p0):
    return np.exp(-p0*(x))*p0/(np.exp(-p0*(100))-np.exp(-p0*(200)))
def b_pdf2(x,q0,q1):
    return (q0*x+q1)/(q0*200**2/2+200*q1-(q0*100**2/2+100*q1))
def b_pdf3(x,r1,r2,r3):
    return (r1*x**2+r2*x+r3)/((200**3-100**3)*r1/3+(200**2-100**2)*r2/2+100*r3)

      
    
                
    
    
#load the text file
x = np.loadtxt("mass.txt")
#x = np.linspace(100,200,101)
x1 = 100.
x2 = 200.
nb = 20
bins = np.linspace(x1, x2, nb+1)
mu = 155
sigma = 5
#make histogram
f, a = plt.subplots()
c, b, _ = a.hist(x, bins, histtype='step')
cc.statBox(a, x, b)
a.set_xlim(b[0], b[-1])
a.tick_params("both", direction='in', length=10, right=True)
a.set_xticks(b, minor=True)
a.tick_params("both", direction='in', length=7, right=True, which='minor')
#f.show()
#input("press")

#include/exclude systematics on background shape
shapeSyst = True
s_pdf = stats.norm.pdf(x,mu,sigma)
def NLL2(S,B,p0):
    temp = np.log(S*s_pdf + B*b_pdf(x,p0))
    return S+B-temp.sum()
def NLL3(S,B,q0,q1):
    temp = np.log(S*s_pdf + B*b_pdf2(x,q0,q1))
    return S+B-temp.sum()
def NLL4(S,B,r1,r2,r3):
    temp = np.log(S*s_pdf + B*b_pdf3(x,r1,r2,r3))
    return S+B-temp.sum()


                                    
m = Minuit(NLL2, S=10., B=190.,p0=1.,print_level=1, errordef=0.5,error_S=1.0, error_B=1.0, error_p0=0.1)
m2 = Minuit(NLL3, S=10., B=190.,q0=-0.001,q1=20.,print_level=1, errordef=0.5,error_S=1.0, error_B=1.0, error_q0=0.001,error_q1=0.001)
m3 =  Minuit(NLL4, S=10., B=190.,r1=2.5,r2=1.,r3=1.,print_level=1, errordef=0.5,error_S=1.0, error_B=1.0, error_r1=0.001,error_r2=0.001,error_r3=0.001)


m.migrad()
m.minos()
m.print_param()
input("")
xxx, yyy, _ = m.mnprofile('S', subtract_min=True, bins=100, bound=(0,200))
fig3, ax3 = plt.subplots()
ax3.plot(xxx,yyy,linestyle='solid', color='b')
ax3.set_xlim(min(xxx), max(xxx)/3)
ax3.set_ylim(min(yyy), max(yyy)/5)
ax3.set_xlabel('S')
ax3.set_ylabel('deltaNLL')
ax3.plot([min(xxx), max(xxx)], [0.5, 0.5], linestyle='dashed', color='red')
ax3.plot([min(xxx), max(xxx)], [2.0, 2.0], linestyle='dashed', color='red')
ax3.plot([min(xxx), max(xxx)], [4.5, 4.5], linestyle='dashed', color='red')
#fig3.show()
#input("enter to see next fit")


m2.migrad()
m2.minos()
m2.print_param()
input("")
xxx1, yyy1, _ = m2.mnprofile('S', subtract_min=True, bins=100, bound=(0,200))
fig5, ax5 = plt.subplots()
ax5.plot(xxx1,yyy1,linestyle='solid', color='b')
ax5.set_xlim(min(xxx1), max(xxx1)/3)
ax5.set_ylim(min(yyy1), max(yyy1)/5)
ax5.set_xlabel('S')
ax5.set_ylabel('deltaNLL')
ax5.plot([min(xxx1), max(xxx1)], [0.5, 0.5], linestyle='dashed', color='red')
ax5.plot([min(xxx1), max(xxx1)], [2.0, 2.0], linestyle='dashed', color='red')
ax5.plot([min(xxx1), max(xxx1)], [4.5, 4.5], linestyle='dashed', color='red')
#fig5.show()
#input("press enter to see next fit")

m3.migrad()
m3.minos()
m3.print_param()
input("")
#xxx2, yyy2, _ = m3.mnprofile('S', subtract_min=True, bins=100, bound=(0,200))
#fig6, ax6 = plt.subplots()
#fig7, ax7 = plt.subplots()
#b = np.linspace(100,200,200)


#ax6.plot(xxx2,yyy2,linestyle='solid', color='b')
#ax6.set_xlim(min(xxx2), max(xxx2)/3)
#ax6.set_ylim(min(yyy2), max(yyy2)/5)
#ax6.set_xlabel('S')
#ax6.set_ylabel('deltaNLL')
#ax6.plot([min(xxx2), max(xxx2)], [0.5, 0.5], linestyle='dashed', color='red')
#ax6.plot([min(xxx2), max(xxx2)], [2.0, 2.0], linestyle='dashed', color='red')
#ax6.plot([min(xxx2), max(xxx2)], [4.5, 4.5], linestyle='dashed', color='red')
#fig6.show()
#input("enter something to see histogram plot superimpoosed")




#input("Carriage return to continue....")
fig8, ax8 = plt.subplots()
b = np.linspace(100,200,200)
c, b1, _ = ax8.hist(x, bins, histtype='step')
cc.statBox(ax8, x, b1)
ax8.set_xlim(b1[0], b1[-1])
ax8.tick_params("both", direction='in', length=10, right=True)
ax8.set_xticks(b, minor=True)
ax8.tick_params("both", direction='in', length=7, right=True, which='minor')

ax8.plot(b,5*(177*b_pdf(b,0.01291)+20*stats.norm.pdf(b,mu,sigma)), linestyle='solid', color='b')
fig8.show()
input("")

fig9, ax9 = plt.subplots()
b = np.linspace(100,200,200)


c, b2, _ = ax9.hist(x, bins, histtype='step')
cc.statBox(ax9, x, b2)
ax9.set_xlim(b2[0], b2[-1])
ax9.tick_params("both", direction='in', length=10, right=True)
ax9.set_xticks(b2, minor=True)
ax9.tick_params("both", direction='in', length=7, right=True, which='minor')

b = np.linspace(100,200,200)
ax9.plot(b,5*(180.*b_pdf2(b,-0.08738,20.2)+20.*stats.norm.pdf(b,mu,sigma)), linestyle='solid', color='b')
fig9.show()

input("")

fig10, ax10 = plt.subplots()


c, b3, _ = ax10.hist(x, bins, histtype='step')
cc.statBox(ax10, x, b3)
ax10.set_xlim(b3[0], b3[-1])
ax10.tick_params("both", direction='in', length=10, right=True)
ax10.set_xticks(b, minor=True)
ax10.tick_params("both", direction='in', length=7, right=True, which='minor')




b = np.linspace(100,200,200)
ax10.plot(b,5*(181*b_pdf3(b,-0.002939,0.07699,122.7)+19*stats.norm.pdf(b,mu,sigma)), linestyle='solid', color='b')
fig10.show()
print("The value of S, is:")
print("S= 20+/-7+/-2")
input("")




