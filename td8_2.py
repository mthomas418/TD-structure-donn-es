# -*- coding: utf-8 -*-
"""
Created on Wed May 21 09:51:17 2025

@author: Thoma
"""

import struct


def extraire_echantillons(fichier):
    with open(fichier, 'rb') as f:
        f.seek(44)  # On saute l'en-tête standard (44 octets pour un WAV PCM simple)
        donnees = f.read()  # On lit tout le reste (les données audio)

    nb_echantillons = len(donnees) // 2
    echantillons = struct.unpack('<' + 'h' * nb_echantillons, donnees)
    gauche=echantillons[::2]
    droite=echantillons[1::2]
    return gauche, droite


    
g,d =extraire_echantillons("the_wall.wav")

print ("premiers échantillons de gauche", g[:10])
print ("premiers échantillons de droite", d[:10])
print ("taille de l'echantillon par canal", len(g))



def ecrire_wav(fichier, g, d):
    with open(fichier, "wb") as f:
        nb_canaux = 2
        bit_echantillon = 16
        nb_echantillon = len(g)
        taille_donnee = nb_echantillon * nb_canaux * 2  # 2 octets par échantillon

        # Écriture de l'entête
        f.write(b"RIFF")
        f.write(struct.pack("<I", 36 + taille_donnee))  # taille totale - 8
        f.write(b"WAVE")

        f.write(b"fmt ")
        f.write(struct.pack("<IHHIIHH", 16, 1, nb_canaux, 44100,
                            44100 * nb_canaux * 2, nb_canaux * 2, bit_echantillon))

        f.write(b"data")
        f.write(struct.pack("<I", taille_donnee))

        # Écriture des échantillons (stéréo)
        for i in range(nb_echantillon):
            f.write(struct.pack("<hh", g[i], d[i]))  # g = gauche, d = droite


g, d = extraire_echantillons("the_wall.wav")
ecrire_wav("copie.wav", g, d)



def speed2(channel):
    return [channel[2*i] for i in range (len(channel)//2)]


g2 = speed2(g)
d2 = speed2(d)

ecrire_wav("the_wall_speed2.wav", g2, d2)






        
        


