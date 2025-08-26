#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 23:44:29 2025

@author: islomisomiddinov
"""

import unittest
from tubsonmi import tubSonmi

class tubSonTest(unittest.TestCase):
    def test_true(self):
        self.assertTrue(tubSonmi(7))
        self.assertTrue(tubSonmi(193))
    
    def test_false(self):
        self.assertFalse(tubSonmi(4))
        self.assertFalse(tubSonmi(265))
        
unittest.main()