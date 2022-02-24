# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

yosh = int(input("Yoshingiz nechada: "))
if yosh <= 4 or yosh >= 60:
    narx = 0
elif yosh < 18:
    narx = 10000
else:
    narx = 20000
print(f"Siz uchun kirish {narx} so'm")