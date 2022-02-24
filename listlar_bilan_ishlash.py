# -*- coding: utf-8 -*-
"""
Created on Thu Feb 10 08:28:50 2022

@author: nurot_ricw6a7
"""

davlatlar = ["Singapur", "Malayziya", "Avstraliya", "Germaniya","AQSh"]
print(davlatlar)
print("Davlatlar ro'yxatining uzunligi: ",len(davlatlar))
print(sorted(davlatlar))
print(sorted(davlatlar,reverse = True))
print(davlatlar)
davlatlar.reverse()
print(davlatlar)
davlatlar.sort()
print(davlatlar)
davlatlar.sort(reverse=True)
print(davlatlar)
son = list(range(120,1200))
print(son)
print(sum(son))
katta = max(son)
kichik = min(son)
ayirma = katta - kichik
print(ayirma)
print("Elementlar soni: ", len(son))
print(son[:20])
print(son[-20:])
print(son[530:550])
taomlar = ["Manti","Osh","Shashlik","Jiz","Tandir kabob"]
nonushta = taomlar[:]
nonushta.remove("Manti")
del nonushta[0]
nonushta.append("Shirchoy")
nonushta.insert(0, "Quymoq") # 5-o'ringa yangi qiymat qo'shadi
print(f'{taomlar},{nonushta}')
nonushta = tuple(nonushta)
nonushta[0] = "Qaymoq va non"
