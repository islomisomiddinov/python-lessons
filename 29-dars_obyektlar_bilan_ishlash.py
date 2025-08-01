#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 29 16:17:18 2025

@author: islomisomiddinov
"""

class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.bosqich = 1
        
    def set_bosqich(self, yangi_bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = yangi_bosqich
        
    def update_bosqich(self):
        """Talabaning bosqichini 1taga ko'paytirish"""
        self.bosqich += 1
        
    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi"
    
    def get_name(self):
        return self.ism
    
    def get_lastname(self):
        return self.familiya
    
    def get_fullname(self):
        return f"{self.ism} {self.familiya}"
        
    
    
    ### Obyektlar o'rtasida munosabatlar
    
class Fan():
    """Fan nomli klass"""
    def __init__(self, nomi):
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []
  
    def add_student(self,talaba):
        """Fanga talabalar qo'shish"""
        self.talabalar.append(talaba)
        self.talabalar_soni += 1
        
        
        # Bir qatorda ro'yxat yaratish
        
    def get_students(self):
        """Fanga yozilgan talabalar haqida ma'lumot"""
        return [talaba.get_fullname() for talaba in self.talabalar]
    
    
    
        # METODLARNI FILTRLASH
        
# def see_methods(klass):
#     return [method for method in dir(klass) if not method.startswith('__')]

                # OR
                
# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]
    

    
matematika = Fan("Oliy matematika")
talaba1 = Talaba('Olim', 'Saidov', 1998)
talaba2 = Talaba('Fazliddin', 'Xusanov', 1996)
talaba3 = Talaba('Umida', 'Yunusova', 2001)
matematika.add_student(talaba1)
matematika.add_student(talaba2)
matematika.add_student(talaba3)





            # AMALIYOT
        
            
        # AVTO KLASS ini yaratamiz
            
class Avto:
    def __init__(self, model, rang, korobka, narx):
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narx = narx
        self.km = 0
    
    def get_model(self):
        return self.model
    
    def get_color(self):
        return self.color
    
    def get_korobka(self):
        return self.korobka
    
    def get_price(self):
        return self.narx
    
    def get_info(self):
        return f"{self.rang} {self.model.title()}, {self.korobka} korobka, \
narxi {self.narx}$, yurgan kilometri {self.km} km"

    def set_km(self, yurgan_km):
        self.km = yurgan_km
        
    def update_km(self, son):
        self.km += int(son)
        
        
        
        # AVTOSALON KLASS ini YARATAMIZ
        
        
class Avtosalon:
    def __init__(self, salon_nomi, manzili):
        self.salon_nomi = salon_nomi
        self.manzili = manzili
        self.sotuvdagi_avtolar = []
        self.avtolar_sigimi = 100
        self.avtolar_soni = 0
        
    def add_cars(self, avto):
        self.sotuvdagi_avtolar.append(avto)
        self.avtolar_sigimi -= 10
        self.avtolar_soni += 10
        
    def get_cars_num(self):
        return self.avtolar_soni
        
    def get_place_num(self):
        return self.avtolar_sigimi
    
    def get_cars_info(self):
        return [avto.get_info() for avto in self.sotuvdagi_avtolar]
    
    def get_cars(self):
        return [avto.get_model() for avto in self.sotuvdagi_avtolar]
    
    
salon1 = Avtosalon('Driver\'s Village', "Toshkent shahri")
avto1 = Avto("Kia K8", "qora", "avtomat", 38000)
avto2 = Avto("Kia Sonet", "oq", "avtomat", 18000)
avto3 = Avto("Kia Seltos", "qora", "avtomat", 31000)
salon1.add_cars(avto1)
salon1.add_cars(avto2)
salon1.add_cars(avto3)


def see_methods(klass):
    return [method for method in dir(klass) if not method.startswith('__')]

# print(dir(Avtosalon))
print(salon1.__dict__)