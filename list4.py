# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 17:26:41 2022

@author: nurot_ricw6a7
"""

friends = []
friends.append("Sanjar")
friends.append("Ma'ruf")
friends.append("Jasur")
friends.append("Bobur")
friends.append("Sadin")
friends.append("Sherzod")
friends.remove("Bobur")
friends.remove("Sadin")
del friends[-1]
friends.insert(0, "Mirjalol")
friends.insert(2, "Umid aka")
friends.insert(-1, "Alisher")
mehmonlar = []
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(-2))
mehmonlar.append(friends.pop(0))
print("\nKelgan mehmonlar:", mehmonlar)
