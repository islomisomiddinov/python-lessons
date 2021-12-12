# 09.12.2021
# 11-dars. IF-ELIF-ELSE

# yosh = int(input("Yoshingiz nechida? > "))
# if yosh <= 4: print("Sizga kirish bepul.")
# elif yosh <=12: print("Siz uchun chipta narxi 5000 so'm.")
# elif yosh <= 18: print("Sizga kirish 7000 so'm.")
# else: print("Sizga kirish narxi 10000 so'm.")

# yosh = int(input("Yoshingiz nechida? > "))
# if yosh <= 4: narx = 0
# elif yosh <=12: narx = 5000
# elif yosh <= 18: narx = 7000
# else: narx = 10000

# print(f"Siz uchun bilet narxi {narx} so'm")

#   #   OR operatori

# kun = input("Bugun haftaning qaysi kuni? > ")
# if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
#     print('Bugun dam olish kuni!')
# else:
#     print("Bugun ish kuni!")

#   #   AND operatori

# kun = input("Bugun qaysi kun? > ")
# harorat = float(input("Havo harorati qanday? > "))
# if kun.lower()=='yakshanba' and harorat>=25:
#     print("Bugun basseynga boramiz!!!")
# elif kun.lower()=='yakshanba' and harorat<25:
#     print("Bugun baliqqa boramiz!")
    
#   #   OR va AND operatorlari

# kun = input("Bugun qaysi kun? > ")
# harorat = float(input("Havo harorati qanday? > "))
# if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>=25:
#     print("Bugun basseynga boramiz!!!")
# elif (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat<25:
#     print("Bugun baliqqa boramiz!")

# narx = 15000 # mijoz 15000 so'mga taom oldi
# choy = True # mijoz choy ham oldi
# salat = True # mijoz salat olmadi
# if choy and salat: # agar mijoz choy ham, salat ham olgan bo'lsa
#     narx = narx + 10000 # narxga 10000 so'm qo'shamiz
# elif choy or salat: # agar choy yoki salat olgan bo'lsa
#     narx = narx + 5000 # narxga 5000 so'm qo'shamiz
# print(f"Jami {narx} so'm.")

# narx = 15000 # mijoz 15000 so'mga ovqat oldi
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
# ##Quyidagi har bir shart alohida tekshiriladi bir-biriga bog'liq emas
# if choy: # agar choy olsa
#     print("Mijoz choy oldi.")
#     narx = narx + 3000
# if salat: # agar salat olsa
#     print("Mijoz salat oldi.")
#     narx = narx + 5000
# if non: # agar non olsa
#     print("Mijoz non oldi.")
#     narx = narx + 2000
# if kompot: # agar kompot olsa
#     print("Mijoz kompot oldi.")
#     narx = narx + 5000
# if assorti: # agar assoti olsa
#     print("Mijoz assorti oldi.")
#     narx = narx + 15000

# print(f"Jami {narx} so'm.")

# narx = 15000 # mijoz 15000 so'mga ovqat oldi
# choy = 1
# salat = 0
# non = 1
# kompot = 1
# assorti = 1
# ##Quyidagi har bir shart alohida tekshiriladi bir-biriga bog'liq emas
# if choy: # agar choy olsa
#     print("Mijoz choy oldi.")
#     narx = narx + 3000
# if salat: # agar salat olsa
#     print("Mijoz salat oldi.")
#     narx = narx + 5000
# if non: # agar non olsa
#     print("Mijoz non oldi.")
#     narx = narx + 2000
# if kompot: # agar kompot olsa
#     print("Mijoz kompot oldi.")
#     narx = narx + 5000
# if assorti: # agar assoti olsa
#     print("Mijoz assorti oldi.")
#     narx = narx + 15000

# print(f"Jami {narx} so'm.")

#   #   IN operatori

# menu = ['osh', 'kabob', 'dimlama', 'norin', 'somsa']
# 'manti' in menu # menu da manti bormi?

# menu = ['osh', 'kabob', 'dimlama', 'norin', 'somsa']
# taom = input("Qanday taom buyurtma berasiz? > ")
# if taom.lower() in menu:
#     print("Buyurtmangiz qabul qilindi.")
# else:
#     print("Afsuski, bizda bunday taom yo'q.")

