#!/usr/bin/env python3
# StupidHWProgram2.py
# Prompts user to enter a sentence and print out a count of the number
# of words and the number of characters in the sentence.
#
# Jack Roten 23 Jan 19
#
#


sentence = input('Please write a sentce: ')

#for ii in range len(sentence):

words = sentence.split()
print(words)
print(len(words))

for ii in words:
    word = words[ii]
    letters = 

## Will count all individual letter in the words: Overkill for this assignment.
#from collections import Counter
#cnt = Counter()
#for ii in words:
#    for letters in set(ii):
#        cnt[letters]+=1
#print(cnt)

