#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 26 23:19:44 2025

@author: islomisomiddinov
"""

import unittest
from circle import getArea, getPerimeter

class Circletest(unittest.TestCase):
    def test_area(self):
        self.assertAlmosrEqual(getArea(4), 50.26544)
        # self.assertAlmostEqual(getArea(8), 201.06176)
        
unittest.main()