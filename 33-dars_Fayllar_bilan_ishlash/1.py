#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 22:12:27 2025

@author: islomisomiddinov
"""

    # TAVSIYA ETILMAYDIGAN USUL


file = open('pi.txt')
PI = file.read()
print(PI)
file.close()

    # RECOMMENDED


with open('pi.txt') as file:
    pi = file.read()
    
print(pi)

pi = pi.rstrip()
pi = pi.replace("\n", '')
pi = float(pi)
print(pi)


        # FAYL ICHIDAGI QATORLARNI ALOHIDA O'QISH

filename = 'data/talabalar.txt'
with open(filename) as file:
    for line in file:
        print(line)
        
        
        # readline() METODI QATORLARNI RO'YXATGA YUKLASH
        
with open(filename) as file:
    talabalar = file.readlines()
    
print(talabalar)

talabalar = [talaba.rstrip() for talaba in talabalar]
print(talabalar)