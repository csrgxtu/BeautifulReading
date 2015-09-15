#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 15/Sep/2015
# File: dedumplicate.py
# Desc: remove the dumplicate records from kaijuan.csv
#
# Produced By BR(BeautifulReading)
from util import loadMatrixFromFile, saveMatrixToFile

mat = loadMatrixFromFile('./kaijuan.csv')
newmat = []
tmpLst = []

for row in mat:
    if row[0] in tmpLst:
        print 'INFO: dumplicate ', row[0]
    else:
        newmat.append(row)
        tmpLst.append(row[0])

saveMatrixToFile('kaijuannodump.csv', newmat)
