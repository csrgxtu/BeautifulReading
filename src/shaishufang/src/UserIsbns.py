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

    def __init__(self, uid, cookie):
        self.UID = uid
        self.Cookie = cookie

    def run(self):
        # first, fillup the bids of the user
        u = UserBooks(self.UID, self.Cookie, 1)
        totalPages = u.getTotalPageNumbers()
        if totalPages == 0:
            # jump over this uid
            print "WARN: ", self.UID, self.Cookie

        for i in range(1, totalPages + 1):
            print "INFO: ", self.UID, self.Cookie, i
            u = UserBooks(self.UID, self.Cookie, i)
            self.BIDS.extend(u.getBids())

        # second, foreach bid in bids, get isbns
        return self.BIDS
