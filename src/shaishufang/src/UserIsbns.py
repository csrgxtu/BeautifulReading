#!/usr/local/env python
#
# Author: Archer Reilly
# Date: 28/Oct/2015
# File: UserIsbns.py
# Desc: get isbns of a user
#
# Produced By CSRGXTU
from UserBooks import UserBooks
from BookInfo import BookInfo

class UserIsbns(object):
    UID = None
    Cookie = None
    BIDS = []
    ISBNS = []

    TotalBooks = None
    UserName = None
    Proxy = None

    def __init__(self, uid, cookie, proxy):
        self.UID = None
        self.Cookie = None
        self.BIDS = []
        self.ISBNS = []
        self.Proxy = None

        self.UID = uid
        self.Cookie = cookie
        self.Proxy = proxy


    def run(self):
        # first, fillup the bids of the user
        u = UserBooks(self.UID, self.Cookie, 1, self.Proxy)
        totalPages = u.getTotalPageNumbers()

        self.TotalBooks = u.getTotalBooks()
        self.UserName = u.getUserName()

        if self.TotalBooks == 0:
            # jump over this uid
            # print "WARN[UserIsbns]: ", self.UID, self.Cookie
            return self.ISBNS

        for i in range(1, totalPages + 2):
            # print "INFO[UserIsbns]: ", self.UID, self.Cookie, i
            u = UserBooks(self.UID, self.Cookie, i, self.Proxy)
            self.BIDS.extend(u.getBids())

        # second, foreach bid in bids, get isbns
        for bid in self.BIDS:
            b = BookInfo(self.UID, bid, self.Cookie, self.Proxy)
            isbn = b.getIsbn()
            if isbn:
                # print "WARN[UserIsbns]: ", self.UID, bid, self.Cookie
                self.ISBNS.append(isbn)

        return self.ISBNS

    def getTotalBooks(self):
        return self.TotalBooks

    def getUserName(self):
        return self.UserName
