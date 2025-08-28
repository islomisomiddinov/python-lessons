#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 05:42:00 2025

@author: islomisomiddinov
"""

import datetime as dt

        # datetime()
hozir = dt.datetime.now()
print(hozir)
        # sanani ajratib olish
print(hozir.date()) 
        # vaqtni ajratib olish
print(hozir.time())
        # soatni ajratib olish
print(hozir.hour)
        # minutni ajratib olish
print(hozir.minute)
        # sekundni ajratib olish
print(hozir.second)


        # date()
bugun = dt.date.today()
print(f"Bugungi sana:{bugun}")
ertaga = dt.date(2025, 8, 28)
print(f"Ertangi sana:{ertaga}")


        # time()
hozir = dt.datetime.now()
vaqtHozir = hozir.time()
print(f"Hozirgi soat: {vaqtHozir}")
vaqtKeyin = dt.time(23, 45, 30)
print(vaqtKeyin)


        # Sanalar orasidagi farq
bugun = dt.date.today()
ramazon = dt.date(2026, 2, 18)
farq = ramazon - bugun
print(farq)
print(f"Ramazonga {farq.days} kun qoldi!")


        # Soatlar orasidagi farq
hozir = dt.datetime.now()
futbol = dt.datetime(2025, 8, 31, 18, 30, 00)
farq = futbol - hozir
sekundlar = farq.seconds
minutlar = int(sekundlar/60)
soatlar = int(minutlar/60)
print(f"Match boshlanishiga {farq.days} kunu {soatlar} soat qoldi.")

        # sana va vaqtni o'zimizga qulay formatda chiqaramiz
vaqt = hozir.strftime("%H:%M:%S")
print(f"Hozir soat: {vaqt}")
sana = hozir.strftime("%d.%m.%Y")
print(f"Bugun sana: {sana}")
