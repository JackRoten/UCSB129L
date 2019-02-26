#!/usr/bin/env python3
#
# stupidHWProgram2.py
#
# Winter 2019 129L
# Homework Exercise 3
# Prompt user for sentence and remove dupilicated words and output sentence
# with duplicate words removed
#
# Jack Roten 25 Jan 19
#----------------------------------------------------------------------------


def remove_duplicates(userInput):
    wordList = []
    [wordList.append(ii) for ii in userInput if ii not in wordList]
    return wordList

sentence = input('Please enter a sentence, preferably with duplicate words: ')
sentence=' '.join(remove_duplicates(sentence.split()))
print(sentence)

