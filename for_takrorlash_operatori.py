# -*- coding: utf-8 -*-
"""
Created on Thu Feb 17 11:07:04 2022

@author: nurot_ricw6a7
"""

ismlar = ["Sanjar","Jaur","Mirjalol","Bobur","Sadin"]
for ism in ismlar:
    print(f'Assalomu alaykum {ism}')
print(f'Kod {len(ismlar)} marta takrorlandi ')

toq_sonlar = list(range(11,100,2))
for son in toq_sonlar:
    print(f'{son} ning kubi {son**3} ga teng ')

kinolar = []
print("5ta eneg yaxshi ko'rgan filmingizni kiriting") 
for n in range(5):
    kinolar.append(input(f"{n+1} - eng yaxshi ko'rgan filmingiz: "))  
print(kinolar)    

odamlar = []
soni = (int(input("Bugun nechta inson bilan uchrashdingiz: ")))
for n in range(soni):
    odamlar.append(input(f'{n+1} - uchrashgan insoningizning ismi: '))
print(f"Siz bugun jami {soni} ta inson bilan ya'ni {odamlar}lar bilan uchrashgansiz.")    

