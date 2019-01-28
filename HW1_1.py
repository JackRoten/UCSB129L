#!/usr/bin/env python3
#
# Prompt user to input one integer
# Output number squared if input is integer
# Output error if not integer and ask for another input
#
# Jack Roten 23 Jan 19
#-------------------------------------------------------


val=int(input('Please enter a number:'))
try:
    print(val**2)
    break
except ValueError:
    print('Input not an integer, Please enter an integer')

#make it so this loops back and asks again, how do you do this?

#val=int(input('Please enter a number: '))
#TorF=True
#while TorF == True:
#    if val is int:
#        print(val**2)
#        TorF = False
#    else:
#        print('Input is not an integer, Please enter an integer')
#        TorF = True
        

