#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 14:39:35 2025

@author: islomisomiddinov
"""

class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        
    def get_name(self):
        return self.ism
    
    def get_lastname(self):
        return self.familiya
    
    def get_age(self, yil):
        return yil - self.tyil
        
    def tanishtir(self):
        return f"Ismim {self.ism} {self.familiya}, tug'ilgan yilim {self.tyil}"
        
        
talaba1 = Talaba('Ravshan', 'Umarov', 2000)
talaba2 = Talaba('Fozil', 'Saidov', 2003)
talaba3 = Talaba('Sarvar', 'Yusupov', 1997)
    

        # AMALIYOT
        
        
class User:
    def __init__(self, ism, login, email, tel_raqam):
        self.ism = ism
        self.login = login
        self.email = email
        self.tel_raqam = tel_raqam
        
    def get_info(self):
        return f"Foydalanuvchi logini: {self.login}, ismi: {self.ism}, \
email: {self.email}, telefon raqami: {self.tel_raqam}"

user1 = User('Komil Jumayev', 'komil_uzbek', 'komiluser@gmail.com', 909999997)