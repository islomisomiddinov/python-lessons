# 09-DARS. FOR LOOP (SIKLI)
# 09.12.2021

# mehmonlar = ['Abror', 'Bobur', 'Fazliddin', 'Doniyor', 'Jasur']
# for mehmon in mehmonlar:
#     print('Salom', mehmon)
    
# mehmonlar = ['Jasur', 'Abror', 'Bobur', 'Anvar', 'Axror']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20-dekabr kuni nahorga oshga taklif qilamiz")
#     print("Hurmat bilan Isayevlar oilasi!")
    
# mehmonlar = ['Jasur', 'Abror', 'Bobur', 'Anvar', 'Axror']
# for mehmon in mehmonlar:
#     print(mehmon)
    
    
    
#     print(mehmonlar) # bu qator ham sikl ichkarisi hisoblanadi

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng.")
    
# sonlar = list(range(11)) # 0 dan 10 gacha sonlar ro'yhatini yaratamiz
# sonlar_kvadrati = [] # bo'sh ro'yhat yaratamiz
# for son in sonlar:
#     sonlar_kvadrati.append(son**2) # sonning kvadratini hisoblab, sonlar_kvadrati ro'yhatiga yuklaymiz
    
# print(sonlar)
# print(sonlar_kvadrati)

# dostlar = [] # bo'sh ro'yhat 
# print("5 ta eng yaqin do'stingiz kimlar?")
# for n in range(5): # n bu yerda 0 dan 4 gacha qiymat oladi
#     dostlar.append(input(f"{n+1}-do'stingizni yozing:"))
# print(dostlar)

#   # Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# ismlar = ['Usmon', 'Axror', 'Iqbol', 'Laziz', 'Erkin']
# for ism in ismlar:
#     print(f"{ism}, siz kim bo'lib ishlaysiz?")

#   # Yuqoridagi sikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring (n o'rniga kod necha marta takrorlanganini yozing)
# print(f"Kod {len(ismlar)} marta takrorlandi.")

#   # 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
# toq_sonlar = list(range(11,100,2))
# print(toq_sonlar)
# for son in toq_sonlar:
#     print(f"{son} ning kubi: {son**3}")

#   # Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
# kinolar = []
# print("5 ta eng yoqtirgan kinolaringiz nomini kiriting!")
# for kino in range(5):
#     kinolar.append(input(f"{kino+1}-kino nomi: ").upper())
# print(kinolar)
    
#   # Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
# people = int(input("Bugun nechta odam bilan suhbatlashdingiz?\n>>>"))
# ismlar = []
# for p in range(people):
#     ismlar.append(input(f"{p+1}-odamning ismi nima?\n>").title())
# print(ismlar)

