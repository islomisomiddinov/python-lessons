#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 17:24:15 2025

@author: islomisomiddinov
"""

n = input("Butun son kiriting: ")

try:
    n = int(n)
    x=20/n
except ValueError:      # agar butun son kiritilmasa...
    print("Siz butun son kiritmadingiz.")
except ZeroDivisionError:   # agar foydalanuvchi 0 soni kiritsa...
    print("0 ga bo'lish mumkin emas")
else:
    print(f"x={int(x)}")
    