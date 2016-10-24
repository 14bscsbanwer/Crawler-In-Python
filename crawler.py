#Bilal Anwer
#Reg #35940
##BSCS-4C

import os
import sys
import hashlib

from os.path import join
from os.path import basename

txt = {}

#NUMBER OF files
counter = 0

#Set Root Path
myPath = '/Users/Bilal/Desktop/'

#Indexing the Files
for root, dirs, files in os.walk(myPath):
    for file in files:
        if file.endswith(".txt"):#Check for .txt file
            counter = counter + 1

            txt[str(counter)] = join(root, file.title())#Put  the path and name in the Dictionary 

#hashtable for words
wordDict = {}
wordCount = 0

#Indexing the words
for x in range(1,counter+1,1):
    with open(txt[str(x)],"r") as f:
        for line in f:
            for word in line.split():
                wordCount = wordCount + 1
                sha1 = hashlib.sha1()
                sha1.update(word.lower())
                if str(sha1.hexdigest()) in wordDict.keys():
                        wordDict[str(sha1.hexdigest())] = wordDict[str(sha1.hexdigest())] + "," + str(x)
                else:
                    wordDict[str(sha1.hexdigest())] = str(x)

print ("Files Found: " + str(counter)+ "\n")
for keys,values in txt.items():
    print(values)
print ("Word Count: " + str(wordCount) + "\n")

#Infinite Search Loop
while(1):
    sTerm = str(raw_input(""))
    sha1 = hashlib.sha1()
    sha1.update(sTerm.lower())
    sha1 = sha1.hexdigest()
    result = ""

    #Check for filenames
    for x in range(1, counter + 1, 1):

        loc, fname = os.path.split(txt[str(x)])

        if sTerm.lower() in [f.lower() for f in fname.split(".")]:
            print ("Filename found: " + txt[str(x)] + "\n")

    if str(sha1) in wordDict.keys():
        result = wordDict[str(sha1)]
        result = result.split(",")
        tmp = ""

        for r in result:

            
            if tmp != r:
                print("Found In " + txt[str(r)] + "\n")
            tmp = r
    else:
        print("Not found in the text file" + "\n")
