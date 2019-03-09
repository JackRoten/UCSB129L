!/usr/bin/env python3
# Amalu Shimamura
# 4978292
# Physics 129L
# Homework 2
# All of my work so far... 1 through 3
# Due Feb. 1
# ---------------------------------------------------------------------------

#Problem 1
#----------------------------------------------------------------------------
# Write a program to prompt the user to enter an integer that will print out the# integer squared. If the user enters something that is not a number, it should # output an error and ask the user to try again.

while True:
    try:
        integer = int(input("Enter an integer: "))
        break
    except ValueError:
        print("The value you typed in is not an integer! Try again ")

print(integer*integer)



#-------------------------------------------------------------
# Question 2
# Write a program to prompt the user to enter a sentence and print out a count
# of the number of words and the number of characters in the sentence.Note that
# words can be separated by white spaces but also commas, etc.
#--------------------------------------------------------------

import re
sentence = input("Enter a sentence: ")
#using regex to match a set of characters with the command [\w'] 
words = re.findall(r"[\w']+", sentence)
stringCount = len(words)
print("Word Count is: ", stringCount)
charCount = 0
for x in range(0,stringCount):
    charCount += len(words[x])

print("The number of characters in the sentence is: ", charCount)



#--------------------------------------------------------------
# Problem3
# Same exercise as 2 but print out the same sentence with repeat words (if any) removed. For simplicity you can omit the punctuation in your answer
#--------------------------------------------------------------

# repeating the stuff used from homework2
import re
sentence = input("Enter a sentence: ")
words = re.findall(r"[\w']+", sentence)

# debug below to make sure words prints out
#print('words: ', words)
#create a temporary set to remove duplicate of the sentence
temp = set()
#list with duplicate words removed
updatedWords = []
for item in words:
    if item not in temp:
        temp.add(item)
        updatedWords.append(item)

#debut below to make sure duplicate words are removed
#print('updated words ', updatedWords)
stringCount = len(updatedWords)

# for loop to count the number of characters in the sentence
charCount = 0
for x in range(0,stringCount):
    charCount += len(updatedWords[x])

print("Word Count is: ", stringCount)
print("The number of characters in the sentence is: ", charCount)

#--------------------------------------------------------------
# Question 4
# Write a program that output all integers between 100 and 400 (included) such that all of their digits are even.
#--------------------------------------------------------------

def evenDigit(number):
	integer = str(number)
	returnDigit = []
# for each individual digit in the number
	for digit in integer:
# if its even %2 = 0
		if int(digit) % 2 == 0:
# if true, add it in the list
			returnDigit.append(True)
		else:
# else, ignore it
			returnDigit.append(False)
	return returnDigit

evenList = [i for i in range (100, 401) if all(evenDigit(i))]
print(','.join([str(i) for i in evenList]))

#--------------------------------------------------------------
# Question 5
# Write a program that output all integers between 100 and 400 (included) such that all of their digits are even.
#--------------------------------------------------------------

# Write a python program that runs the shell /bin/ls /etc command and writes the output of the
# shell command would then be available to python for further processing.

import os
os.system('/bin/ls /etc')


#--------------------------------------------------------------
# Question 6
# Write a program that asks for a number and return the prime factors of that number, with their relative powers. For example if the number was 4567956 it should return something like
# 2 to the power 2
# 3 to the power 1
# 191 to the power 1
# 1993 to the power 1
#--------------------------------------------------------------

from collections import Counter
import math

# function that will calculate the prime factors
def thePrimeFact(n):
	i = 2
	numbList = []
	while i * i <= n:
		if n % i:
			i += 1
		else:
			n //= i
			numbList.append(i)
	if n > 1:
		numbList.append(n)
	return numbList

# function that will print out as it iterates through, adding the string "to the power between each prime factorization
def printOut(m):
	numbSoul = thePrimeFact(m)
	counter = Counter(numbSoul)
	for i,j in counter.items():
		print(i, 'to the power ', j)

numbae = int(input("Enter the number you wanna factor: "))
printOut(numbae)
#print('[%s]' % ', '.join(map(str, numbList)))
