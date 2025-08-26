#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 23:41:16 2025

@author: islomisomiddinov
"""

def tubSonmi(n):
    if n==2 or n==3: return True
    if n%2==0 or n<2: return False
    for i in range(3, int(n**0.5)+1, 2):       # faqat tub sonlarni tekshiramiz
        if n%i==0:
            return False
    return True