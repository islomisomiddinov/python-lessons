#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 21 22:11:01 2025

@author: islomisomiddinov
"""

while True:
    book = input("Yoqtirgan kinolaringiz nomini yozing, to'xtash uchun Enter tugmasini bosing:")
    if not book:
        break
    with open('kino', 'a') as file:
        file.write(book +'\n')
        
with open('kino', 'r') as file:
    books = file.readlines()
books = [book.rstrip() for book in books]
print(books)