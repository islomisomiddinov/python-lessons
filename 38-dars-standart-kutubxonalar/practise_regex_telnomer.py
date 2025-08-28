#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 11:46:54 2025

@author: islomisomiddinov
"""
import re

andoza = "^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"
nomer = input("Telefon raqamingizni kiriting: ")
if re.match(andoza, nomer):
    print(f"Tabriklaymiz! {nomer} telefon raqamingiz muvaffaqiyatli saqlandi.")
else:
    print("Bu telefon raqami mavjud emas!")