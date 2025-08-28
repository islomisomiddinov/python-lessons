#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 05:38:50 2025

@author: islomisomiddinov
"""

import datetime as dt

bugun = dt.datetime.today()
# print(bugun.date())

n=0
while n<10:
    print(bugun.strftime("%Y-%m-%d"))
    bugun += dt.timedelta(weeks=2)
    n +=1