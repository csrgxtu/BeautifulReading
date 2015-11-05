#!/usr/local/env python
#
# Author: Archer Reilly
# Date: 27/Aug/2015
# File: BookInfo.py
# Desc: parse book info page
#
# Produced By CSRGXTU
from Download import Download
from bs4 import BeautifulSoup

class BookInfo(object):
    HTML = None
    UID = None
    BID = None
    Cookie = None
    Soup = None

    def __init__(self, uid, bid, cookie):
        self.reset()
        self.UID = uid
        self.BID = bid
        self.Cookie = cookie

        if not self.request():
            print "ERROR[BookInfo]: ", uid, bid, cookie
        else:
            self.Soup = BeautifulSoup(self.HTML, "lxml")

    def reset(self):
        self.HTML = None
        self.UID = None
        self.BID = None
        self.Cookie = None
        self.Soup = None

    def getIsbn(self):
        if not self.Soup:
            return False

        if self.Soup.find('div', {'id': 'attr'}):
            if len(self.Soup.find('div', {'id': 'attr'}).find_all('li')) == 0:
                return False
            if "ISBN:" in self.Soup.find('div', {'id': 'attr'}).find_all('li')[-1].text:
                return str(self.Soup.find('div', {'id': 'attr'}).find_all('li')[-1].text.replace('ISBN:', ''))
            else:
                return False
        return False

    def request(self):
        baseUrl = 'http://shaishufang.com/index.php/site/detail/uid/'
        postFix = '/status//category/none/friend/false'
        url = baseUrl + self.UID + '/ubid/' + self.BID + postFix

        d = Download(url, self.Cookie)
        if d.doRequest():
            return False

        self.HTML = d.getSOURCE()
        return True
