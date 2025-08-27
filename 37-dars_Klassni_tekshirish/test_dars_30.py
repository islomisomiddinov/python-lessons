#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 05:03:15 2025

@author: islomisomiddinov
"""

import unittest
from dars_30_shaxs import Shaxs, Talaba

class ClassesTest(unittest.TestCase):
    def setUp(self):
        self.shaxs1 = Shaxs("nigora", 'fozilova', 'AD2344567', 2004)
        self.talaba1 = Talaba("leyla", 'erkinova', 'AB3334455', 2000, 'N0007771')
        
    def test_isinstance(self):
        self.assertIsInstance(self.shaxs1, Shaxs)
        self.assertIsInstance(self.talaba1, Talaba)
        self.assertIsInstance(self.talaba1, Shaxs)
    
    def test_get_info(self):
        self.assertEqual(
            self.shaxs1.get_info(),
            "Nigora Fozilova. Passport: AD2344567, 2004-yilda tug'ilgan."
            )
        
    def test_get_age(self):
        self.assertEqual(self.shaxs1.get_age(2025), 21)
        self.assertEqual(self.talaba1.get_age(2025), 25)
        
    def test_talaba_methods(self):
        self.assertEqual(self.talaba1.get_id(), "N0007771")
        self.assertEqual(self.talaba1.get_bosqich(), 1)
        self.assertEqual(
            self.talaba1.get_info(), 
            "Leyla Erkinova. 1-bosqich talabasi, ID-raqami: N0007771"
            )
        
unittest.main()