import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Note: this makes use of some "magic methods"
# to "overload" operators like "*" to define
# the multiplication of a triangle by a number (!)
# For a list of such possibilities, see
# http://www.ironpythoninaction.com/magic-methods.html

class LVector:
    """
    New Class for Four-Vector
    """
    
    # Initialized the Four-vector
    def __init__(self, x0, x1, x2, x3):
        """
        Initialize by passing the three points at the verteces.
        Each point can be a 2-element np.array of (x,y) or a list.
        We should probably protect against passing junk, but whatever.
        We will store the points as np.array
        """
        self.x0 = np.array(x0, dtype=float) # in case we pass a list
        self.x1 = np.array(x1, dtype=float) # in case we pass a list
        self.x2 = np.array(x2, dtype=float) # in case we pass a list
        self.x3 = np.array(x3, dtype=float) # in case we pass a list

        
    def copy(self):
        """
        make a copy
        """
        return LVector(self.x0, self.x1, self.x2, self.x3)

    def __str__(self):
        """
        Nicely formatted print
        """
        return " x0 = ({0}) \n x1 = ({1}) \n x2 = ({2}) \n x3 = ({3}".format(self.x0,self.x1,self.x2,self.x3)


    def __add__(self, other):
        """
        return the addition of 2 vectors
        """
        return  ((self.x0+other.x0), (self.x1+other.x1), (self.x2+other.x2), (self.x3+other.x3)) 

    def __sub__(self, other):
        """
        return the subtraction of 2 vectors
        """
        return  ((self.x0-other.x0), (self.x1-other.x1), (self.x2-other.x2), (self.x3-other.x3))

    #__rmul__ = __mul__ Alternative to defining two functions
    def __rmul__(self, num):
        return (self.x0*num, self.x1*num, self.x2*num, self.x3*num)

    def __mul__(self, num):
        return (self.x0*num, self.x1*num, self.x2*num, self.x3*num)


    def set_x0(self, num):
        """
        return the float of vector
        """
        self.x0 = num 
        return  (self.x0, self.x1, self.x2, self.x3)

    def set_x1(self, num):
        """
        return the float of vector
        """
        self.x1 = num
        return  (self.x0, self.x1, self.x2, self.x3) 

    def set_x2(self, num):
        """
        return the float of vector
        """
        self.x2 = num
        return  (self.x0, self.x1, self.x2, self.x3)

    def set_x3(self, num):
        """
        return the float of vector
        """
        self.x3 = num
        return  (self.x0, self.x1, self.x2, self.x3)

    def get_rlength(self):
        """
        return the length of a vector
        """
        return math.sqrt(self.x1*self.x1 + self.x2*self.x2 + self.x3*self.x3)

    def square(self):
        """
        return the square of a vector
        """
        return  ((self.x0*self.x0), (self.x1*self.x1), (self.x2*self.x2), (self.x3*self.x3)) 

    def get_rtlength(self):
        """
        return the vector in complex plane
        """
        return math.sqrt(self.x1*self.x1 + self.x2*self.x2)

    def get_r(self):
        return np.array([self.x1, self.x2, self.x3])

    def get_rt(self):
        self.x3 = 0
        d = np.array([self.x1, self.x2, self.x3])
        return d

    def phi(self):
        rvect = np.array([self.x1, self.x2, self.x3])
        newAr = np.array([])
        for num in rvect:
            toyAr = np.array([])
            b = np.append(toyAr, newAr)
        i = 0
        for anum in b:
            i += anum
        ans = math.sqrt(i)
        #x1axis = np.array([self.x1, 0, 0])
        x1axisMagn = math.sqrt(self.x1*self.x1)
        shit = math.fmod(math.atan2(ans,x1axisMagn), math.pi)
        return shit

    def theta(self):
        rvect = np.array([self.x1, self.x2, self.x3])
        newAr = np.array([])
        for num in rvect:
            toyAr = np.array([])
            b = np.append(toyAr, newAr)
        i = 0
        for anum in b:
            i += anum
        ans = math.sqrt(i)
        #x3axis = np.array([self.x3, 0, 0])
        x3axisMagn = math.sqrt(self.x3*self.x3)
        shit = math.fmod(math.atan2(ans,x3axisMagn),math.pi)
        return shit

    def eta(self):
        return 1

    def Y(self):
        return 1

    def boost(self, aListForBoost):
        gammaAr = []
        for aBeta in aListForBoost:
            gamma = 1/math.sqrt(1-aBeta*aBeta)
            gammaAr.append(gamma)
        # gammaAr is a list of 3 possible gammas



        #---------------------------
        ct = self.x0
        newCt = gammaAr[0] * (ct - aListForBoost[0]*self.x1)

        aRR = [self.x1, self.x2, self.x3]
        j=0
        newVals = [newCt]
        for val in aRR:

            newVals.append(val + ((-gammaAr[j]*ct + (gammaAr[j]*gammaAr[j])/(1+gammaAr[j])*(aListForBoost[j])*val) * aListForBoost[j]))


        return newVals

        

 