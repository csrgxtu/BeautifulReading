#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# Date: 06/Nov/2015
# File: MySQLDB.py
# Desc: CRUD
#
# Produced By CSRGXTU
import MySQLdb

class MySQLDB(object):
    DB = None

    def __init__(self, host, port, username, password, database):
        self.DB = MySQLdb.connect(host, username, password, database)
        pass

    def InsertBooks(self):
        pass
