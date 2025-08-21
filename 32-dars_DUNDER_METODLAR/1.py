#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 19 09:17:48 2025

@author: islomisomiddinov
"""

class Avto:
    """Avtomobil klassi"""
    __num_avto = 0
    def __init__(self, make, model, rang, yil, narx):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narx = narx
        Avto.__num_avto += 1
        
    # def __str__(self):
    #     return f"Avtomobil: {self.make} {self.model}"
    
    def __repr__(self):
        return f"Avtomobil: {self.make} {self.model}"
    
    def __eq__(self, y):
        return self.narx == y.narx
    
    def __lt__(self, y):
        return self.narx<y.narx
    
    def __le__(self, y):
        return self.narx<=y.narx
        
avto1 = Avto('Toyota', "Camry", "oq", 2020, 45000)
avto2 = Avto("Chevrolet", "Cobalt", "oq", 2025, 13000)
# print(avto1)



class Autosalon:
    """Avtosalon klassi"""
    def __init__(self, name):
        self.name = name
        self.autolar = []
        
    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def __len__(self):
        return len(self.autolar)
    
    def __getitem__(self, index):
        return self.autolar[index]
    
    def __setitem__(self, index, value):
        self.autolar[index] = value
        
    def __call__(self, *value):
        if value:
            for auto in value:
                self.add_auto(auto)
        else:
            return [auto for auto in self.autolar]
        
    def __add__(self, y):
        if isinstance(y, Autosalon):
            yangi_autosalon = Autosalon(f"{self.name} {y.name}")
            yangi_autosalon.autolar = self.autolar + y.autolar
            return yangi_autosalon
        elif isinstance(y, Avto):
            self.add_auto(y)
    
    def add_auto(self, *values):
        for auto in values:
            if isinstance(auto, Avto):
                self.autolar.append(auto)
            else:
                print("Avtomobil qo'shing")
                

    
salon1 = Autosalon("Driver's Village")
salon2 = Autosalon("Auto Lider")

auto1 = Avto('Honda', "Accord", "silver", 2015, 23000)
auto2 = Avto("Volkswagen", "Passat", "qora", 2023, 34000)
auto3 = Avto('Mazda', '7', "qizil", 2019, 39000)
salon1.add_auto(auto1, auto2, auto3)

# print(salon1[0])

salon1[2] = Avto('Xiaomi', "Su7 Max", "Diamond Black", 2025, 42000)

# print(salon1())

auto4 = Avto('Tesla', "Y", 'blue', 2024, 45000)
auto5 = Avto('BMW', "X7", 'qora', 2024, 70000)
salon2(auto4, auto5)

salon3 = salon1+salon2
# print(salon3)