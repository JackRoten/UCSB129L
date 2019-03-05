#!/usr/bin/env python3
#
#Program creates a class to represent a 4-vector aka Lorentz vector
#
#CR 02/26/19
#-----------------------------------------------------------------------------
import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

#what i am doing is making a general layout for the class of lorentz vectors
#so if you look at profs code you have to replace each of the components with self.inputvector[0,1,2,3]
#define all of the vector addition/subtraction with a general definition using self.inputvector
#I suck too much to try the boosts, so if you want to give that a shot add it back  in cause           # I took it out

class LVector:
    """
    Triangle class in 2D
    """

    def __init__(self, inputvector):

     
        self.inputvector = np.array(inputvector, dtype=float) # in case we pass a list


    def copy(self):
        """
        make a copy
        """
        return LVector(self.inputvector)

    def __str__(self):
        """
        Nicely formatted print
        """
        return " p0 = ({0}) \n p1 = ({1}) \n p2 = ({2}) \n p3=({3})".format(self.inputvector[0],self.inputvector[1],self.inputvector[2],self.inputvector[3])

    def add(self, other):
        return LVector(self.inputvector+other.inputvector)

    def subtract(self,other):
        return LVector(self.inputvector+other.inputvector)

    def scalar_multiplication(self,inputvector):
        return LVector(self.inputvector*4)

    def square_of_vector(self,inputvector):
        return LVector(self.inputvector**2)

    def length_of_3vector(self,inputvector):
        return LVector(self.inputvector[0]**2+self.inputvector[1]**2+self.inputvector[2]**2+self.inputvector[3]**2)

    def component_of_3vector(self,inputvector):
        return LVector(sqrt(self.inputvector[0]**2+self.inputvector[1]**2))

    def array_of_3components(self,inputvector):
        return np.array(self.inputvector[0],self.inputvector[1],self.inputvector[2])

#    def phi_azimuthal_angle(self,inputvector):
#
#        for i in range (0,2*pi):
#           #make a for loop for this phi to iterate over the range
           

#    def theta_polar_angle(self,inputvector):
#        #make another for loop


    def side(self, i):
        """
        Length of side i.
        i = 0 --> length between p0 and p1
        i = 1 --> length between p1 and p2
        i = 2 --> length between p2 and p0
        If i is out of range, return -9999
        Should have better way of returning an error!!!!!
        """
        if i == 0:
            length = math.sqrt( np.square(self.inputvector[0]-self.inputvector[1]).sum())
        elif i == 1:
            length = math.sqrt( np.square(self.inputvector[1]-self.inputvector[2]).sum())
        elif i == 2:
            length = math.sqrt( np.square(self.inputvector[2]-self.p).sum())
        else:
            length = -9999
        return length

    def perimeter(self):
        """
        Perimeter of triangle
        """
        return self.side(0)+self.side(1)+self.side(2)

    def area(self):
        """
        Area of the triangle
        Use the "shoelace" formula (check wikipedia!)
        """
        d1 = self.p0[0] - self.p2[0]
        d2 = self.p1[1] - self.p0[1]
        d3 = self.p0[0] - self.p1[0]
        d4 = self.p2[1] - self.p0[1]
        return 0.5 * abs( d1*d2 - d3*d4 )

    def angle(self,i):
        """
        angle at point i in radians
        i = 0  point is p0
        i = 1  point is p1
        i = 2  point is p2
        If i is out of range, return -9999
        Should have better way of returning an error!!!!!
        """
        # v and w are vectors along the sides 
        if i == 0:
            v = self.p1 - self.p0
            w = self.p2 - self.p0
        elif i == 1:
            v = self.p2 - self.p1
            w = self.p0 - self.p1
        elif i == 2:
            v = self.p1 - self.p2
            w = self.p0 - self.p2
        else:
            return 999

        # scalar product v*w = abs(v)*abs(w)*cos(angle)
        vlength = math.sqrt( np.square(v).sum() )
        wlength = math.sqrt( np.square(w).sum() )
        return math.acos( (v*w).sum() / (vlength*wlength) )

    def translate(self, v):
        """
        Translate triangle by vector v
        v can be 2-element np.array of (x,y) or a list.
        We should probably protect against passing junk, but whatever.
        """
        w = np.array(v, dtype=float) # in case we pass a list
        self.inputvector[0]=self.inputvector[0]+w
        self.inputvector[1]=self.inputvector[1]+w
        self.inputvector[2]=self.inputvector[2]+w
        self.inputvector[3]=self.inputvector[3]+w
        

   

    def __rmul__(self, scale):
        """
        return triangles resized by scale keeping center in same place
        """
        new = self.copy()
        oldCenter = new.center()
        # put p0 at the origin
        new.translate(-new.p0)
        new.p1 = scale * new.p1
        new.p2 = scale * new.p2
        newCenter = new.center()
        new.translate(oldCenter-newCenter)
        return new

    def draw(self, fig, ax):
        """
        Draw the triangle
        """
        line0 = Line2D( [self.p0[0], self.p1[0]], [self.p0[1], self.p1[1]] )
        line1 = Line2D( [self.p1[0], self.p2[0]], [self.p1[1], self.p2[1]] )
        line2 = Line2D( [self.p0[0], self.p2[0]], [self.p0[1], self.p2[1]] )
        ax.add_line(line0)
        ax.add_line(line1)
        ax.add_line(line2)
        fig.show()
