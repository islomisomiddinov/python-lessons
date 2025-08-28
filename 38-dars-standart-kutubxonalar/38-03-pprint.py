#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 17:42:33 2025

@author: islomisomiddinov
"""

from pprint import pprint
import json

filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)
    
# pprint(bemor)

import requests
r = requests.get('https://api.github.com')

# pprint(r.json())