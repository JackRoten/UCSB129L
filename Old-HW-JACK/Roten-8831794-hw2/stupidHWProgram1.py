#!/usr/bin/env python3
#
# stupidHWProgram1.py
# 
# Prompt user to input one integer
# Output number squared if input is integer
# Output error if not integer and ask for another input
#
# Jack Roten 28 Jan 19
#-------------------------------------------------------

while True:
    try:
        userInput = int(input("Please enter an integer: "))
    except ValueError:
        # if input is not an integer we will loop back.
        print("Type is not a number. ")
        continue
    else:
        #input was sucesfully parsed
        #we are ready to exit the loop
        print('Here is your inputed number squared: ', userInput**2)
        break
