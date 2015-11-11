#!/usr/bin/env python
# coding=utf8
#
# Author: Archer Reilly
# Date: 06/Nov/2015
# File: MySQLDB.py
# Desc: CRUD
#
# Produced By CSRGXTU
import sys
import MySQLdb

class MySQLDB(object):
    DB = None
    Cursor = None

    def __init__(self, host, port, username, password, database):
        self.DB = MySQLdb.connect(host, username, password, database, charset='utf8')
        self.Cursor = self.DB.cursor()

    # userModel = {'UserID': 1, 'UserName': 'archer', 'TotalBooks': 34}
    def InsertUsers(self, userModel):
        sql = "INSERT INTO Users(UserID, UserName, TotalBooks, State)  \
                VALUES('%d', '%s', '%d', '%d')" % \
                (userModel['UserID'], userModel['UserName'], userModel['TotalBooks'], userModel=['State'])

        try:
            self.Cursor.execute(sql)
            self.DB.commit()
        except:
            self.DB.rollback()
            print "Unexpected error:", sys.exc_info()[0]
            return False

        return True

    # bookModel = {'ISBN': '34224323223', 'BookName': 'what the hell', 'UserID': 1}
    def InsertBooks(self, bookModel):
        sql = "INSERT INTO Books(ISBN, BookName, UserID, State) \
                VALUES('%s', '%s', '%d', '%d')" % \
                (bookModel['ISBN'], bookModel['BookName'], bookModel['UserID'], bookModel['State'])

        try:
            self.Cursor.execute(sql)
            self.DB.commit()
        except:
            self.DB.rollback()
            return False
        return True

    def CloseDB(self):
        self.DB.close()
