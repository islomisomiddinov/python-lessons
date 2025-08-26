#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 01:46:34 2025

@author: islomisomiddinov
"""

def juftSonlar(sonlar):
    juft_sonlar = [son for son in sonlar if son%2==0]
    return juft_sonlar

# result = juftSonlar([34, 89, -78, 96])
# print(result)