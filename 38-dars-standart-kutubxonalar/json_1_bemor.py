#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 00:35:21 2025

@author: islomisomiddinov
"""

import json

bemor = {
    'ism':'Salim Fozilov',
    'yosh':29,
    'oila':True,
    'farzandlari':('Javlon', 'Leyla'),
    'allergiya':None,
    'dorilar':[
        {'nomi':'sefazalin', 'doza':0.5},
        {'nomi':'natriy xlor', 'doza':200}
    ]
}

bemor_json = json.dumps(bemor, indent=4)
# print(bemor_json)

with open('bemor.json', 'w') as f:
    json.dump(bemor, f)

sonlar = (34, 77, 100, 21)    
with open('sonlar.json', 'w') as f:
    json.dump(sonlar, f)
    
bemor2 = json.loads(bemor_json)

with open('bemor.json') as f:
    bemor = json.load(f)
    
# print(type(bemor))