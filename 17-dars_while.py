# 19.12.2021
# 17-dars:    INPUT() va WHILE

##  input()

# ism = input("Ismingiz nima? ")
# savol = (f"Salom {ism.title()}. Yoshingiz nechida? ")
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Bo'yingiz necha metr? ")
# height = float(height)

##  while()

# son = 1     # songa 1 qiymatini beramiz
# while son <= 5:     # toki son 5 dan kichik yoki teng ekan...
#     print(son, end =' ')     # son ni konsolga chiqaramiz
#     son = son + 1 
#     # son += 1    # son ga 1 qo'shamiz
# print('\nDastur tugadi!')


##  while and input

# print("Istalgan sonning kvadratini qaytaruvchi dastur!")
# savol = "Istalgan son kiriting: "
# savol += "\n(dasturni to'xtatish uchun 'exit' deb yozing): >"
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print('\nDastur tugadi!')


##  ishora

# print("Istalgan sonning kvadratini hisoblovchi dastur!")
# savol = "\nIstalgan son kiriting."
# savol += "\n(dasturdan chiqish uchun exit deb yozing.) : >"
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:   print(float(qiymat)**2)
# print("Dastur to'xtadi!")


##  break while

# print("Istalgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting."
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): >>>"
# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break   # siklni to'xtatish
#     else:   print(float(qiymat)**2)
# print('Dastur tugadi!')


##  for sikli uchun break

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng.")


##  for sikli uchun CONTINUE

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng.")


##  while sikli uchun CONTINUE

# son = 0
# while son<10:
#     son += 1
#     if son%2 != False:
#         continue
#     else:
#         print(son)


##  infinite loop (abadiy sikl yaratib qo'yish xatoligi)
##  (Mantiqiy xatolik)

# son = 0
# while son<10:
#     # son += 1    # xatolikka sabab bo'lgan qolib ketgan qator
#     if son%2 != 0:
#         continue
#     else:
#         print(son)


##  Komandalar ketma-ketligidagi xatolik

# son = 0
# while son<10:

#     if son%2 != 0:
#         continue
#     else:
#         print(son)
#     son += 1    # xatolikka sabab bo'lgan joyi noto'g'ri yozilgan qator
    

##  Sikl chegarasini noto'g'ri belgilash

# son = 1
# while son>0:    # xatolikka sabab bo'lgan qolib ketgan qator( son<10 )
#     son += 1
#     if son%2 != 0:
#         continue
#     else:
#         print(son)




#   #   #   HOMEWORK    #   #   #



##  Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang.
##  Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating

# savol = "Yaxshi ko'rgan kitobingizni kiriting!"
# savol += "(dasturni to'xtatish uchun 'stop' deb yozing):\n>>>"
# while True:
#     kitob = input(savol)
#     if  kitob == 'stop':
#         break
# print("Dastur to'xtadi!")


##  Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan
##  yoshlarga - 2000 so'm, 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm,
##  65 dan kattalarga bepul. Shunday while sikl yozingki, dastur
##  foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin.
##  Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin
##  (ikkita shartni ham tekshiring).

# print("Muzeyga kirish uchun chipta narxlari:")
# savol = 'Yoshingiz nechida? '
# savol += "(dastur to'xtashi uchun 'quit' yoki 'exit' deb yozing)\n>>>"

# while True:
#     yosh = input(savol)
#     if yosh=='quit' or yosh=='exit':
#         break
#     yosh = int(yosh)
#     if yosh<=7:
#         narx=2000
#     elif yosh>7 and yosh<=18:
#         narx=3000
#     elif 18<yosh<=65:
#         narx=10000
#     else:
#         narx=0
    
#     if narx==0:
#         print("Sizga chipta bepul!")
#     else:
#         print(f"Siz uchun chipta narxi {narx} so'm.")
# print("Chiptalar qolmadi!")


##  Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora,
##  yoki shart tekshirish)

# print("Muzeyga kirish uchun chipta narxlari:")
# savol = 'Yoshingiz nechida? '
# savol += "(dastur to'xtashi uchun 'quit' yoki 'exit' deb yozing)\n>>>"
# qiymat = ''

# while qiymat != 'quit' or qiymat != 'exit':
#     yosh = input(savol)
#     if yosh=='quit' or yosh=='exit':
#         print("Chiptalar qolmadi!")
#         break
#     else:
#         yosh = int(yosh)
#         if yosh<=7:
#             narx=2000
#         elif yosh>7 and yosh<=18:
#             narx=3000
#         elif 18<yosh<=65:
#             narx=10000
#         else:
#             narx=0
    
#         if narx==0:
#             print("Sizga chipta bepul!")
#         else:
#             print(f"Siz uchun chipta narxi {narx} so'm.")


##  Quyidagi dasturda bir nechta mantiqiy xatolar bor. Jumladan,
##  xususiy holatlarda tsikl abadiy qaytarilib qolmoqda. Xatolarni
##  to'g'rilay olasizmi?

# savol = "Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): \n"

# while True:
#     qiymat = input(savol)
#     if qiymat=='Exit':
#         break
#     elif float(qiymat) <0:
#         print("Siz manfiy son kiritdingiz!")
#         continue
#     else:
#         ildiz = float(qiymat)**(0.5)
#         print(f"{qiymat} ning ildizi {ildiz} ga teng")