#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 16:41:10 2025

@author: islomisomiddinov
"""

        # FAYL USTIDA TURLI AMALLAR

import json

files = ["""python-darslari/35-dars_Xatolar_bn_ishlash/talaba1.json""", 
"""python-darslari/35-dars_Xatolar_bn_ishlash/talaba2.json""", 
"""python-darslari/35-dars_Xatolar_bn_ishlash/talaba3.json""", 
"""python-darslari/35-dars_Xatolar_bn_ishlash/talaba4.json"""]

for filename in files:
    try:
        with open(filename) as f:
            talaba = json.load(f)
    except FileNotFoundError:
        print(f"{filename} mavjud emas.")
    else:
        print(talaba["ism"])
        
        
        # OR
        
        
for filename in files:
    try:
        with open(filename) as f:
            talaba = json.load(f)
    except FileNotFoundError:
        pass
    else:
        print(talaba["ism"])