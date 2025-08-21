#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 22 01:16:16 2025

@author: islomisomiddinov
"""

import json

talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""

talaba = json.loads(talaba_json)
# print(f"{talaba['ism']} {talaba['familiya']}")

with open('student.json', 'w') as f:
    json.dump(talaba, f)
    