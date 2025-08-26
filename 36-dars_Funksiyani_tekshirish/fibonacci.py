#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 02:10:39 2025

@author: islomisomiddinov
"""

def fibonacci(son):
    sonlar = []
    for x in range(son):
        if x==0 or x==1:
            sonlar.append(1)
        else:
            sonlar.append(sonlar[x-1] + sonlar[x-2])
    print(sonlar)
    return son in sonlar
    
# print(fibonacci(5))
    
    
    
    
    
    
    
    
# def fibonachchi(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x-1] + sonlar[x-2])
#     return sonlar
    
# print(fibonachchi(7))