# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 12:16:58 2022

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
word = lugat.get(input("Biror so'z kiriting:"),"Bunday ma'lumot mavjud emas")
print(f"{word}")