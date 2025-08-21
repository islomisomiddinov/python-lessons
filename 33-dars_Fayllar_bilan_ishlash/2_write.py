#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 19:21:10 2025

@author: islomisomiddinov
"""

faylnomi = 'new_file.txt'


    # FAYLGA YANGI MA'LUMOT YOZISH

ism = 'Polvon Musayev'
tyil = 1998
with open(faylnomi, 'w') as fayl:
    fayl.write(ism+'\n')  
    fayl.write(str(tyil)+'\n')



    # FAYLGA MA'LUMOT QO'SHISH USULI

with open(faylnomi, 'a') as fayl:
    fayl.write('Komiljon Jurayev\n')
    fayl.write('2001\n')