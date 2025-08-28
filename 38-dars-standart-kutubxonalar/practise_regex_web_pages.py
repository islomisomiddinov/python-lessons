#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 28 12:01:42 2025

@author: islomisomiddinov
"""

import re


    
web_pages = []
def regex_url(matn):
    """Berilgan matndan veb sahifa manzilini ajratib oluvchi funksiya"""
    andoza = r'https?://[^\s]+'
    result = re.findall(andoza, matn)
    web_pages.append(result)
    # return web_pages
    if web_pages:
        for page in web_pages:
            return page


text = """Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi:
https://youtu.be/vsxJPRLXpgI Ushbu darsimizda unittest moduli yordamida klasslarning
xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. 
Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"""

natija = regex_url(text)
print(natija)