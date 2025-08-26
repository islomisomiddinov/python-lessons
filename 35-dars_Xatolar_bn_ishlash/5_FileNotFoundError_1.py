#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 16:28:46 2025

@author: islomisomiddinov
"""

filename = 'data.txt'   # bunday fayl hozir menda yo'q
try:
    with open(filename) as f:
        text = f.read()
except FileNotFoundError:
    print(f"{filename} nomli fayl topilmadi.")