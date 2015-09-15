#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 13/Sep/2015
# File: util.py
# Desc: utilities
#
# Produced By BR(BeautifulReading)
import json

# loadIsbns
# load isbn from file
#
# @param inputFile
# @return isbns in list
def loadIsbns(inputFile):
  isbns = []
  with open(inputFile, 'r') as myFile:
    for line in myFile:
      isbns.append(line.rstrip())

  return isbns

# appendlst2file
# append a [] list to file
#
# @param lst
# @param outFile
# @return nothing
def appendlst2file(lst, outFile):
  with open(outFile, "a") as myFile:
    myStr = ''
    for item in lst:
      myStr = myStr + item.encode('utf8') + ','
    myFile.write(myStr + '\n')
    # myFile.write(",".join(map(lambda x: str(x), lst)) + "\n".encode("UTF-8"))
    myFile.close()

def ldUserAgents(fileName):
    tmpBuf = ''
    with open(fileName, 'r') as f:
        tmpBuf = f.read()

    return json.loads(tmpBuf)['brower']

# loadMatrixFromFile
# load string matrix from file
#
# @param inputFile
# @return lst 2 dim
def loadMatrixFromFile(inputFile):
  res = []
  with open(inputFile, 'r') as myFile:
    for line in myFile:
      res.append(line.rstrip().split(','))
  return res

# saveMatrixToFile
# save an string matrix to file
#
# @param outputFile
# @param matrix
# @return noe
def saveMatrixToFile(outputFile, matrix):
  with open(outputFile, 'w') as myFile:
    for row in matrix:
      myFile.write(','.join([str(x) for x in row]) + '\n')
    myFile.close()

# appendstr2file
# append string to file
#
# @param string
# @param outFile
# @return nothing
def appendstr2file(string, outFile):
  try:
    with open(outFile, "a") as myFile:
      myFile.write(string + "\n")
  except UnicodeEncodeError:
    pass
