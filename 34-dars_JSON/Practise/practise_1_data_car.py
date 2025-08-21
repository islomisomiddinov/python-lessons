#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 01:08:59 2025

@author: islomisomiddinov
"""

import json

data = {
        'model':'malibu',
        'rang':'qora',
        'yil':2025,
        'narx':40000
        }

data_json = json.dumps(data, indent=4)
# print(data_json)

with open('car_model.json', 'w') as f:
    json.dump(data, f)