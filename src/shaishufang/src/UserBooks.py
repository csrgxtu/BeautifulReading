#!/usr/bin/env python
# coding=utf-8
# Author: Archer Reilly
# Date: 27/Aug/2015
# File: UserBooks.py
# Desc: class for UserBooks list page
#
# Produced By CSRGXTU
import re
from Download import Download
from bs4 import BeautifulSoup

class UserBooks(object):
    HTML = None
    Cookie = None
    UID = None
    Page = None
    Soup = None

    def __init__(self, uid, cookie, page):
        self.reset()
        self.UID = uid
        self.Cookie = cookie
        self.Page = page

        if not self.request():
            print "ERROR[UserBooks]: ", uid, cookie, page
        else:
            self.Soup = BeautifulSoup(self.HTML, "lxml")

    def reset(self):
        self.HTML = None
        self.Cookie = None
        self.UID = None
        self.Page = None
        self.Soup = None

    def getTotalPageNumbers(self):
        if not self.Soup:
            return 0

        if self.Soup.find('ul', {'id': 'booksPage'}):
            if len(self.Soup.find('ul', {'id': 'booksPage'}).find_all('li')) == 0:
                return 0

            return int(self.Soup.find('ul', {'id': 'booksPage'}).find_all('li')[-2].text)

        return 1

    def getTotalBooks(self):
        if not self.Soup:
            return 0

        if self.Soup.find('ul', {'id': 'categoryList'}):
            if self.Soup.find('ul', {'id': 'categoryList'}).find('li'):
                return int(re.sub(r'[^\x00-\x7F]+',' ',self.Soup.find('ul', {'id': 'categoryList'}).find('li').find('a').text).strip())

        return 0

    def getUserName(self):
        if not self.Soup:
            return False

        if self.Soup.find('div', {'id': 'username'}):
            return self.Soup.find('div', {'id': 'username'}).find('span').text

        return False

    def getBids(self):
        bids = []
        if not self.Soup:
            return bids

        if self.Soup.find('ul', {'id': 'booksList'}):
            if len(self.Soup.find('ul', {'id': 'booksList'}).find_all('li')) == 0:
                return bids
            for item in self.Soup.find('ul', {'id': 'booksList'}).find_all('li'):
                bids.append(item.attrs['id'])

        return bids

    def request(self):
        baseUrl = "http://shaishufang.com/index.php/site/main/uid/"
        postFix = "/friend/false/category//status//type//page/"
        url = baseUrl + self.UID + postFix + str(self.Page)

        d = Download(url, self.Cookie)
        if d.doRequest():
            return False

        self.HTML = d.getSOURCE()
        return True
