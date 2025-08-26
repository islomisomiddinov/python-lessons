#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 02:05:25 2025

@author: islomisomiddinov
"""

import unittest
from juft_sonlar import juftSonlar

class JuftSonTest(unittest.TestCase):
    def test_juft(self):
        self.assertEqual(
            juftSonlar([23, 56, 7, -34, 129, 562]),
            [56, -34, 562]
            )
        
unittest.main()