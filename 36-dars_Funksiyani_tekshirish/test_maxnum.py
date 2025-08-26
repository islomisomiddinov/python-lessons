#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 00:59:15 2025

@author: islomisomiddinov
"""

import unittest
from max_nums import eng_kattasi

class MaxNumTest(unittest.TestCase):
    def test_max_num(self):
        self.assertEqual(eng_kattasi(3,56,-61), 56)
        
unittest.main()