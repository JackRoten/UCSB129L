#!/usr/bin/env python3
#
# StupidHWProgram4.py
#
# 129L Homework Exercise 4
# Ouput all integers between 100 and 400(inlcude) such that all digits are even
#
# Jack Roten 23 Jan 19
#-------------------------------------------------------


def all_even(number):
    num_str = str(number)
    digit_bool = []
    for digit in num_str:
        if int(digit)%2 == 0:
            digit_bool.append(True)
        else:
            digit_bool.append(False)
    return digit_bool

mylist = [i for i in range(100, 401) if all(all_even(i))]

print(','.join([str(i) for i in mylist]))




