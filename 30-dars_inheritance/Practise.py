#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 19:18:16 2025

@author: islomisomiddinov
"""

class Shaxs:
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil
        
    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport: {self.passport}, {self.tyil}-yilda tug'ilgan."
        return info
    
    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi funksiya"""
        return yil - self.tyil
    

inson = Shaxs('Nigora', "Fozilova", "AD2344567", 2004)


class Talaba(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil, fanlar):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        self.fanlar = []
        
    def get_id(self):
        """Talabaning ID raqamini qaytaradi"""
        return self.idraqam
    
    def get_bosqich(self):
        """Talaba nechinchi kursda o'qishi"""
        return self.bosqich
        
    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.bosqich}-bosqich talabasi, ID-raqami: {self.idraqam}"
        return info
    

class Fan:
    def __init__(self, nomi):
        self.nomi = nomi
        self.muddati = 1
        
geograf = Fan('Geografiya')
history = Fan("Tarix")
english = Fan("Ingliz tili")