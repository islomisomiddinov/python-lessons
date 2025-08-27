#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 03:31:08 2025

@author: islomisomiddinov
"""

import unittest
from car import Car

class CarTest(unittest.TestCase):
    """Car klassini tekshirish uchun test"""
    def setUp(self):
        make = "Chevrolet"
        self.model = "Malibu"
        year = 2025
        self.price = 40000
        self.km = 1500
        self.avto1 = Car(make, self.model, year)
        self.avto2 = Car(make, self.model, year, price=self.price)
        
    def test_create(self):
        # Qiymatlar mavjudligini assertIsNotNone metodi bilan tekshirish
        self.assertIsNotNone(self.avto1.make)
        self.assertIsNotNone(self.avto1.model)
        self.assertEqual(self.model, self.avto1.model)
        self.assertIsNotNone(self.avto1.year)
        # Qiymat mavjud emasligini assertIsNone metodi orqali tekshiramiz
        self.assertIsNone(self.avto1.price)
        # Qiymat tengligini assertEqual metodi bilan tekshiramiz
        self.assertEqual(0, self.avto1.get_km())
        # avto2 narxini tekshiramiz
        self.assertEqual(self.price, self.avto2.price)
        
    def test_set_price(self):
        new_price = 45000
        self.avto2.set_price(new_price)
        self.assertEqual(new_price, self.avto2.price)
        
    def test_add_km(self):
        #1 Musbat qiymat berib ko'ramiz
        self.avto1.add_km(self.km)
        self.assertEqual(self.km, self.avto1.get_km())
        self.avto1.add_km(3000)
        self.assertEqual(4500, self.avto1.get_km())
        #2 Musbat qiymat berib ko'ramiz
        new_km = -500
        try:
            self.avto1.add_km(new_km)
        except ValueError as error:
            self.assertEqual(type(error), ValueError)
            
    def test_get_info(self):
        avto1_info = "CHEVROLET Malibu. 2025-yil, 0km yurgan."
        self.assertEqual(avto1_info, self.avto1.get_info())
        # avto1 narxi va km o'zgartiramiz
        self.avto1.set_price(44000)
        self.avto1.add_km(500)
        avto1_info = "CHEVROLET Malibu. 2025-yil, 500km yurgan.Narxi 44000"
        self.assertEqual(avto1_info, self.avto1.get_info())
         
unittest.main()