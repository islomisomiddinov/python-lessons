#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 18:00:53 2025

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
    

# inson = Shaxs('Nigora', "Fozilova", "AD2344567", 2004)


class Talaba(Shaxs):
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        self.manzil = manzil
        
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
        
    
    
class Manzil:
    def __init__(self, uy, kocha, tuman, viloyat):
        self.uy = uy
        self.kocha = kocha
        self.tuman = tuman
        self.viloyat = viloyat
        
    def get_manzil(self):
        manzil = f"{self.viloyat} viloyati, {self.tuman} tumani, "
        manzil += f"{self.kocha} ko'chasi {self.uy}-uy"
        return manzil

    
    
talaba1_manzil = Manzil(7, "Mevazor", "Olmazor", "Toshkent")
talaba1 = Talaba("Leyla", "Erkinova", "AB3334455", 2000, "N0007771", talaba1_manzil)




