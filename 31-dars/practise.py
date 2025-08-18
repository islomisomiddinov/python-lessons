#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 18:48:19 2025

@author: islomisomiddinov
"""

class Shaxs:
    __odamlar_soni = 0
    def __init__(self, ism, familiya, passport, tyil):
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.__tyil = tyil
    
    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"Passport: {self.passport}, {self.tyil}-yilda tug'ilgan."
        return info
    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi funksiya"""
        return yil - self.tyil
    
    def get_tyil(self):
        return self.__tyil
    
    classmethod
    def get_num_people(cls):
        return cls.__odamlar_soni
    

inson = Shaxs('Nigora', "Fozilova", "AD2344567", 2004)
print(Shaxs.get_num_people())


class Talaba(Shaxs):
    __talabalar_soni = 0
    def __init__(self, ism, familiya, passport, tyil, idraqam, telraqam):
        super().__init__(ism, familiya, passport, tyil)
        self.__idraqam = idraqam
        self.__bosqich = 1
        # self.__telraqam = telraqam
        
    def get_id(self):
        """Talabaning ID raqamini qaytaradi"""
        return self.__idraqam
    
    def get_bosqich(self):
        """Talaba nechinchi kursda o'qishi"""
        return self.bosqich
    
    def get_tel(self):
        return self.__telraqam
         
    def get_info(self):
        info = f"{self.ism} {self.familiya}. "
        info += f"{self.bosqich}-bosqich talabasi, ID-raqami: {self.idraqam}"
        return info
    
    # @classmethod
    # def get_num(cls):
    #     return cls.__talabalar_soni
    
        
talaba1 = Talaba("Leyla", "Erkinova", "AB3334455", 2000, "N0007771", 909973434)
# print(talaba1.get_id())
# print(Talaba.get_num())