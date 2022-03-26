# 12.12.2021
# 12-dars DICTIONARY (Lug'at)

# car_0 = {'model':'ferrari', 'rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])

# en_uz = {'apple':'olma', 'banana':'banan', 'pear':'nok'}

# mevalar = {'olma':10000, 'tarvuz':18000, 'non':3000}
# print(f"Nonning narxi {mevalar['non']} so'm")

##  Lug'atda istalgan ma'lumot turlarini saqlash mumkin
# talaba_0 = {'ism':'murod olimov', 'yosh':21, 't_yil':2000}
# print(f"{talaba_0['ism'].title()},\
#       {talaba_0['t_yil']}-yilda tug'ilgan,\
#       {talaba_0['yosh']} yoshda")
      
##  Yangi kalit so'z va qiymat qo'shish
# talaba_0['kurs'] = 4
# talaba_0['fakultet'] = 'informatika'
# talaba_0['ism'] = 'abdulloh'

##  Bo'sh lug'at
# talaba_1 = {}
# talaba_1['ism'] = 'laziz qurbonov'
# talaba_1['kurs'] = 3
# talaba_1['t_yil'] = 2000
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

##  Qiymat yangilash
# talaba_1['kurs'] = 4
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

##  Kalit so'z-qiymatni o'chirib tashlash
# talaba_0 = {'ism':'murod olimov', 'yosh':20, 't_yil':2000}
# print(talaba_0)
# del talaba_0['yosh']
# print(talaba_0)

##  Lug'atlarni bir nechta qatorda yozish
# telefonlar = {
#     'abror':'galaxy note20',
#     'bobur':'iphone 12',
#     'jasur':'redmi 10'
#     }



##  get() metodi


# phone = telefonlar['abror']
# print(f"Abrorning telefoni {phone}")

# phone = telefonlar['xasan']
# print(f"Xasanning telefoni {phone}")

# phone = telefonlar.get('xasan', 'Bunday ism mavjud emas')
# print(phone)

# phone = telefonlar.get('bobur', 'Bunday ism mavjud emas')
# print(phone)

# meva = en_uz.get('watermelon', 'Bunday meva mavjud emas')
# print(meva)

# meva = en_uz.get('pear', 'Bunday meva mavjud emas')
# print(meva)

# meva = en_uz.get('lemon')
# print(meva)



#   #   #   HOMEWORK    #   #   #


##  otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting 
##  (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :Otamning 
##  ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan


# otam = {'ism':'otam, xatamov bahromjon', 't_yil':1959, 'kasb':'vet-shifokor', 't_joy':'Toshkent viloyati'}
# onam = {'ism':'onam, xatamova shohida', 't_yil':1962, 'kasb':"o'qituvchi", 't_joy':'Toshkent viloyati'}
# opam = {'ism':'opam, musabekova shoira', 't_yil':1985, 'kasb':'tarbiyachi', 't_joy':'Toshkent viloyati'}
# akam1 = {'ism':'katta akam, xatamov adham', 't_yil':1987, 'kasb':'elektrik', 't_joy':'Toshkent viloyati'}
# akam2 = {'ism':'kichik akam, xatamov laziz', 't_yil':1991, 'kasb':'vet-vrach', 't_joy':'Toshkent viloyati'}

# qarindoshlar = [otam, onam, opam, akam1, akam2]

# for qarindosh in  qarindoshlar:
#     print(f" {qarindosh['ism'].title()}, {qarindosh['t_yil']}-yilda {qarindosh['t_joy'].capitalize()}da tug'ilgan.\n")

# print(f"Otamning ismi {otam['ism'].title()}, {otam['t_yil']}-yilda {otam['t_joy'].title()}da tug'ilgan.\n")
# print(f"Onamning ismi {onam['ism'].title()}, {onam['t_yil']}-yilda {onam['t_joy'].title()}da tug'ilgan.\n")
# print(f"Opamning ismi {opam['ism'].title()}, {opam['t_yil']}-yilda {opam['t_joy'].title()}da tug'ilgan.\n")
# print(f"Katta akamning ismi {akam1['ism'].title()}, {akam1['t_yil']}-yilda {akam1['t_joy'].title()}da tug'ilgan.\n")
# print(f"Kichik akamning ismi {akam2['ism'].title()}, {akam2['t_yil']}-yilda {akam2['t_joy'].title()}da tug'ilgan.\n")



##  Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin.
##  Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh

# taomlar = {'adam':'palov', 'oyim':'shashlik', 'akam1':'dimlama', 'akam2':'norin', 'opam':'salat'}
# print(f"Adamning sevimli ovqati {taomlar['adam']}")
# print(f"Oyimning sevimli ovqati {taomlar['oyim']}")
# print(f"Akamning sevimli ovqati {taomlar['akam2']}")



##  Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float,
##  string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.

# python = {'integer':'butun son',
#           'syntaxerror':'yozish xatoligi',
#           'upper':'matndagi barcha harflarni katta harf qiladi',
#           'input':"foydalanuvchidan ma'lumot so'raydi",
#           'tuple':"o'zgarmas ro'yhat",
#           'del':"o'chirish operatori",
#           'append':"ro'yhatga ma'lumot qo'shish metodi",
#           'if':'agar',
#           'else':'aks holda',
#           'remove':'olib tashlash'
#           }


##  Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering.
##  Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.

# soz = input("Pythonga oid birorta so'zni yozing:\n> ").lower()
# print(python.get(soz, "Bunday so'z mavjud emas."))



##  Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.

# soz = input("Pythonga oid birorta so'zni yozing:\n> ").lower()
# tarjima = python.get(soz)
# if tarjima == None:
#     print("Bunday so'z mavjud emas.")
# else:
#     print(f"{soz.title()} so'zi {tarjima} deb tarjima qilinadi.")`