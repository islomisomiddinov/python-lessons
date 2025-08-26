#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 10:17:56 2025

@author: islomisomiddinov
"""

import unittest

from name import get_full_name

class NameTest(unittest.TestCase):
    def test_toliq_ism(self):
        name = get_full_name('umar', 'erkinov')
        self.assertEqual(name, 'Umar Erkinov')
        
        
unittest.main()