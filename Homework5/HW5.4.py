#!/usr/bin/env python 3
#
#program takes a 16 bit integer and decodes the three pieces of information
#user is prompted to print out channel number, time, and pulse height
#for a number
#
#CR 02/21/19
#-----------------------------------------------------------------------------
#Returns first 3 terms of bin num as an int
def decodechannelN(n):
    return (n & 0b1111)
#Returns next 4  terms
def decodetime(n):
    return(n & 0b11110000) >>4
#Returns next 10 terms
def decodepulse(n):
    return (n & 0b1111111100000000) >>8

def decode():
    #user picks a number to decode
    decodenum= int(input("Enter a 16bit integer in decimal form"))

    #decoder fns

    channelN=decodechannelN(decodenum)
    time=decodetime(decodenum)
    pulse=decodepulse(decodenum)

    #Prints the info decoded

    print("binary input:  ",bin(decodenum))
    print("channel num:   ",channelN, "or", bin(channelN))
    print("Time:   ", time, "or", bin(time))
    print("Pulse Height:   ",pulse, "or", bin(pulse))
decode()

