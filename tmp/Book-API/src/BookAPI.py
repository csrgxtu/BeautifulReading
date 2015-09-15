#/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Author: Archer Reilly
# Date: 13/Sep/2015
# File: BookAPI.py
# Desc: Return the price and availability of the book
#
# Produced By BR(BeautifulReading inc)
from Download import Download
import json
from bs4 import BeautifulSoup

class BookAPI(object):
    ISBN = None
    HTML = None
    Json = None
    ResDict = None
    User_Agent = 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
    BaseUrl = 'http://book.douban.com/isbn/'

    def __init__(self, isbn, user_agent):
        self.ISBN = isbn
        self.User_Agent = user_agent
        self.ResDict = {}
        self.ResDict['error'] = False
        self.ResDict['msg'] = None
        self.ResDict['total'] = 0
        self.ResDict['isbn'] = isbn

    def api(self):
        if self.requestHtml():
            self.ResDict['error'] = True
            self.ResDict['msg'] = 'cant do http request'
            self.buildJson()
            return self.Json

        if self.parseHtml():
            self.ResDict['error'] = False
            self.ResDict['msg'] = 'no data available'
            self.buildJson()
            return self.Json

        self.buildJson()
        return self.Json
        # return self.ResDict

    def requestHtml(self):
        url = self.BaseUrl + self.ISBN
        # print url, self.User_Agent
        d = Download(url, self.User_Agent)
        if d.doRequest():
            return 1

        self.HTML = d.getSOURCE()

        return 0

    def parseHtml(self):
        # self.ResDict = {}
        data = {}
        try:
            soup = BeautifulSoup(self.HTML)
        except:
            self.ResDict['data'] = data
            self.ResDict['title'] = 'No Such Book'
            return 1

        title = soup.find('h1')
        if not title:
            self.ResDict['title'] = '我没有见过这本书'
            return 1

        self.ResDict['title'] = title.get_text().replace('\n', '')

        snippet = soup.find('div', id = 'buyinfo')
        if not snippet:
            snippet = soup.find('div', id = 'buyinfo-printed')
            if not snippet:
                return 1
            else:
                snippetLst = soup.find('div', id = 'buyinfo-printed').find_all('li')
        else:
            snippetLst = soup.find('div', id = 'buyinfo').find_all('li')

        if len(snippetLst) == 0:
            return 1

        del snippetLst[-1]
        self.ResDict['total'] = len(snippetLst)

        # for index in range(len(snippetLst)):
        #     tmpLst = snippetLst[index].find_all('span', class_ = '')
        #     data[index] = {tmpLst[0].get_text(): tmpLst[1].get_text().replace('\n', '').replace(' ', '')[0:5]}
        for item in snippetLst:
            try:
                tmpLst = item.find_all('span', class_ = '')
                data[tmpLst[0].get_text()] = tmpLst[1].get_text().replace('\n', '').replace(' ', '')[0:5]
            except:
                key = item.find_all('a')[1].get_text().replace(' ', '').replace('\n', '')
                value = item.find_all('span', class_ = 'buylink-price')[0].get_text()[4:]
                data[key] = value
        self.ResDict['data'] = data

        return 0

    def buildJson(self):
        self.Json = json.dumps(self.ResDict, ensure_ascii=False)
        return 0
