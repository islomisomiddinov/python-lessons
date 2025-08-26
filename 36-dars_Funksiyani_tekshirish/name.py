#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 17:39:19 2025

@author: islomisomiddinov
"""

def get_full_name(ism, familiya, otasi):
    return f"{ism} {otasi} {familiya}".title()

# def get_full_name(ism, familiya, otasi =''):
#     if otasi:
#         return f"{ism} {otasi} {familiya}".title()
#     else:
#         return f"{ism} {familiya}".title()