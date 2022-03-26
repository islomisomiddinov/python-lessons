# 20.12.2021
# 20-dars:    FUNKSIYADAN QIYMAT QAYTARISH

# def toliq_ism_yasa(ism, familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     print(toliq_ism)
    
# toliq_ism_yasa('komil','erkinov')


# def toliq_ism_yasa(ism, familiya):
#     """To'liq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism} {familiya}"
#     return toliq_ism
    
# talaba1 = toliq_ism_yasa('komil','erkinov')
# talaba2 = toliq_ism_yasa('toir','qudratov')
# print(f"Darsga kelmagan talabalar: \n{talaba1};\n{talaba2}.")
# print(f"{talaba2} darsga kechikib keldi.")



##  IXTIYORIY ARGUMENT


# def toliq_ism_otasi(ism, familiya, otasining_ismi=''):
#     """To'liq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism = f"{familiya} {ism} {otasining_ismi}"
#     else:
#         toliq_ism = f"{familiya} {ism}"
#     return toliq_ism.title()

# talaba1 = toliq_ism_otasi('komil','erkinov')
# talaba2 = toliq_ism_otasi('toir','qudratov', 'bahtiyorovich')
# print(f"Darsga kelmagan talabalar: \n{talaba1};\n{talaba2}.")



##  FUNKSIYA dan LUG'AT qaytarish


# def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
#     """Avtomobil haqida ma'lumot qaytaruvchi funksiya"""
#     avto = {
#         'kompaniya':kompaniya,
#         'model':model,
#         'rang':rangi,
#         'yil':yili,
#         'korobka':korobka,
#         'narx':narxi
#         }
#     return avto

# avto1 = avto_info('Kia', 'K5', 'Qora', 'Avtomat', 2021)
# avto2 = avto_info('Ravon', 'Spark', 'Oq', 'Mexanika', 2020, 7000)
# avtolar = [avto1, avto2]
# print("Online bozorda sotuvda mavjud avtomobillar:")
# for avto in avtolar:
#     if avto['narx']:
#         narx = avto['narx']
#     else:
#         narx = "Noma'lum"
#     print(f"{avto['rang'].title()} {avto['model'].title()} - Narxi: {narx}")



##  FUNKSIYA dan RO'YHAT qaytarish


# def oraliq(min, max):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += 1
#     return sonlar

# print(oraliq(1, 11))
# print(oraliq(100, 301))


# def oraliq(min, max, qadam=1):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar

# print(oraliq(1, 11, 3))
# print(oraliq(100, 301, 7))


# def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
#     avto = {
#         'kompaniya':kompaniya,
#         'model':model,
#         'rang':rangi,
#         'korobka':korobka,
#         'yil':yili,
#         'narx':narxi
#         }
#     return avto

# print("Saytimizdagi avtomobillar ro'yhatini shakllantiramiz.")
# avtolar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting:", end='')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narxi=input("Narxi: ")
    ##  Foydalanuvchi kiritgan ma'lumotlardan avto_info funksiyasi yordamida
    ##  lug'at shakllantirib, har bir lug'atni ro'yhatga qo'shamiz:
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narxi))
#     ##  Yana avto qo'shish-qo'shmasligini so'raymiz
#     javob = input("Yana avto qo'shasizmi? (yes/no): > ")
#     if javob == "yo'q":
#         break
# print("\nSalonimizdagi avtolar:")
# for avto in avtolar:
#     if avto['narx']:
#         narx = avto['narx']
#     else:
#         narx = "Noma'lum"
#     print(f"{avto['rang'].title()} {avto['kompaniya'].title()} \
# {avto['model'].title()}, {avto['korobka']} korobka. Narxi: ${narx}")




#   #   #   HOMEWORK    #   #   #



##  Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email
##  manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi
##  funksiya yozing. Lug'atda foydalanuvchi yoshi ham bo'lsin. Ba'zi
##  argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)

# def foydalanuvchi_info(ism, familiya, tyil, tjoy, email='', tel=None):
#     foydalanuvchi = {
#         'ism':ism,
#         'familiya':familiya,
#         'tyil':tyil,
#         'yoshi':2021-tyil,
#         'tjoy':tjoy,
#         'email':email,
#         'telefon':tel,
#         }
#     return foydalanuvchi


##  Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar
##  degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi
##  ma'lumotni konsolga chiqaring.

# print("Foydalanuvchi haqida ma'lumotlarni kiriting.")
# foydalanuvchilar = []
# while True:
#     ism=input("Ismingiz: ")
#     familiya=input("Familiyangiz: ")
#     tyil=int(input("Tug'ilgan yilingiz: "))
#     tjoy=input("Tug'ilgan joyingiz: ")
#     email=input("Email: ")
#     telefon=input("Telefon raqamingiz: ")
#     foydalanuvchilar.append(foydalanuvchi_info(ism, familiya, tyil, tjoy, email, telefon))
#     javob = input("Davom etasizmi? (yes/no): ")
#     if javob == 'no':
#         break

# print("Foydalanuvchilar: ")
# for foydalanuvchi in foydalanuvchilar:
#     print(f"{foydalanuvchi['ism'].title()} {foydalanuvchi['familiya'].title()}\
#   {foydalanuvchi['yoshi']} yoshda. Telefon raqami: {foydalanuvchi['telefon']}")
 
 
##  Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing

# def taqqosla(a, b, c):
#     """Kiritilgan 3 ta sonning eng kattasini aniqlovchi funksiya"""
#     max = a
#     if b>max:
#         max=b
#     elif c>max:
#         max=c
#     return max


# def kattasi(x, y, z):
#     max = x
#     if y >= max:
#         max = y
#     if z >= max:
#         max = z
#     return max

# print(kattasi(4, 95, 23))


##  Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini,
##  diametrini, perimetri va yuzini lug'at ko'rinishida
##  qaytaruvchi funksiya yozing

# def aylana_info(radius, pi=3.14):
#     aylana = {
#         'radius':radius,
#         'diametr':2*radius,
#         'perimetr':2*pi*radius,
#         'yuza':pi*(radius**2)
#         }
#     return aylana
# print("Aylananing radiusini kiriting:")
# aylanalar = []
# n=1
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting:", end='')
#     radius=float(input(f"{n}-Aylana radiusi: "))
#     aylanalar.append(aylana_info(radius, pi=3.14))
#     n += 1
#     javob = input("Yangi aylana haqida ma'lumot qo'shasizmi? (yes/no): > ")
#     if javob == "no":
#         break
# print("\nAylanalar haqida ma'lumotlar:")
# for aylana in aylanalar:
#     print(f"\nAylananing radiusi: {aylana['radius']}, "
#     f"\ndiametri: {aylana['diametr']}, "
#     f"\nperimetri: {aylana['perimetr']}, "
#     f"\nyuzasi: {aylana['yuza']}"
#     )


##  Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing
##  (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi,
##  1 dan katta musbat sonlar)

# def tub_sonlar_top(min, max):
#     tub_sonlar = []
#     for n in range(min, max + 1):
#         tub = True
#         if n <= 1:
#             tub = False
#         else:
#             for x in range(2, n):
#                 if n % x == 0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)

#     return tub_sonlar

# print(tub_sonlar_top(-7, 30))


##  Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-
##  ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing.  Ta’rif: Har
##  bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-
##  ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had
##  ko’pincha 1 deb olinadi.  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...

# def fibonachchi(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)
#         else:
#             sonlar.append(sonlar[x-1] + sonlar[x-2])
#     return sonlar
    
# print(fibonachchi(7))