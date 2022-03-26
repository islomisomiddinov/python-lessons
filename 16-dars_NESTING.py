# 17.12.2021
# 16-dars: NESTING

# car0 = {
#         'model':'gentra',
#         'rang':'qora',
#         'yil':2020,
#         'narx':14000,
#         'km':30000,
#         'korobka':'mexanika'
#         }

# car1 = {
#         'model':'cobalt',
#         'rang':'oq',
#         'yil':2019,
#         'narx':10000,
#         'km':45000,
#         'korobka':'avtomat'
#         }

# car2 = {
#         'model':'nexia 3',
#         'rang':'qizil',
#         'yil':2021,
#         'narx':8500,
#         'km':100000,
#         'korobka':'mexanika'
#         }


# car = car2
# print(f"{car['model'].title()}, "
#       f"rangi {car['rang']} , "
#       f"{car['yil']}-yil, narxi $ {car['narx']}")



#   #   RO'YHAT ICHIDA LUG'ATLAR



# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#       f"rangi {car['rang']} , "
#       f"{car['yil']}-yil, narxi $ {car['narx']}")


# print(cars[0]['model'])


# print(f"{cars[2]['rang'].title()} "
#       f"{cars[2]['model']}")


# malibus = []
# for n in range(10):
#     new_car = {
#         'model':'malibu',
#         'rang':None,    #rangi noaniq
#         'yil':2021,
#         'narx':None,
#         'km':0,
#         'korobka':'avto'
#         }
#     malibus.append(new_car)   

# for malibu in malibus:
#     print(malibu)
    
# for malibu in malibus[:3]:
#     malibu['rang'] = 'qizil'
    
# for malibu in malibus:
#     print(malibu)

# for malibu in malibus[3:6]:
#     malibu['rang'] = 'qora'
    
# for malibu in malibus:
#     print(malibu)

# for malibu in malibus[6:]:
#     malibu['rang'] = 'qora'
#     malibu['korobka'] = 'mexanika'
    
# for malibu in malibus:
#     print(malibu)

# for malibu in malibus:
#     if malibu['korobka']=='avto':
#         malibu['narx'] = 40000
#     else: malibu['narx']=37000

# for malibu in malibus:
#     print(malibu)




#   #   LUG'AT ICHIDA RO'YHATLAR



# dasturchilar = {
#     'abror':['redux', 'react', 'js'],
#     'timur':['html', 'css', 'vue.js'],
#     'polvon':['go', 'node.js'],
#     'erkin':['swift', 'flutter']
#     }
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi daturlash tillarini biladi:")
#     for til in tillar:
#         print(til.upper())
        
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi daturlash tillarini biladi: ", end='')
#     for til in tillar:
#         print(f'{til.upper()} ', end='')


# hamkasblar = {
#     'abror':{'familiya':'nabiyev',
#              'tyil':1998,
#              'malumot':'tugallanmagan oliy',
#              'tillar':['c++', 'sql']},
#     'shaxzod':{'familiya':'yuldashev',
#                'tyil':1997,
#                'malumot':'oliy',
#                'tillar':['java', 'js']},
#     'shahboz':{'familiya':'toirov',
#                'tyil':1998,
#                'malumot':"o'rta",
#                'tillar':['go', 'swift']}
#     }

# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, "
#           f"{info['tyil']}-yilda tug'ilgan. "
#           f"Ma'lumoti: {info['malumot']}. \n"
#           f"Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())



#   #   #   HOMEWORK    #   #   #



##  Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxslar
##  haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta
## ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.

# ilm = {
#        'ism':"Mirzo Ulug'bek",
#        'tyil':1394,
#        'tjoy':'sultoniya shahri',
#        'umr':55
#        }
# sanat = {
#     'ism':'picasso',
#     'tyil':1881,
#     'tjoy':'malaga shahri',
#     'umr':92
#     }
# net = {
#        'ism':'steven paul jobs',
#        'tyil':1955,
#        'tjoy':'san-fransisko shahri',
#        'umr':56
#        }
# fan = {
#        'ism':'nicola tesla',
#        'tyil':1856,
#        'tjoy':'smilyan shahri',
#        'umr':86
#        }
# m_shaxslar = [ilm, sanat, net, fan]

# for shaxs in m_shaxslar:
#     print(f"\t{shaxs['ism'].title()} {shaxs['tyil']}-yilda \
# {shaxs['tjoy'].capitalize()}da tavallud topgan. \
# {shaxs['umr']} yil umr ko'rgan.\n")



##  Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham
##  qo'shing. For sikli yordamida muallifning ismi va uning asarlarini
##  konsolga chiqaring.

# ilm['asarlar'] = ["ziji jadidi ko'ragoniy", "tarixi arba' ulus"]
# sanat['asarlar'] = ['tinchlik kabutari', 'menina']
# net['asarlar'] = ['macintosh', 'apple']
# fan['asarlar'] = ['elektromagnetizm']

# for shaxs in m_shaxslar:
#     print(f"\n{shaxs['ism'].title()}ning mashhur asarlari: ")
#     for asar in shaxs['asarlar']:
#         print(f"{asar.title()}, ")


##  Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida
##  so'rang. Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat
##  ko'rinishida lug'atga saqlang.  Natijani konsolga chiqaring.

# filmlar = {
#     'xasan':['titanik', 'hulk', 'temir odam'],
#     'xusan':['gul', 'iqror', "o'yin"],
#     'laziz':['sarob', 'mafiya', 'ufq'],
#     'madina':['qish sonatasi', 'tangem', 'kuz ifori']
#     }

# for ism, kinolar in filmlar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari: ")
#     for kino in kinolar:
#         print(kino.title())


##  Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar
##  haqida ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida
##  ma'lumotni konsolga chiqaring.

davlatlar = {
    'urugvay':{'nomi':'urugvay respublikasi',
               'poytaxt':'montevideo',
               'joylashuv':'janubiy amerika',
               'til':'ispan'},
    'monako':{'nomi':'monako knyazligi',
               'poytaxt':'monako',
               'joylashuv':'yevropa',
               'til':'fransuz'},
    'baa':{'nomi':'birlashgan arab amirliklari',
           'poytaxt':'abu-dabi',
           'joylashuv':'osiyo',
           'til':'arab'},
    'nigeriya':{'nomi':'nigeriya federativ respublikasi',
                'poytaxt':'abuja',
                'joylashuv':'afrika',
                'til':'ingliz'}
    }
# for nom, info in davlatlar.items():
#     print(f"\n{nom.title()}ning poytaxti {info['poytaxt'].title()} shahri."
#           f"\nRasmiy atalishi: {info['nomi'].title()}. "
#           f"\nJoylashuvi: {info['joylashuv'].title()} qit'asi"
#           f"\nDavlat tili: {info['til']}")


##  Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni
##  emas, foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar
##  davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida
##  ma'lumot yo'q" degan xabarni chiqaring.

# country = input("Davlat nomini kiriting: ").lower()
# if country in davlatlar:
#     info = davlatlar[country ]
#     print(f"\n{country .title()}ning poytaxti {info['poytaxt'].title()}. "
#           f"\nRasmiy atalishi: {info['nomi'].title()}. "
#           f"\nJoylashuvi: {info['joylashuv'].title()} qit'asi"
#           f"\nDavlat tili: {info['til']}")
# else: print(f"\nBizda {country.title()} haqida ma'lumot yo'q.")