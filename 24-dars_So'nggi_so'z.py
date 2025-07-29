#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 14:52:28 2025

@author: islomisomiddinov
"""

# 24-dars:    FUNKSIYALAR - SO'NGGI SO'Z


# import math

# def nom(argument):  # Nomli funksiyaning ko'rinishi
#     return ifoda



#   #    lambda - Nomsiz funksiyalarning ko'rinishi:
    
    
    
# lambda argument: ifoda  

# lambda argument1, argument2: ifoda = argument1 + argument2


# uzunlik = lambda pi, radius: 2*pi*radius
# print(uzunlik(math.pi,10))


# kvadrat = lambda x, y : x**y
# print(kvadrat(3, 2))


# def daraja(n):
#     return lambda x : x**n

# kvadrat = daraja(2)
# kub = daraja(3)
# print(f"3 ning kvadrati {kvadrat(3)} ga, "
#       f"kubi {kub(3)} ga teng.")



#   #   map() funksiyasi


# from math import sqrt  # sqrt - kvadrat ildiz hisoblaydi

# sonlar = list(range(11)) 
# ildizlar = list(map(sqrt, sonlar))
# print(ildizlar)


# def daraja2(x):
#     """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x*x

# print(list(map(daraja2, sonlar)))


# kvadratlar = list(map(lambda x: x*x, sonlar))
# print(kvadratlar)


# a = [4, 5, 6]
# b = [7, 8, 9]
# a_plus_b = list(map(lambda x,y: x+y, a, b))
# # print(a_plus_b)


# ismlar = ['akbar', 'yulduz', 'qodir', 'javlon']
# print(list(map(lambda matn: matn.title(), ismlar)))




#   #   filter funksiyasi



import random as r

sonlar = r.sample(range(100),10)  # 0-100 oraliqda 10 ta tasodifiy sonlar
# print(sonlar)

def juftmi(x):
    """x juft bo'lsa True, aks holda False qaytaruvchi funksiya"""
    return x%2==0

# juft_sonlar = list(filter(juftmi, sonlar))
# print(juft_sonlar)

juft_sonlar = list(filter(lambda son: son%2==0, sonlar))
# print(juft_sonlar)



#   #   filter funksiyasini matnlar bilan birga qo'llash


mevalar = ['anor', 'uzum', 'shaftoli', 'behi', 'banan', 'olma', 'tarvuz']
harf = 'b'
mevalar_b = list(filter(lambda meva:meva.startswith(harf), mevalar))
# print(mevalar_b)

mevalar2 = list(filter(lambda meva:len(meva)<=5, mevalar))
# print(mevalar2)



#   #   #   HOMEWORK    #   #   #


a_r = list(filter(lambda meva:(meva.startswith('a') and meva.endswith('r')),
                                                                  mevalar))
# print(a_r)




#   #   Toq sonlar ro'yhati

from random import sample
from math import sqrt

x = list(range(0, 1001))
y = sample(x, k=10)
# print(y)

ildizlar = list(map(lambda n: sqrt(n), y))
# print(ildizlar)

toq_sonlar = list(filter(lambda n: n % 2, y))
# print(toq_sonlar)



##  Tub sonlar ro'yhati

def tubmi(x):
    if x % 2 == 0 or x < 2:
        return False  # Son juft yoki 2 dan kichik bo'lsa
    elif x == 2 or x == 3:
        return True  # Son 2 yoki 3 bo'lsa
    for i in range(3, x, 2):
        if x % i == 0:
            return False
    return True

tub_sonlar = list(filter(tubmi, range(100)))
# print(tub_sonlar)


f1 = lambda x: x * 10
# print(f1(10))


f2 = lambda x, y: x * y
# print(f2(5, 4))