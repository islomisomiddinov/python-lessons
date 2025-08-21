#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 19:41:32 2025

@author: islomisomiddinov
"""

import pickle

with open('info.pkl', 'rb') as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)
    
print(talaba1)
print(talaba2)
