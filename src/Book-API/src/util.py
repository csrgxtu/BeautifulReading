#!/usr/bin/env python
#
# Author: Archer Reilly
# Date: 13/Sep/2015
# File: util.py
# Desc: utilities
#
# Produced By BR(BeautifulReading)
import json

def ldUserAgents(fileName):
    tmpBuf = ''
    with open(fileName, 'r') as f:
        tmpBuf = f.read()

    return json.loads(tmpBuf)['brower']
