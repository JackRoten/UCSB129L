#!/usr/bin/env python3
# StupidHWProgram2.py
# Prompts user to enter a sentence and print out a count of the number
# of words and the number of characters in the sentence.
#
# Jack Roten 29 Jan 19
#
#----------------------------------------------------------------------

import string
from collections import Counter

phrase = input('Please enter a sentence: ')
phrase = phrase.translate(str.maketrans({key: None for key in string.punctuation}))
print('Number of words in sentence: ', len(phrase.split()))
print('Number of letters in sentence: ', sum(sorted(map(len, phrase.split()))))


    
    
