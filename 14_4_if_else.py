# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 21:37:42 2022

@author: nurot_ricw6a7
"""

lugat = {
    "integer" : "butun son", 
    "float" : "o'nlik son",
    "string" : "matn", 
    "for" : "sikl operatori",
    "if" : "shart operatori",
    "print" : "natijani konsolga chiqarish",
    "input" : "ma'lumot kiritish",
    "list" : "ro'yxat",
    "tuple" : "o'zgarmas ro'yxat",
    "dict" : "lug'at"    
    }

tarjima = lugat.get(input("Biror so'z kiriting: ").lower())
if tarjima == None:
    print("Bunday so'z mavjud emas.")
else:
    print(f"{tarjima}")
    