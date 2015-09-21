#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 21/Sep/2015
# File: ASINParser.py
# Desc: parse asin from the html
#
# Produced By BR(BeautifulReading)
from bs4 import BeautifulSoup

class ASINParser(object):
    HTML = None

    def __init__(self, html):
        self.HTML = html

    def getAsin(self):
        soup = BeautifulSoup(self.HTML, "lxml")

        element = soup.find('a', class_ = 'a-link-normal a-text-normal')
        if not element:
            return False

        return element['href'].split('/')[-1]
