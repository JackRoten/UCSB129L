#!/usr/bin/env python3
#
# 129L Homework Exercise 4
# Ouput all integers between 100 and 400(inlcude) such that all digits are even
#
#
# Jack Roten 23 Jan 19
#-------------------------------------------------------

#list numbers 100-400

numList = list(range(100, 401))
#print(numList)

for ii in numList:
    digitList = [int(kk) for kk in str(numList[ii])]
    for jj in digitList:
        if digitList[jj]%2 == 0:
            # recombine even digits into one number
            
    # Add even digit number to a list and print this list out, or print out
    # 
        else:
            break
        
# [] Ask TA/Prof is 100 is really included even though all digits are not
# even
        
    
