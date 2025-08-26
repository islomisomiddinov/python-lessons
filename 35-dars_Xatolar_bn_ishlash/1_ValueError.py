#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 11:28:09 2025

@author: islomisomiddinov
"""

yosh = input("Yoshingizni kiriting: ")
    
try:
    yosh = int(yosh)
except ValueError:
    print("Siz butun son kiritmadingiz!")
else:
    print(f"Siz {2025-yosh} yilda tug'ilgan ekansiz")
    
print("Dastur davom etayapti!")