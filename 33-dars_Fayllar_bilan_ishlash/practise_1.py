#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 19:54:04 2025

@author: islomisomiddinov
"""

import pickle

dars = "Bugun men fayllar bilan ishlash bo'yicha ko'nikmalarni o'rgandim"

# with open('teach.txt.rtf') as file:
#     dars = file.read()
    
# print(dars)


with open('write', 'wb') as file:
    pickle.dump(dars, file)
    
with open('write', 'rb') as file:
    dars = pickle.load(file)
    
# print(dars)