# 20.12.2021
# 19-dars:    FUNCTIONS (FUNKSIYALAR)

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalom alaykum!")

# salom_ber()

def salom_ber(ism):     # () ichidagi parametr deyiladi
    """Foydalanuvchi ismini qabul qilib,
    unga salom beruvchi funksiya"""
    print(f"Assalom aleykum, hurmatli {ism.title()}!")
    
# salom_ber('ahror')  # foydalanuvchi kiritgan () ichidagi argument deyiladi
# salom_ber('behruz')

# salom_ber()     # argument qolib ketdi


def toliq_ism(ism, familiya):
    """Foydalanuvchi ismi va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")
    
# toliq_ism('akbar', 'xoldorov')
# toliq_ism(akbar, xoldorov)
# toliq_ism('xoldorov', 'akbar')


# def yosh_hisobla(ism, t_yil):
#     """Foydalanuvchi yoshini hisoblaydigan funksiya"""
#     print(f"{ism.title()} {2021-t_yil} yoshda")
    
# yosh_hisobla('ali', 2003)
# yosh_hisobla(2003, 'ali')

# yosh_hisobla(t_yil=2003, ism='guli')


def yosh_hisobla(tugilgan_yil, joriy_yil=2021):
    """Foydalanuvchi tug'ilgan yilidan yoshini topadigan funksiya"""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz.")
    
# yosh_hisobla(1999,2021)
# yosh_hisobla(1999)



#   #   #   HOMEWORK    #   #   #



##  Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini
##  hisoblaydigan funksiya yozing.

# def t_yilini_hisobla(ism, yosh):
#     """Foydalanuvchi ismi va yoshini so'rab,
#     uning tug'ilgan yilini hisoblaydigan funksiya"""
#     print(f"Foydalanuvchi {ism.title()} {2021-yosh}-yilda tug'ilgan.")
    
# t_yilini_hisobla(ism='erkin', yosh=36)


##  Foydalanuvchidan son olib, uning kvadrati va kubini konsolga
##  chiqaruvchi funksiya yozing.

# def darajaga_oshir(son):
#     """Kiritilgan sonning kvadrati va kubini hisoblovchi funksiya"""
#     print(f"{son} ning kvadrati {son**2} ga, \
# kubi {son**3} ga teng.")
          
# darajaga_oshir(7)


##  Foydalanuvchidan son olib, son juft yoki toqligini konsolga
##  chiqaruvchi funksiya yozing.

# def juftmi(son):
#     """Kiritilgan son juft yoki toqligini konsolga chiqaruvchi funksiya"""
#     if son%2 == 0:
#         print(f"{son} juft son.")
#     else:   print(f"{son} toq son.")
    
# juftmi(245.31)
# juftmi(-20)


##  Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi
##  funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng"
##  degan xabarni chiqaring.

# def solishtir(x, y):
#     """Ikki sonni solishtiruvchi funksiya"""
#     if x>y:     print(f"{x}>{y}")
#     elif x<y:   print({y}>{x})
#     else:       print(f"{x}={y}")
    
# solishtir(98, -53)


##  Foydalanuvchidan x va y sonlarini olib, ni konsolga
##  chiqaruvchi funksiya yozing.

# def darajasi(x, y):
#     """x ni y-darajaga oshiruvchi funksiya"""
#     print(f"{x} ning {y} darajasi {x**y} ga teng.")
    
# darajasi(5,3)
# darajasi(49, 1/2)


##  Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.

# def x_kvadrati(x, y=2):
#     """x ni 2-darajaga oshiruvchi funksiya"""
#     print(f"{x} ning {y} darajasi {x**y} ga teng.")
    
# x_kvadrati(5)
# x_kvadrati(49)


##  Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan
##  sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing.
##  Natijalarni konsolga chiqaring.

# def qoldiq_aniqla(son):
#     """Kiritilgan sonning qoldiqsiz bo'linuvchilarini aniqlash"""
#     for n in range(2,11):
#         if not son % n:
#             print(f"{son} {n} ga qoldiqsiz bo'linadi.")
            
# qoldiq_aniqla(93)