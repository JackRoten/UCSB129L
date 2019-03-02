







import numpy as np
import math
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


class LVector:
    """
    Triangle class in 2D
    """

    def __init__(self, inputvector):

     
        self.inputvector = np.array(inputvector) # in case we pass a list


    def copy(self):
        """
        make a copy
        """
        return LVector(self.inputvector)

    def __str__(self):
        return " p0 = ({0}) \n p1 = ({1}) \n p2 = ({2}) \n p3=({3})".format(self.inputvector[0],self.inputvector[1],self.inputvector[2],self.inputvector[3])

#defining operations
    
    def __add__(self, other):
        return LVector(self.inputvector+other.inputvector)

    def __sub__(self,other):
        return LVector(self.inputvector+other.inputvector)

    def __rmul__(self,num):
        return LVector(self.inputvector*num)

    def __mul__(self,num):
        return LVector(self.inputvector*num)

#defining functions
    
    def square(self):
        return LVector(self.inputvector**2)


    def set_x0(self,num):
        self.inputvector[0]=num
        return(self.inputvector)
    
    def set_x1(self,num): 
        self.inputvector[1]=num
        return(self.inputvector)

    def set_x2(self,num):
        self.inputvector[2]=num
        return(self.inputvector)

    def set_x3(self,num):
        self.inputvector[3]=num
        return(self.inputvector)

    def get_rlength(self):
        return LVector(self.inputvector[0]**2+self.inputvector[1]**2+self.inputvector[2]**2)

    def get_rtlength(self):
        return LVector(math.sqrt(self.inputvector[0]**2+self.inputvector[1]**2))

    def get_r(self):
        return np.array([self.inputvector[0],self.inputvector[1],self.inputvector[2]])
    
    def get_rt(self):
        self.inputvector[3]=0
        return(self.inputvector)


    def phi(self):
        rvect=np.array([self.inputvector[0],self.inputvector[1],self.inputvector[2],self.inputvector[3]])
        newAr=np.array([])
        for num in rvect:
            toyAr=np.array([])
            b=np.append(toyAr,newAr)

        i=0
        for anum in b:
            i+=anum
        ans=math.sqrt(i)
        xlaxisMagn=math.sqrt(self.inputvector[1]*self.inputvector[1])
        s=math.fmod(math.atan2(ans,xlaxisMagn),2*math.pi)
        return s

    def theta(self):
        rvect=np.array([self.inputvector[0],self.inputvector[1],self.inputvector[3]])
        newAr=np.array([])
        for num in rvect:
            toyAr=np.array([])
            b=np.append(toyAr,newAr)

            i=0
            for anum in b:
                i += anum
                ans=math.sqrt(i)
                x3axisMagn=math.sqrt(self.inputvector[3]*self.inputvector[3])
                s=math.fmod(math.atan2(ans,x3axisMagn),math.pi)
                return s

    def eta(self):
        return 1


    def Y(self):
        return 1


    def boost(self,aListForBoost):
        gammaAr=[]
        for aBeta in aListForBoost:
            gamma=1/math.sqrt(1-aBeta*aBeta)
            gammaAr.append(gamma)




        #gammaAr has 3 pos values


        ct=self.inputvector[0]
        newCt=gammaAr[0]*(ct-aListForBoost[0]*self.inputvector[1])
        aRR=[self.inputvector[1],self.inputvector[2],self.inputvector[3]]
        j=0
        newVals=[newCt]

        for val in aRR:
            newVals.append(val+((-gammaAr[j]*ct+(gammaAr[j]*gammaAr[j])/(1+gammaAr[j])*(aListForBoost[j]*val)*aListForBoost[j])))
        
         


            j+=1 



        return newVals



        
        



    

        

           

   

   
   


    
    
    


   
        

   

  
    
     