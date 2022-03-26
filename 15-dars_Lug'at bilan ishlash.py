# 13.12.2021
# 15-dars Lug'at bilan ishlash

talaba_0 = {
    'ism':'alijon',
    'familiya':'shamshiyev',
    'yosh':22,
    'kurs':4,
    'fakultet':'matematika'
    }



#   #   .items()    #   #


# print(talaba_0.items())

# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat}\n")
    
telefonlar = {
    'ali':'iphone 12',
    'nodir':'redmi 10',
    'zokir':'galaxy S21',
    'rustam':'huawei p30'
    }
# for k, q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}\n")
    


#   #   .keys()     #   #

mahsulotlar = {
    'olma':9000,
    'uzum':5000,
    'shaftoli':27000,
    'banan':23000,
    'mandarin':16000
    }
# print(mahsulotlar.keys())

# print("Do'konimizdagi mahsulotlar:")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())

# print("Do'kondagi mahsulotlar:")
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())

bozorlik = ['olma', 'mandarin', 'non', 'baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()}ning narxi {mahsulotlar[mahsulot]} so'm.")

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling.")



#   #   LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH

# print("Do'konimizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())



#   #   .values()

# print(telefonlar.values())

# print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
# for tel in telefonlar.values():
#     print(tel)


#   #   set

telefonlar = {
    'abror':'galaxy note21',
    'doni':'redmi 10',
    'bobur':'samsung a5',
    'rustam':'iphone 13',
    'qodir':'huawei p40',
    'olim':'nokia 3310',
    'polvon':'iphone 13',
    'toxir':'redmi 10',
    'erkin':'redmi 10',
    'ergash':'asus'
    }
# print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
# for tel in telefonlar.values():
#     print(tel)

#   #   set
# print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi:")
# for tel in set(telefonlar.values()):
#     print(tel)
    
toys = {'ball', 'lamp', 'car', 'ball', 'teddy', 'car'}
# print(type(toys))
# print(toys)
# print(sorted(toys))



#   #   #   HOMEWORK    #   #   #


##  Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing.
##  Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.

python_izohli = {
    'set':"takrorlangan so'zlarni olib tashlovchi ma'lumot turi",
    'get':"lug'atdan kalit so'zga mos keluvchi qiymatni olib chiqaradi",
    'insert':"ro'yhatga indeksi bo'yicha element qo'shadi",
    'dictionary':"lug'at",
    'values':"lug'atdagi kalitning qiymatini qaytaradi",
    'pop':"ro'yhatda turgan oxirgi elementni sug'urib oladi",
    'indeks':"element turgan joyning raqami",
    'upper':"matndagi barcha so'zlarni katta harfga aylantiradi",
    'capitalize':"matnning faqat birinchi harfini katta harfga o'zgartiradi",
    'tuple':"o'zgarmas ro'yhat turi",
    'items':"lug'at elementlarini kalit-qiymat shaklida qaytaradi"
    } 
# for k, v in sorted(python_izohli.items()):
#     print(f"{k.title()} - {v}")


##  Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni,
##  keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring.

davlat_poytaxt = {
    'spain':'madrid',
    'uzbekistan':'tashkent',
    'russia':'moscow',
    'oman':'mascat',
    'jordan':'ierusalem',
    'germany':'berlin',
    'canada':'ottawa',
    'france':'paris',
    'austria':'vienna'
    }
# print("Dunyo davlatlari:")
# for kalit in sorted(davlat_poytaxt):
#     print(f"{kalit.upper()}")

# print("Dunyo shaharlari")
# for qiymat in sorted(davlat_poytaxt.values()):
#     print(f"{qiymat.title()}")
    

##  Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring.
##  Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.

# davlat = input("Qaysi davlatning poytaxtini bilishni istaysiz? > ")
# if davlat.lower() in davlat_poytaxt:
#     print(f"{davlat.upper()}ning poytaxti {davlat_poytaxt[davlat].title()} shahri")
# else: print("Bizda bu davlat haqida ma'lumot yo'q.")

# davlat = input("Qaysi davlatning poytaxtini bilishni istaysiz? > ").lower()
# poytaxt = davlat_poytaxt.get(davlat)
# if poytaxt == None: print("Bizda bu davlat haqida ma'lumot yo'q.")
# else: 
#     print(f"{davlat.upper()}ning poytaxti {poytaxt.title()} shahri")


##  Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan
##  3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring,
##  agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.

menu = {
        'non':3000,
        'choy':2000,
        'salat':5000,
        'shirinlik':8000,
        'osh':12000,
        'norin':15000,
        'muzqaymoq':4000,
        'shashlik':11000,
        'qozonkabob':17000,
        'tabaka':14000
        }
# print("Iltimos, 3 ta taomga buyurtma bering:")
# buyurtmalar = []
# for n in range(3):
#     buyurtmalar.append(input(f"{n+1}-ovqat: ").lower())

# for buyurtma in buyurtmalar:
#     if buyurtma in menu:
#         print(f"{buyurtma.title()} - {menu[buyurtma]} so'm.")
#     else: print(f"Kechirasiz, bizda {buyurtma} yo'q.")