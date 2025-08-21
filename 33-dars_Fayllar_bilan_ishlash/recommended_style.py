#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 19:43:37 2025

@author: islomisomiddinov
"""

import pickle

shaxs1 = {'ism':'qudrat', 'familiya':'toirov', 'tyil':1996, 'passport':'AB3330022', 'manzil':'samarqand'}

with open('recom', 'wb') as file:
    pickle.dump(shaxs1, file)
    
with open('recom', 'rb') as file:
    shaxs1 = pickle.load(file)
    
print(shaxs1)