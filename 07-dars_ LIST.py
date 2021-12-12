# 07-dars. LIST (RO'YXAT)
# 03/12/2021

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# narxlar = [12000, 18000, 10900, 22000, 25000, 36000, -25, 63.2]
# sonlar = ['bir', 'ikki', 3, 4, 5]  # sonlar va matnlar aralash ro'yxat
# ismlar = []   # Bo'sh ro'yhat

# .append()

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
# mevalar.append('tarvuz')    # mevalar ro'yhatiga tarvuzni qo'shamiz
# print(mevalar)

# .insert

# cars = ['Gentra', 'Nexia 3', 'Cobalt']
# cars.insert(0, 'Malibu')    # 1-o'ringa yangi qiymat qo'shamiz
# print(cars)
# cars.insert(2, 'Damas')    # 3-o'ringa yangi qiymat qo'shamiz
# print(cars)

# del

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# del mevalar[1]  # 2-element (anjir) ni o'chirib tashlaymiz
# print(mevalar)

# .remove

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik", 'anor']
# mevalar.remove('shaftoli')  # ro'yhatdan shaftolini o'chirdik
# print(mevalar)

# hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
# hayvonlar.remove('mushuk')  # Ro'yhatda 2 ta mushuk bor, ulardan 
# birinchisi o'chadi
# print(hayvonlar)

# .pop

# bozorlik = ['yog\'', 'un', 'piyoz', 'banan', "go'sht"]
# mahsulot = bozorlik.pop(3)      # Ro'yhatdan banan ni sug'urib olamiz
# print("Men " + mahsulot + " sotib oldim")
# print("Olinmagan mahsulotlar: ", bozorlik)

    # HOMEWORKS
    
# # ismlar degan ro'yxat yarating va kamida 3 ta yaqin do'stingizning ismini kiriting
# ismlar = ['Vali', 'Sardor', 'Xasan', 'Xusan', 'Bobur', 'Anvar']

# Ro'yxatdagi har bir do'stingizga qisqa xabar yozib konsolga chiqaring:    
# print("Salom ", ismlar[0], " ishlaring yaxshimi?")
# print(ismlar[1] + " kecha futbol qanaqa bo'ldi? " + ismlar[-1] + ' va ' + ismlar[-2] + " ham bordimi o'yinga?")
# print(f"{ismlar[2]} va {ismlar[3]} egizaklar.")

# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik).
# sonlar = [45, 23, 17.2, -38, 71, -19]
# print(sonlar)

# Yuqoridagi ro'yxatdagi sonlar ustida turli arifmetik amallar bajarib ko'ring. Ro'yxatdagi ba'zi sonlarning qiymatini o'zgartiring, ba'zilarini esa almashtiring. 
# sonlar.append(sonlar[0] + sonlar[1])
# sonlar[2] = 53.7
# del sonlar[3]
# sonlar.insert(-1, -19)
# sonlar.remove(-19)
# print(sonlar) 

# t_shaxslarva z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting.
# t_shaxslar = ['Amir Temur', 'Islom Karimov', 'Imom Buxoriy'] 
# z_shaxslar = ['Jeff Bezos', 'Ilon Musk', 'Jack Maa']

# Yuqoridagi ro'yxatlarning har biridan bittadan qiymatni sug'urib olib (.pop()), quyidagi ko'rinishda chiqaring:
# print(f"Men tarixiy shaxslardan {t_shaxslar.pop(1)} bilan, zamonaviy shaxslardan esa {z_shaxslar.pop(1)} bilan uchrashishni istar edim")

# friends nomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting. 
# friends = []
# friends.append('Doniyor')
# friends.append('Bobur')
# friends.append('Asilxan')
# friends.append('Jasur')
# friends.append('Akmal')

# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chirib tashlang.
# friends.remove('Akmal')

# Ro'yxatning oxiriga, boshiga va o'rtasiga yangi ismlar qo'shing.
# friends.insert(0, 'Abror')
# friends.insert(2, 'Baxtiyor')
# friends.insert(6, 'Anvar')

# Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
# mehmonlar = []
# mehmonlar.append(friends.pop(3))
# mehmonlar.append(friends.pop(0))
# mehmonlar.append(friends.pop(2))
# print("Kelgan mehmonlar: ", mehmonlar)