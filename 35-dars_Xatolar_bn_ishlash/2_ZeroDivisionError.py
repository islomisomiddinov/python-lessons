#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 14:15:15 2025

@author: islomisomiddinov
"""

x,y = 5,10
try:
    y/(x-5)
except ZeroDivisionError:
    print("0 ga bo'lish mumkin emas!")
    