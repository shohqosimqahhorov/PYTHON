# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 08:37:47 2022

@author: nurot_ricw6a7
"""

son = int(input("Biror butun son kiriting: "))

for n in range(2,11):
    if son % n == 0:
        print(f"{n} soni {son} ga qoldiqsiz bo'linadi")