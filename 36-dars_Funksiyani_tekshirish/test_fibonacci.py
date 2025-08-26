#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 02:59:24 2025

@author: islomisomiddinov
"""

import unittest
from fibonacci import fibonacci

class FibonacciTest(unittest.TestCase):
    def test_true_fibo(self):
        self.assertTrue(fibonacci(5))
        self.assertTrue(fibonacci(13))
        
    def test_false_fibo(self):
        self.assertFalse(fibonacci(14))
        self.assertFalse(fibonacci(20))
        

unittest.main()