# menu = ['osh', 'kabob', 'dimlama', 'norin', 'somsa']
# taom = input("Qanday taom buyurtma berasiz? > ")
# if taom.lower() not in menu:
#     print("Afsuski, bizda bunday taom yo'q.")
# else:
#     print("Buyurtmangiz qabul qilindi.")
    
# menu = ['osh', 'manti', 'kabob', 'somsa', 'dimlama']
# buyurtmalar = ['somsa', 'norin', 'kabob']

# if buyurtmalar: # ro'yhatda biror element bo'lsa bu ifoda True qaytaradi
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor.")
#         else: 
#             print(f"Kechirasiz, menuda {taom} yo'q.")
# else: # agar ro'yhat bo'sh bo'lsa
#     print("Savatchangiz bo'sh")


#   #   #   HOMEWORK    #   #   #

##  Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!",
##agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
# son = float(input("Juft son kiriting: > "))
# if son % 2 == 0:
#     print("Rahmat")
# else:
#     print("Bu son juft emas.")

##  Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
## Agar foydalanuvchi 4 yoshdan kichkina yoki 60 dan katta bo'lsa bepul
##Agar foydalanuvchi 18 dan kichik bo'lsa 10000 so'm
##Agar foydalanuvchi 18 dan katta bo'lsa 20000 so'm

# yosh = int(input("Yoshingiz nechida? > "))
# if yosh<=4 or yosh >=60: narx = 0
# elif yosh<=18: narx = 10000
# elif yosh>18: narx = 20000

# print(f"Sizga kirish {narx} so'm.")

##  Foydalanuvchidan ikkita son kiritishni so'rang, sonlarni solishtiring va 
##ularning teng yoki katta/kichikligi haqida xabarni chiqaring
# x = float(input("birinchi sonni kiriting: > "))
# z = float(input("ikkinchi sonni kiriting: > "))
# if x>z: print(f"{x}>{z}")
# elif x<z: print(f"{x}<{z}")
# elif x==z: print(f"{x}={z}")

##  mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va 
##foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va 
##qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# mahsulotlar = ['mix','arra','reyka','lak','pena','sement','ohak','bolta','truba','plastik','shlang']
# savat = []
# for s in range(5):
#     savat.append(input(f"Savatga {s+1}-mahsulotni qo'shing. >>> "))
# for s in savat:
#     if s in mahsulotlar:
#         print(f"{s} do'konimizda bor.")
#     else:
#         print(f"{s} do'konimizda yo'q.")
        
##  Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda
##bor mahsulotlarni yangi, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.
##Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi 
##mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
# mahsulotlar = ['mix','arra','reyka','lak','pena','sement','ohak','bolta','truba','plastik','shlang']
# savat = []
# bor_mahsulotlar = []
# mavjud_emas = []
# for s in range(5):
#     savat.append(input(f"Savatga {s+1}-mahsulotni qo'shing. >>> "))
# for s in savat:
#     if s in mahsulotlar:
#         bor_mahsulotlar.append(s)
#     else:
#         mavjud_emas.append(s)
# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")    
#     for s in mavjud_emas:
#         print(s)
# else:
#     print("Siz so'ragan hamma mahsulotlar bor!")
# print("\nDo'konimizda quyidagi mahsulotlar bor: ")
# for s in bor_mahsulotlar:
#     print(s)


##  foydalanuvchilar degan ro'yxat tuzing va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va
##foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday 
##login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
# foydalanuvchilar = ['iiislamic','mars','karl','ironman','benom']
# login = input("Yangi login kiriting: > ")
# if login.lower() in foydalanuvchilar:
#     print("Bu login band, yangi login tanlang!")
# else:
#     print(f"Xush kelibsiz, {login.title()}")


##  Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 dan 10 gacha bo'lgan sonlardan qay 
##biriga qoldiqsiz bo'linishini konsolga chiqaring. 
# x = int(input("Istalgan butun son kiriting: > "))
# for son in range(2,11):
#     if not (x % son):
#         print(f"{x} {son} ga qoldiqsiz bo'linadi.")