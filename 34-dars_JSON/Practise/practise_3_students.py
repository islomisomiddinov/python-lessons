#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 01:52:49 2025

@author: islomisomiddinov
"""

import json

with open('students.json') as f:
    data = json.load(f)
    
print(data)