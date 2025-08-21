#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  1 17:57:46 2025

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
    def __init__(self, ism, familiya, passport, tyil, idraqam):
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam = idraqam
        self.bosqich = 1
        
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
        
talaba1 = Talaba("Leyla", "Erkinova", "AB3334455", 2000, "N0007771")


