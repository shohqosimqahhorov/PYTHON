# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 15:45:41 2022

@author: nurot_ricw6a7
"""

mahsulot = ["osh", "olma", "olxori", "sabzi", "karam", "shakar", "gosht", "pepsi", "kola", "manti"]
savat = []
bor_mahsulotlar = []
mavjud_emas = []
for n in range(5):
    savat.append(input(f"{n+1} - mahsulotni kiriting: "))
for food in savat:
    if food in mahsulot:
        bor_mahsulotlar.append(food)
    else:
        mavjud_emas.append(food)
if len(bor_mahsulotlar) != 0:
    print(f"{bor_mahsulotlar} mahsulotlari do'konimizda bor.")
else:
    print("Siz so'ragan birorta mahsulot do'konimizda yo'q")
if len(mavjud_emas) != 0:
    print(f" {mavjud_emas} mahsulotlari do'konimizda yo'q")
else:
    print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

    





        