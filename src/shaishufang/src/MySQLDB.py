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
                (int(userModel['UserID']), userModel['UserName'], int(userModel['TotalBooks']), int(userModel['State']))

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
                (bookModel['ISBN'], bookModel['BookName'], bookModel['UserID'], 1)

        try:
            self.Cursor.execute(sql)
            self.DB.commit()
        except:
            self.DB.rollback()
            return False
        return True

    def InsertProxies(self, proxies):
        sql = "DELETE FROM Proxies WHERE ProxyID > 0"
        try:
            self.Cursor.execute(sql)
        except:
            self.DB.rollback()
            return False

        for i in range(1, len(proxies) + 1):
            sql = "INSERT INTO Proxies(ProxyID, Proxy) \
                VALUES('%d', '%s')" % \
                (i, proxies[i - 1])
            try:
                self.Cursor.execute(sql)
                self.DB.commit()
            except:
                self.DB.rollback()
                return False
        return True

    def ReadProxy(self):
        sql = "SELECT Proxy FROM Proxies ORDER BY RAND() LIMIT 0,1"
        self.Cursor.execute(sql)
        proxy = self.Cursor.fetchone()
        return str(proxy[0])

    def CloseDB(self):
        self.DB.close()
