#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 22:49:32 2025

@author: islomisomiddinov
"""

import json

x = 10
x_json = json.dumps(x)

y = 5.5
y_json = json.dumps(y)

m = True
m_json = json.dumps(m)

sonlar = (12, 45, 77, 20)
sonlar_json = json.dumps(sonlar)

numbers = json.loads(sonlar_json)
print(numbers)