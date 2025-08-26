#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 01:26:02 2025

@author: islomisomiddinov
"""

import unittest
from head_letter import head_letter

class headletterTest(unittest.TestCase):
    def test_head_letter(self):
        self.assertEqual(
            head_letter(['olma', 'anjir', 'uzum', 'shaftoli', 'gilos']),
            ['Olma', 'Anjir', 'Uzum', 'Shaftoli', 'Gilos']
            )
        
unittest.main()