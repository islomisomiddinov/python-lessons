# 19.12.2021
# 18-dars:    WHILE va RO'YHATLAR

# print("Yaqin do'stlaringiz ro'yhatini tuzamiz!")
# ismlar = []
# n=1     # ismlarni sanash uchun o'zgaruvchi
# while True:
#     savol = f"{n}-do'stingizning ismini kiriting:\n"
#     ism = input(savol)
#     ismlar.append(ism)
#     takrorlash = input("Yana ism qo'shasizmi: (ha/yo'q)? \n")
#     n += 1
#     if takrorlash != 'ha':
#         break
    
# print("\nYaqin do'stlaringiz ro'yhati:\n")
# for ism in ismlar:
#     print(ism.title())


# print("Do'stlaringizning yoshini saqlaydigan dastur!")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingizning ismini kiriting:\n> ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: > ")
#     dostlar[ism] = int(yosh)
#     javob = input("Yana ma'lumot qo'shasizmi (ha/yo'q)?\n> ")
#     if javob != 'ha':
#         ishora = False
    
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda.")


# cars = ['gentra', 'cobalt', 'captiva','spark', 'cobalt', 'orlando', 'tahoe', 'cobalt', 'spark']
# while 'cobalt' in cars:
#     cars.remove('cobalt')
# print(cars)


# cars = ['gentra', 'cobalt', 'captiva','spark', 'cobalt', 'orlando', 'tahoe', 'cobalt', 'spark']
# car = 'cobalt'
# while car in cars:
#     cars.remove(car)
# print(cars)


# talabalar = ['davron', 'hulkar', 'qodir', 'malika','rustam']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi.")
#     baholangan_talabalar[talaba] = int(baho)
    
# for talaba, baho in baholangan_talabalar.items():
#     print(f"\n{talaba.title()}ning bahosi {baho}.")



#   #   #   HOMEWORK    #   #   #



##  Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini
##  birma-bir qabul qilib, yangi ro'yxatga joylang.

# print("Buyurtmalaringiz ro'yhatini tuzamiz.")
# buyurtmalar = []
# n=1
# ishora = True
# while ishora:
#     savol = f"{n}-buyurtmangizni kiriting: "
#     savol += "(Ro'yhat tuzib bo'lgach 'stop' deb yozing)\n> "
#     mahsulot = input(savol)
#     n += 1
#     if mahsulot =='stop':
#         ishora = False
#     else:   buyurtmalar.append(mahsulot)
# print("\nBuyurtmalaringiz ro'yhati:")
# for mahsulot in set(buyurtmalar):
#     print(mahsulot)


##  e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi
##  dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot
##  va uning narhi) kiritishni so'rang.

# print("E-bozor uchun mahsulot-narx dasturi!")
# e_bozor = {}
# while True:
#     mahsulot = input("Mahsulot nomini kiriting: ")
#     narx = input(f"{mahsulot}ning narxini kiriting: ")
#     e_bozor[mahsulot] = float(narx)
#     javob = input("Yana mahsulot kiritasizmi (ha/yo'q) ? >")
#     if javob != 'ha':
#         break
# for mahsulot, narx in e_bozor.items():
#     print(f"E-bozorda {mahsulot.title()}ning narxi {narx} so'm.")


##  Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi
##  har bir mahsulotni e-bozordagi mahsulotlar bilan solishtiring (tayyor
##  ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa
##  mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q"
##  degan xabarni kor'sating.

# buyurtmalar = ['olma','ananas','banan','anor','fanta','pepsi','uzum']
# e_bozor = {
#     'olma':10000,
#     'guruch':11000,
#     'fanta':12000,
#     'sabzi':2500,
#     'uzum':5500
#     }
# while buyurtmalar:
#     buyurtma = buyurtmalar.pop()
#     if buyurtma in e_bozor:
#         print(f"{buyurtma.title()}ning E-bozordagi narxi {e_bozor[buyurtma]} so'm.")
#     else:
#         print(f"E-bozorda {buyurtma.title()} yo'q.")