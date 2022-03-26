# 23.12.2021
# 22-dars:    *args va **kwargs



##  *args   (arguments)


# def avto_info(kompaniya, model, rang, yil, korobka, narx=None):
#     avto = {
#         'kompaniya':kompaniya,
#         'model':model,
#         'rang':rang,
#         'yil':yil,
#         'korobka':korobka,
#         'narx':narx
#         }
#     return avto
# avto1 = avto_info('toyota', 'yaris', 'silver', 2015, 'avtomat')
# avto2 = avto_info('porsche', 'panameria', 'qora', 2017, 'avtomat', 75000)
# avtolar = [avto1, avto2]
# print("Online bozordagi mavjud avtomobillar:")
# for avto in avtolar:
#     if avto['narx']:
#         narx = avto['narx']
#     else:
#         narx = "Noma'lum"
#     print(f"{avto['rang'].title()} {avto['model'].title()}.\
#   Korobka: {avto['korobka']}. Ishlab chiqarilgan yili: {avto['yil']}\
#   Narxi: {avto['narx']}")


# def summa(*sonlar):
#     """Kiritlgan sonlar yig'indisini hisoblaydigan funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi
# print(summa(1,2))
# print(summa(4,7,9))
# print(summa())

##//
# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     jami = sum(sonlar)
#     return jami
# print(summa(1, 3, 4, 5, 6))

##//
# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     return sum(sonlar)
# print(summa(4, 7, 9, -3))


# def summa(x, y, *sonlar):
#     """Kiritilgan sonlar yigi'disini hisoblaydigan funksiya"""
#     return x + y + sum(sonlar)
# print(summa(1, 2))
# print(summa(2, 4, -7, 41))
# print(summa(3))




##  **kwargs    (keywords arguments)


# def avto_info(kompaniya, model, **malumotlar):
    # malumotlar['kompaniya'] = kompaniya
    # malumotlar['model'] = model
    # return malumotlar
# avto1 = avto_info('GM', 'gentra', rang='qora', yil=2019, avtomat='avtomat')
# avto2 = avto_info('GM', 'spark', rang='oq', yil=2020, narx=7000)




#   #   #   HOMEWORK    #   #   #


#  Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi
#  funksiya yozing

# def kopaytir(*sonlar):
#     kopaytma = 1
#     for son in sonlar:
#         kopaytma *= son
#     return kopaytma
# print(kopaytir(2, 3, 4, 1))


#  Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi
#  funkisya yozing. Talabaning ismi va familiyasi majburiy argument,
#  qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi
#  mumkin bo'lsin.

def talaba_info(ism, familiya, **info):
    info['ism'] = ism.title()
    info['familiya'] = familiya.title()
    return info
talaba1=talaba_info('javlon','hurramov',yoshi=36,kasbi='dasturchi'.title())
print(talaba1)