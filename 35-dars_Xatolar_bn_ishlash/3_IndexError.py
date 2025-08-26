#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 15:18:21 2025

@author: islomisomiddinov
"""

mevalar = ['olma', 'uzum', 'anjir', 'tarvuz', 'gilos']
try:
    print(mevalar[9])
except IndexError:
    print(f"Ro'yxatda {len(mevalar)} ta meva bor.")