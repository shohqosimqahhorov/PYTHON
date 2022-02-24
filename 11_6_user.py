# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 08:25:18 2022

@author: nurot_ricw6a7
"""

foydalanuvchilar = ["aziznur","sobiruz", "tezru", "alipo", "salom"]

user = input("Yangi login tanlang. ")
if user.lower() in foydalanuvchilar:
    print("Login band. Iltimos boshqa login tanlang.")
else:
    print("Hush kelibsiz foydalanuvchi.")

    