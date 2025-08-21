#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 21:43:00 2025

@author: islomisomiddinov
"""

import pickle

with open('amaliyot/pi_million_digits.txt') as file:
    pi = file.read()
    
pi = pi.rstrip()    # qator oxiridagi boshliqlarni olib tashlash uchun
pi = pi.replace("\n", "")   # qator tashlash belgisini almashtiramiz
pi = pi.replace(" ", "")

# print(pi)

        # TUG'ILGAN KUNIM PI DA BORMI
bdate = '12081996'
# print(bdate in pi)

pi = float(pi)  # matnni float o'nlik songa o'tkazamiz
print(pi)

with open('amaliyot/new_pi_float.dat', 'wb') as file:
    pickle.dump(pi, file)
    
with open('amaliyot/new_pi_float.dat', 'rb') as file:
    pi = pickle.load(file)
print(pi)


