
#!/usr/bin/env python 3
# generate 1000 B+ decay chains 
#CR 03/21/19
#--------------------------------------------------------------

import LVector as lv
import numpy as np
from math import sqrt


#first find 4 vectors for the 5 final state particles
#do the Lorentz transforms /boosts when in a moving reference 
#frame to get them into the lab frame
#Generate a Markov chain to see this reaction multiple times
#Save events in a pickle file


def NRG_P(mass_parent, mass_daughter1, mass_daughter2):
    E1 = (mass_parent**2+mass_daughter1**2-mass_daughter2**2)/(2*mass_parent)
    E2 = (mass_parent**2+mass_daughter2**2-mass_daughter1**2)/(2*mass_parent)
    p1 = p2 = sqrt(E1**2-mass_daughter1**2)
    return E1, E2, p1, p2

#1st decay event
Bplus=5.28
D0star=2.01
pionplus=0.1396

ParticleDecayInfo=NRG_P(Bplus,D0star,pionplus)

print(ParticleDecayInfo[0])
print(ParticleDecayInfo[1])
print(ParticleDecayInfo[2])
print(ParticleDecayInfo[3])

v1=np.array([ParticleDecayInfo[0],ParticleDecayInfo[1],ParticleDecayInfo[2],
ParticleDecayInfo[3]])
v1l=lv.LVector(v1)#lorentz vector for 1st decay

print("v1l:",v1l)

#2nd decay event
D0star=2.01
D0=1.86
pion0=0.1350

ParticleDecayInfo=NRG_P(D0star,D0,pion0)

print(ParticleDecayInfo[0])
print(ParticleDecayInfo[1])
print(ParticleDecayInfo[2])
print(ParticleDecayInfo[3])

v2=np.array([ParticleDecayInfo[0],ParticleDecayInfo[1],ParticleDecayInfo[2],
	ParticleDecayInfo[3]])
v2l=lv.LVector(v2)	
print("v2l:",v2l)#lvector for 2nd decay


#3rd decay event
D0=1.86
Kminus=0.494
pionplus=0.1396

ParticleDecayInfo=NRG_P(D0,Kminus,pionplus)

print(ParticleDecayInfo[0])
print(ParticleDecayInfo[1])
print(ParticleDecayInfo[2])
print(ParticleDecayInfo[3])

v3=np.array([ParticleDecayInfo[0],ParticleDecayInfo[1],ParticleDecayInfo[2],
	ParticleDecayInfo[3]])
v3l=lv.LVector(v3)
print("v3l:",v3l)#lvector of 3rd decay

#4th decay event
pion0=0.1350
gamma1=1
gamma2=gamma1

ParticleDecayInfo=NRG_P(pion0,gamma1,gamma2)

print(ParticleDecayInfo[0])
print(ParticleDecayInfo[1])
print(ParticleDecayInfo[2])
print(ParticleDecayInfo[3])

v4=np.array([ParticleDecayInfo[0],ParticleDecayInfo[1],ParticleDecayInfo[2],
    ParticleDecayInfo[3]])
v4l=lv.LVector(v4)
print("v4l:",v4l)#levector of 4th decay

















