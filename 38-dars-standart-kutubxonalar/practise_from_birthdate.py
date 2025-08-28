#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 10:54:44 2025

@author: islomisomiddinov
"""

import datetime as dt


def count_days(b_year, b_month, b_day):
    """Tug'ilganimdan bugungacha yashagan kunlarim soni"""
    bugun = dt.date.today()
    bdate = dt.date(b_year, b_month, b_day)
    
    # Avval taxminiy farqni olish
    years = bugun.year - bdate.year
    months = bugun.month - bdate.month
    days = bugun.day - bdate.day

    # Kun manfiy bo‘lsa -> oldingi oydan qarz olish
    if days < 0:
        months -= 1
        # oldingi oy oxiri
        from calendar import monthrange
        prev_month = bugun.month - 1 or 12
        prev_year = bugun.year if bugun.month > 1 else bugun.year - 1
        days += monthrange(prev_year, prev_month)[1]

    # Oy manfiy bo‘lsa -> oldingi yildan qarz olish
    if months < 0:
        years -= 1
        months += 12

    return years, months, days

y, m, d = count_days(1996, 8, 12)
print(f"Tug'ilganimga {y} yilu, {m} oy {d} kun bo'ldi")