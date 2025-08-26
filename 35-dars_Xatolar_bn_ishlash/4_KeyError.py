#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 15:21:19 2025

@author: islomisomiddinov
"""

user = {
        'username':'devdas',
        'status':'foydalanuvchi',
        'email':'devdas2000@mail.ru',
        'phone':'909994477'}


key = 'tel'
try:
    print(f"Foydalanuvchi: {user[key]}")
except KeyError:
    print("Bunday kalit mavjud emas")