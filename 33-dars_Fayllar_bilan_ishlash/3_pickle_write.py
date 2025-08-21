#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 19:30:56 2025

@author: islomisomiddinov
"""

import pickle

talaba1 = {'ism':'davron', 'familiya':'usmonov', 'tyil':2002, 'kurs':3}
talaba2 = {'ism':'fazliddin', 'familiya':'ergashev', 'tyil':2006, 'kurs':1}

with open('info.pkl', 'wb') as file:
    pickle.dump(talaba1, file)
    pickle.dump(talaba2, file)