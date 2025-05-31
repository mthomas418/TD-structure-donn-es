# -*- coding: utf-8 -*-
"""
Created on Wed Mar 26 09:48:22 2025

@author: Thoma
"""

lexique=[]
f=open("C:\\Users\\Thoma\\frenchssaccent.dic","r")
for ligne in f :
    lexique.append(ligne[0:len(ligne)-1]) 
f.close()


tirage=['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']


mot_plus_long = ""

for mot in lexique:
    lettres_disponibles=list(tirage)
    mot_valide=True
    
    for lettre in mot:
        if lettre in lettres_disponibles:
            lettres_disponibles.remove(lettre)
        else:
            mot_valide=False
            break
    if mot_valide and len(mot)>=len(mot_plus_long):
        mot_plus_long=mot

print()


dic={'a':1, 'e':1, 'i':1, 'l':1, 'n':1, 'o':1, 'r':1,'s':1,'t':1, 'u':1, 'd':2,'g':2,'m':2,'b':3,'c':3, 'p':3, 'f':4, 'h':4, 'v':4, 'j':8, 'q':8, 'k':10, 'w':10,'y':10,'z':10}
