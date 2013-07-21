#!/usr/bin/env python
import sys
import commands
import time

#Create Dictionary
vocab = dict()  # Dictionary words list
fileStr = "english."
numFiles = 4
wordLenThreshold=9
for j in range(0,numFiles):
    fileName = fileStr+""+str(j)
    ins = open( fileName, "r" )
    for line in ins:
        line = line.strip()
        vocab[line]=0
print "size of dictionary: " + str(len(vocab))   


def enumerate(word):
	keys = vocab.keys()
	inputDict  = dict()
	for i in range(0,len(word)):
		c = word[i]
		if(c not in inputDict):
			inputDict[c] = 1;
		else:
			inputDict[c] = inputDict[c]+1;
	for i in range(0, len(keys)):
		currentWord = keys[i]
		currentDict = dict()
		for j in range(0,len(currentWord)):
			c = currentWord[j]
			if(c not in currentDict):
				currentDict[c] = 1;
			else:
				currentDict[c] = currentDict[c]+1;
		result = 1;
		for j in range(0,len(currentWord)):
			c = currentWord[j]
			if( c not in inputDict):
				result = 0;
			elif(currentDict[c]> inputDict[c]):
				result = 0;
		if(result):
			print currentWord
	
def branch(currentWord, rem):
    if(currentWord in vocab):   # To check if word is in Dictionary
        print currentWord
    l = dict()
    for i in range(0,len(rem)):
        c = rem[i]
        if  c not in l:
            l[c] = 0
            branch(currentWord+c,rem[0:i] + rem[(i+1):]);
               

print 'enter the word to jumble'
word=raw_input()
print 'words in dictionary are '
start = time.clock()
if(len(word)<=wordLenThreshold):
	print "Using recursion"
	branch("", word)
else:
	print "Using exhaustive enumeration"
	enumerate(word)
print "Time taken is " +  str(time.clock() - start)	+ " secs"

