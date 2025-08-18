#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 18 17:56:04 2025

@author: islomisomiddinov
"""

from uuid import uuid4
class Avto:
    """Avtomobil klassi"""
    __num_avto = 0
    def __init__(self, make, model, rang, yil, narx, km=0):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1
        
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto
    
    def get_km(self):
        return self.__km
    
    def get_id(self):
        return self.__id
    
    def add_km(self, km):
        """Mashinaning km ga yana km qo'shish"""
        if km >= 0:
            self.__km += km
        else:
            print("Mashina km kamaytirib bo'lmaydi!")
        
# avto1 = Avto('GM', 'Malibu', 'qora', 2025, 40000)
# print(f"ID : {avto1.get_id()}")
# avto1.add_km(500)
# print(avto1.get_km())

# avto1 = Avto('GM', 'Malibu', 'qora', 2025, 40000)
# avto2 = Avto('GM', 'Cobalt', 'oq', 2024, 14000)
# avto3 = Avto('Kia', 'Sportsage', 'blue', 2025, 45000)
# print(Avto.get_num_avto())

class Bus:
    pass

class Train:
    pass