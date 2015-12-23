#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# Date: 23/Dec/2015
# File: IsbnCheckIn.py
# Desc: give a isbn, check if in the database
#
# Produced By BR
from pymongo import MongoClient

class IsbnCheckIn(object):
    DB = None

    def __init__(self, host, port):
        client = MongoClient(host + ':' + str(port))
        self.DB = client['bookshelf']

        # pass

    def isIn(self, isbn):
        collection = self.DB['bookdetail']
        if collection.find_one({'isbn': isbn}):
            return True
        else:
            return False
        # pass
