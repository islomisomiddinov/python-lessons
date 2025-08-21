#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 12:07:26 2025

@author: islomisomiddinov
"""

class Shaxs:
    def __init__(self, ism, familiya, tyil, passport):
        self.ism = ism
        self.familiya = familiya
        self. tyil = tyil
        self.passport = passport
        
    def __repr__(self):
        return f"Fuqaro: {self.ism.title()} {self.familiya.title()}"
    
    
class Student(Shaxs):
    def __init__(self, ism, familiya, tyil, passport, idraqam, bosqich):
        super().__init__(ism, familiya, tyil, passport)
        self.idraqam = idraqam
        self.bosqich = bosqich
        
    def __repr__(self):
        info = f"Talaba: {self.ism.title()} {self.familiya.title()}\n"
        info += f"{self.idraqam} ID-raqamli talaba {self.bosqich}-kurs"
        return info
    
    def get_kurs(self):
        return self.bosqich
    
    def __eq__(self, y):
        return self.bosqich == y.bosqich
    
    def __ge__(self, y):
        return self.bosqich >= y.bosqich
    
talaba1 = Student('Abror', "turdiyev", 2002, "AD4758294", "N1234567", 3)
talaba2 = Student("sarvar", 'rahimov', 1998, 'AB7770990', 'N9080705', 2)

# print(talaba1.__repr__())
# print(talaba2.__repr__())