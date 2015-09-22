#!/usr/bin/env python
# coding=utf-8
#
# Author: Archer Reilly
# Date: 22/Sep/2015
# File: BasicInfoParser.py
# Desc: parse the basic info from the book info page
#
# Produced By BR(BeautifulReading)
from bs4 import BeautifulSoup
import json

class BasicInfoParser(object):
    Soup = None
    HTML = None

    def __init__(self, html):
        self.HTML = html
        self.Soup = BeautifulSoup(self.HTML)

    def basicInfo(self):
        infoJson = {}
        keys = ['出版社:', '外文书名:', '丛书名:', '平装:', '语种：', '开本:', 'ISBN:', '条形码:', '商品尺寸:', '商品重量:', '品牌:', 'ASIN:']

        contentElement = self.Soup.find('td', class_='bucket').find('div', class_='content')
        if not contentElement:
            return infoJson

        for item in contentElement.find('ul').find_all('li'):
            # print item.find('b').get_text().encode('UTF-8').replace('\n', '').replace(' ', '')
            if item.find('b').get_text().encode('UTF-8') == '外文书名:':
                # print item.find('b').get_text().encode('UTF-8'), item.find('a').get_text()
                infoJson[item.find('b').get_text().encode('UTF-8')] = item.find('a').get_text()
                continue

            if item.find('b').get_text().encode('UTF-8') == '丛书名:':
                # print item.find('b').get_text().encode('UTF-8'), item.find('a').get_text()
                infoJson[item.find('b').get_text().encode('UTF-8')] = item.find('a').get_text()
                continue

            if item.find('b').get_text().encode('UTF-8').replace('\n', '').replace(' ', '') in keys:
                # print item.find('b').get_text().encode('UTF-8').replace('\n', '').replace(' ', ''), item.find('b').next_sibling.replace('\n', '').replace(' ', '')
                infoJson[item.find('b').get_text().encode('UTF-8').replace('\n', '').replace(' ', '')] = item.find('b').next_sibling.replace('\n', '').replace(' ', '')

        return json.dumps(infoJson)
