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
    Cursor = None

    def __init__(self, host, port, username, password, database):
        self.DB = MySQLdb.connect(host, username, password, database)
        self.Cursor = self.DB.cursor()

    def InsertUsers(self, userModel):
        sql = "INSERT INTO Users(UserID, UserName, TotalBooks)  \
                VALUES('%d', '%s', '%d')" % \
                (userModel['UserID'], userModel['UserName'], userModel['TotalBooks'])

        try:
            self.Cursor.execute(sql)
            self.DB.commit()
        except:
            self.DB.rollback()
            return False

        return True

    def InsertBooks(self, bookModel):
        sql = "INSERT INTO Books(ISBN, BookName, UserID) \
                VALUES('%s', '%s', '%d')" % \
                (bookModel['ISBN'], bookModel['BookName'], bookModel['UserID'])

        try:
            self.Cursor.execute(sql)
            self.DB.commit()
        except:
            self.DB.rollback()
            return False
        return True

    def CloseDB(self):
        self.DB.close()
