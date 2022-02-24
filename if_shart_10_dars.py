# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 15:53:30 2022

@author: nurot_ricw6a7
"""

cars = ['toyota', 'mazda','hyundai', 'gm','kia']
for car in cars:
    if car != 'gm':
        print(car.title())        
    else:
        print(car.upper())
        

user = input("Foydalanuvchi loginni kiriting: ")
if user.lower() == "admin":
        print(f" Hush kelibsiz, {user.title()}. Foydalanuvchilar ro'yxatini ko'rasizmi? ")
else:
    print(f"Hush kelibsiz, {user.title()}")
       
a = input("1-sonni kiriting: ")    
b = input("2-sonni kiriting: ")
if a == b:
    print("Sonlar teng")
else:
    print("Sonlar turlicha")
    
c = float(input("Istalgan son kiriting: "))
if c > 0:
    print("Son musbat")
else:
    print("Son manfiy")

d = float(input("Istalgan son kiriting: "))
if d > 0:
    print(d**(1/2))
else:
    print("Musbat son kiriting.")
        