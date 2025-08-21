#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 20 13:14:07 2025

@author: islomisomiddinov
"""

class Student:
    def __init__(self, ism, familiya, tyil, idraqam, bosqich):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
        self.idraqam = idraqam
        self.bosqich = bosqich
        
    def __repr__(self):
        return f"{self.ism} {self.familiya}"


class Fan:
    def __init__(self, name, muddat):
        self.name = name
        self.muddat = muddat
        self.students = []
        
    def __repr__(self):
        return f"{self.name} fani"
    
    def __call__(self, *values):
        return [student for student in self.students]
    
    def __len__(self):
        return len(self.students)
    
    def __getitem__(self, index):
        return self.students[index]
    
    def __setitem__(self, index, value):
        self.students[index] = value
        
    def __add__(self, x):
        if isinstance(x, Student):
            self.students.append(x)
        
        
    def add_student(self, *students):
        for student in students:
            if isinstance(student, Student):
                self.students.append(student)
            else:
                print("Bu fan faqat shu universitet talabalari uchun")
                
    def __sub__(self, x):
        x.idraqam.remove()
                    
                    
fan1 = Fan('Tarix', 2)
fan2 = Fan('Oliy matematika', 4)

student1 = Student('Umar', 'Fayziyev', 2001, "N3332211", 3)
student2 = Student('Lobar', "Ikromova", 2004, "B7770099", 2)
student3 = Student("Yulduz", "Ravshanova", 2006, "B2224455", 1)
student4 = Student("Qudrat", "Imomov", 1997, "N5553311", 4)



fan1.add_student(student1)
# print(fan1.students)
fan2.add_student(student2, student3, student4)
# print(fan2.__len__())
# print(len(fan2))
# print(fan2[:])

student5 = Student('Charos', "Tillayeva", 2005, "B0004477", 2)
fan1.__add__(student5)
# print(fan1[:])