def avto_info(kompaniya, model, rangi, korobka, yili, narxi=None):
    """Avtomobil haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    avto = {'kompaniya':kompaniya,
        'model':model,
        'rang':rangi,
        'korobka':korobka,
        'yil':yili,
        'narx':narxi}
    return avto

def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni \
    bitta ro'yhatga joylash imkonini beruvchi funksiya"""
    print("Saytimizdagi avtomobillar ro'yhatini shakllantiramiz.")
    avtolar = []    # Salondagi avtolar uchun bo'sh ro'yhat
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting:", end='')
        kompaniya=input("Ishlab chiqaruvchi: ")
        model=input("Modeli: ")
        rangi=input("Rangi: ")
        korobka=input("Korobka: ")
        yili=input("Ishlab chiqarilgan yili: ")
        narxi=input("Narxi: ")
        #  Foydalanuvchi kiritgan ma'lumotlardan avto_info funksiyasi yordamida
        #  lug'at shakllantirib, har bir lug'atni ro'yhatga qo'shamiz:
        avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narxi))
        ##  Yana avto qo'shish-qo'shmasligini so'raymiz
        javob = input("Yana avto qo'shasizmi? (yes/no): > ")
        if javob == "yo'q":
            break
    return avtolar
     
def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan funksiyani konsolga chiqaruvchi funksiya"""
    print(f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} \
{avto_info['model'].upper()}, {avto_info['korobka'].title()} korobka."
    f"{avto_info['yil']}-yil. Narxi: ${avto_info['narx']}")