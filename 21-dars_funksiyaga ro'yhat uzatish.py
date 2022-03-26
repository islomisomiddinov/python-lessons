# 23.12.2021
# 21-dars:    FUNKSIYAGA RO'YHAT UZATISH

# def bahola(ismlar):
#     baholar = {}
#     while ismlar:
#         ism = ismlar.pop()
#         baho = int(input(f"Talaba {ism.title()}ning bahosini kiriting: "))
#         baholar[ism] = baho
#     return baholar

# talabalar = ['abror', 'bobur', 'ikrom', 'anvar']
# baholar = bahola(talabalar[:])
# print(baholar)
# print(talabalar)



#   #   #   HOMEWORK    #   #   #


##  Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning
##  birinchi harfini katta harfga o'zgatiruvchi funksiya yozing. 

# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i] = matnlar[i].title()

# ismlar = ["ali", "vali", "hasan", "husan"]
# katta_harf(ismlar)
# print(ismlar)


# def katta_harf(matnlar):
#     for soz in range(len(matnlar)):
#         matnlar[soz] = matnlar[soz].title()
#     return matnlar
# ismlar = ["ali", "vali", "hasan", "husan"]
# print(katta_harf(ismlar))


##  Yuqoridagi funksiyani asl ro'yxatni o'zgartirmaydigan va yangi ro'yxat
##  qaytaradigan qilib o'zgartiring

# def katta_harf(matnlar):
#     matnlar = matnlar[:]
#     for soz in range(len(matnlar)):
#         matnlar[soz] = matnlar[soz].title()
#     return matnlar
# ismlar = ["ali", "vali", "hasan", "husan"]
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)


##  Darsimiz davomida yozgan bahola funksiyasini .pop() metodidan
##  foydalanmasdan va asl ro'yxatga o'zgartirish kiritmasdan faqat lug'at
##  qaytaradigan qilib yozing.

# def bahola(talabalar):
#     baholar = {}
#     for talaba in talabalar:
#         baho = int(input(f"{talaba.title()} bahosini kiriting: "))
#         baholar[talaba] = baho
#     return baholar

# talabalar = ['abror', 'bobur', 'ikrom', 'anvar']
# baholar = bahola(talabalar)
# print(baholar)
# print(talabalar)