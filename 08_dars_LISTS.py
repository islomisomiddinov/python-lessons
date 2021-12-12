# 08-dars. LISTS
# 08.12.2021

# TARTIBLASH
# cars = ['bmw', 'mercedes benz', 'volvo', 'gm', 'tesla', 'audi']
# cars.sort()
# print(cars)

#   #   #   KATTA va KICHIK HARFLAR
# cars = ['Bmw', 'mercedes benz', 'volvo', 'gm', 'tesla', 'audi']
# cars.sort()
# print(cars)

#   #   TESKARI TARTIB
# cars = ['bmw', 'mercedes benz', 'tesla', 'volvo', 'audi', 'honda']
# cars.sort(reverse=True)
# print(cars)

#   #   SORTED()
# mehmonlar = ['Odil', 'Hamid', 'Temur', 'Avazbek', 'Farruh']
# print("sorted() qaytargan ro'yhat:", sorted(mehmonlar))
# print("Asl ro'yhat o'zgarmas qoldi:", mehmonlar)
# print(sorted(mehmonlar, reverse=True))

#   #   SONLI RO'YHATLAR
# ages = [12, 63, 57, 36, 11, 92]
# ages.sort()
# print(ages)
# print(sorted(ages, reverse=True))

#   #   RO'YHATNI ORTIDAN BOSHLAB CHIQARISH
# fruits = ['banana', 'watermelon', 'pear', 'lemon', 'apricot']
# fruits.reverse()
# print(fruits)
# print(sorted(fruits, reverse=True))
# print(sorted(fruits))

#   #   RO'YHAT UZUNLIGI
# fruits = ['banana', 'apple', 'watermelon', 'melon', 'apricot', 'pear']
# print("Elementlar soni:", len(fruits))  #len(fruits) ro'yhat uzunligini qaytaradi

#   #   RANGE
# sonlar = list(range(1,11))
# print(sonlar)

#   #   RANGE va QADAM
# juft_sonlar = list(range(2,21,2))  # 2 dan 21 gacha 2 qadam bilan sonlar chiqaradi
# toq_sonlar = list(range(1,20,2))  # 1 dan 20 gacha 2 qadam bilan toq sonlar chiqaradi
# print("Juft_sonlar: ", juft_sonlar)
# print("Toq sonlar: ", toq_sonlar)

#   #   MIN(), MAX(), SUM()
# narxlar = [12000, 5600, 97990, 2500, 71000, 1600]
# arzon = min(narxlar)
# qimmat = max(narxlar)
# jami = sum(narxlar)
# print("Eng arzon narx: ", arzon, ". Eng qimmat narx: ", qimmat, "Narxlarning jami yig'indisi: ", jami)

#   #   RO'YHATNI KESISH
# cars = ['bmw', 'mercedes benz', 'volvo', 'tesla', 'audi', 'honda', 'ford']
# my_cars = cars[0:4] # 0-indeksdan boshlab 4 ta element ajratib oladi
# print(my_cars)
# print(cars[2:5]) # 2-3-4-elementlarni ajratib oladi
# print(cars[:4]) # ro'yhat boshidan 4-gacha kesadi (0, 1, 2, 3)
# print(cars[3:]) # 3-elementdan boshlab ro'yhat oxirigacha kesadi

#   #   RO'YHATDAN NUSXA OLISH
# sonlar = [1, 2, 3, 4, 5] # sonlar degan ro'yhat yaratamiz
# sonlar2 = sonlar # sonlar2 degan ro'yhatni sonlar ga tenglashtiramiz
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yhati: ", sonlar)
# print("Bu sonlar2 ro'yhati: ", sonlar2)

# sonlar2 = sonlar[:] # [:] ro'yhatdan to'liq nusxa ko'chirib oladi
# sonlar2.append(6) # sonlar2 ga 6 sonini qo'shamiz
# sonlar2.append(7) # sonlar2 ga 7 sonini qo'shamiz
# print("Bu sonlar ro'yhati: ", sonlar)
# print("Bu sonlar2 ro'yhati: ", sonlar2)

#   #   TUPLES
# tomonlar = (20, 30, 55.2)
# print(tomonlar)

# toys = ('bus', 'car', 'bear', 'dino', 'lego', 'lizard')
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])

# toys = ('bus', 'car', 'ber', 'dino', 'lego', 'lizard')
# toys[3] = 'dragon'

#   #   TUPLES <-> LIST
# toys = ('bus', 'car', 'ber', 'dino', 'lego', 'lizard') # o'zgarmas ro'yhat
# toys = list(toys) # o'zgarmas ro'yhatni oddiy ro'yhat (list) ga o'zgartiramiz
# # # Ro'yhatga o'zgartirishlar kiritamiz
# toys.append('dragon')
# toys.remove('bus')
# toys[1] = 'teddy'
# toys = tuple(toys) # ro'yhatni qaytadan o'zgarmas ro'yhat (tuple) ga aylantiramiz
# print(toys)

#   #   #   HOMEWORK    #   #   #

#   # O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
# davlatlar = ['Brazil', 'Russia', 'Canada', 'Japan', 'Germany', 'Argentina']
# print(davlatlar)

#   # Ro'yxatning uzunligini konsolga chiqaring
# print(len(davlatlar))

#   # sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
# print(sorted(davlatlar))

#   # sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
# print(sorted(davlatlar, reverse=True))

#   # Asl ro'yxatni qaytadan konsolga chiqaring
# print(davlatlar)

#   # reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
# davlatlar.reverse()
# print(davlatlar)

#   # sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
# davlatlar.sort()
# print(davlatlar)
# davlatlar.sort(reverse=True)
# print(davlatlar)

#   # 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
# juft_sonlar = list(range(120,1200,2))
# print(juft_sonlar)

#   # Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
# print("Juft sonlar yig'indisi: ", sum(juft_sonlar))

#   # Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
# print("Eng katta - eng kichik =", max(juft_sonlar) - min(juft_sonlar))

#   # Ro'yxatdagi elementlar sonini hisoblang
# print(len(juft_sonlar))

#   # Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
# print(juft_sonlar[0:20])
# print(juft_sonlar[36:56])
# print(juft_sonlar[520:540])

#   # taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
# taomlar = ['chuchvara', 'kasha', 'dimlama', 'moshkichra', 'manti']

#   # nonushta degan yangi ro'yxatga taomlardan nusxa oling
# nonushta = taomlar[:]

#   # Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
# nonushta.remove('manti')
# nonushta.remove('dimlama')
# nonushta.remove('chuchvara')
# nonushta.append('tuxum')
# nonushta.append('sut')

#   # Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
# print(taomlar)
# print(nonushta)

#   # Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
# nonushta = tuple(nonushta)
# nonushta[0] = 'qaymoq va non'