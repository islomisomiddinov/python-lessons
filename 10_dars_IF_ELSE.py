# 09.12.2021
# 10-dars. IF-ELSE SHARTLARI va TARMOQLANISH

# avtolar = ['audi', 'kia', 'bmw', 'honda', 'ford']
# for avto in avtolar: # avtolar ichidagi har bir avto uchun...
#     if avto == 'bmw': # ...agar avto bmw ga teng bo'lsa...
#         print(avto.upper()) # avto nomining hamma harflarini katta bilan yoz
#     else: # aks holda...
#         print(avto.title()) # avto nomining faqat birinchi harfini katta qil
        
# ism = 'Ali'

# ism.lower() == 'ali'

# ism = input("ismingiz nima?\n>>>") # Foydalanuvchi ismini so'rayapmiz
# if ism.lower() != 'ali': # Agar ism Aliga teng bo'lmasa...
#     print(f"Uzr {ism.title()}, biz Alini kutayapmiz.") # Quyidagi xabar chiqadi
# else:
#     print("Salom, Ali!")

# javob = float(input("12*6 ning javobi nechaga teng?\n>"))
# if javob != 72:
#     print('Javob xato!')

# yosh = int(input("Yoshingiz nechida? >>> "))
# if yosh >= 18: # yosh 18 dan katta yoki teng bo'lsa...
#     print("Xush kelibsiz!")
# else:
#     print("Kirish mumkin emas!")

# login = input("Yangi login tanlang:")
# if len(login) <= 5: # login uzunligini tekshiramiz
#     print("Login 5 harf yoki belgidan uzun bo'lishi shart!")
    
# t_yil = int(input("Tug'ilgan yilingizni kiriting: > "))
# if 2021-t_yil<18:
#     print(f"Siz {2021-t_yil} yoshda ekansiz.")
#     print('Sizga kirish mumkin emas!')
# else:
#     print("Xush kelibsiz!")

# yosh = int(input("yoshingiz nechida? > "))
# if yosh>70: print("Siz nafaqa yoshida ekansiz!")

# x, y = 250, 50 # x=25 va y=50
# print('x>y') if x>y else print("x<y")


#   #   #   HOMEWORK    #   #   #

##  Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling.
# cars = ['toyota', 'mazda', 'kia', 'gm', 'tesla', 'ford']
# for car in cars:
#     if car == 'gm': print(car.upper())
#     else: print(car.title())

##  Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring. 
# cars = ['toyota', 'mazda', 'kia', 'gm', 'tesla', 'ford']
# for car in cars:
#     print(car.title()) if car!='gm' else print(car.upper())

##  Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
# login = input("loginni kiriting:\n>>> ")
# if login.lower() == 'admin':
#     print("Xush kelibsiz, Admin.")
#     print("Foydalanuvchilar ro'yhatini ko'rishni istaysizmi?")
# else: print("Xush kelibsiz, ", login.title())

##  Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
# print("Iltimos 2 ta son kiriting.")
# son1 = float(input("1-son: "))
# son2 = float(input("2-son: "))
# if son1==son2: print(f"Sonlar bir-biriga teng ekan! {son1}={son2}")

# son = float(input("Istalgan sonni kiriting: "))
# print(f"{son} manfiy son!") if son<0 else print(f"{son} musbat son!")

##  Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
# son = float(input("Istalgan sonni kiriting: "))
# if son>0: print(f"{son} ning ildizi {son**(1/2)} ga teng.")
# else: print("Musbat son kiriting!")