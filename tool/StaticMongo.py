#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# Date: 23/Dec/2015
# File: StaticMongo.py
# Desc: find which books isnt in the mongo
#
# Produced By BR
from Utility import loadMatrixFromFile, appendMatrixToFileUtf
from IsbnCheckIn import IsbnCheckIn

filename = '/home/archer/Downloads/data.csv'
mat = loadMatrixFromFile(filename)
i = IsbnCheckIn('192.168.100.2', 27017)
Res = [] # store not ins

for row in mat:
    if not i.isIn(row[1]):
        print row[1], "not in database"
        Res.append(row)

appendMatrixToFileUtf('NotFound.csv', Res)
