#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 27 18:31:52 2025

@author: islomisomiddinov
"""

import re
from uzwords import words

word1 = "томир"
word2 = "темир"
word3 = "тулпор"

andoza = "^т...р$"

# print(re.match(andoza, word1))
# print(re.match(andoza, word2))
# print(re.match(andoza, word3))


andoza = "^т...р$"
matches = []
for word in words:
    if re.match(andoza, word):
        matches.append(word)
        
# print(matches)f


        # Emailni ajratib olish
matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """

andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
email = re.findall(andoza,matn)
# print(email)


        # kuchli parolni tekshirish
andoza = '^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
msg = "Yangi parol kiriting"
msg += " (kamida 8 ta belgidan iborat, kamida 1 ta lotin bosh harfi, kamida 1 ta kichik harf, "
msg += "1 ta son va 1 ta maxsus bekgi bo'lishi kerak): "

while True:
    password = input(msg)
    if re.match(andoza, password):
        print("Yangi parol qabul qilindi!")
        break
    else:
        print("Parol talabga javob bermadi, boshqa parol kiriting.")
        
        
        
        
        
        