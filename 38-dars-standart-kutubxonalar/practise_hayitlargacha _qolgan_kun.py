#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 10:34:39 2025

@author: islomisomiddinov
"""

import datetime as dt

bugun = dt.date.today()
print(f"Bugun sana: {bugun}")

ramazon_hayit = dt.date(2026,3,20)
qurbon_hayit = dt.date(2026,5,27)

farq_ramazonga = ramazon_hayit - bugun
farq_qurbonga = qurbon_hayit - bugun

print(f"Ramazon hayitigacha {farq_ramazonga.days} kun qoldi.")
print(f"Qurbon hayitigacha {farq_qurbonga.days} kun qoldi.")