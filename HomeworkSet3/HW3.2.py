#!/usr/bin/env python3
#
#Takes f(x)=X^2(1-x) and computes f'(x)=f(x+h)-f(x) /h for h val=10^-2,10^-3,10^-4...
#
#CR 02/05/19
#------------------------------------------------------------------------------
def f(x):
    return x**2-x**3

def fprime(x,h):
    return (f(x+h)-f(x))/(float(h))

def fprime2(x,h):
    return (f(x+h)-f(x-h))/(float(2*h))

for i in range(1,4):
    h = 1/(10**(3*i))

    newh=format(h,'.20g')
    print("for x=1 and h= ",newh, "fprime with the first method is: ", fprime(1,h))

    print("for x=1 and h=",newh, "fprime2 with the second method is: ", fprime2(1,h))
    print()
    


    
   
    



    
