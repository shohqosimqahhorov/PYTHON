# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 08:57:32 2022

@author: nurot_ricw6a7
"""

mahsulot = ["kartoshka", "piyoz", "sabzi", "gosht", "shakar", "paxta yogi", "salat yogi", "non", "sovun", "guruch", "tovuq"]
savat = []
print(" 5 ta mahsulot tanlang.")
for n in range(5):
    savat.append(input(f"{n+1} - mahsulotni kiriting: "))
for food in savat:
    if food in mahsulot:
        print(f"{food} do'konimizda bor")
    else:
         print(f"{food} do'konimizda yo'q")
            
