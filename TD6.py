# -*- coding: utf-8 -*-
"""
Created on Wed May  7 09:47:57 2025

@author: Thoma
"""

import tkinter as tk
import random

MAX_FILS = 6
MAX_CROISEMENTS = 10


class Data :
    def __init__(self, croisement, nb_fils):
        self.croisement=croisement
        self.nb_fils=nb_fils
        
    def mot_croisement(self):
    
        liste_mots = ['H' for _ in range(self.nb_fils)] 
        ordre_fils = list(range(self.nb_fils)) 
        for noeud in self.croisement: 
            for i in range(self.nb_fils): 
                fil_actuel = ordre_fils[i] 
                if i == noeud: 
                    liste_mots[fil_actuel] += 'DH' 
                elif i == noeud + 1: 
                    liste_mots[fil_actuel] += 'UH' 
                else: 
                    liste_mots[fil_actuel] += 'HH' 
            ordre_fils[noeud], ordre_fils[noeud+1] = ordre_fils[noeud+1], ordre_fils[noeud] 
        return liste_mots
    
    def reidemeister(self):
        if len(self.croisement) >= 2:
            a, b = self.croisement[0], self.croisement[1]
        if a == b:
            # Vérifie que les deux croisements se suivent et sont sur les mêmes fils
            self.croisement = self.croisement[2:]  # Supprimer les deux

    

### Partie graphique 
class App:
    def __init__(self):
        # Données
        self.data=Data(croisement=[2,1,1,0,2], nb_fils=4)
        self.color = ['blue', 'red', 'green', 'yellow']
        self.list_mots = self.data.mot_croisement()
        # Dimensions
        self.canvas_largeur = 600
        self.canvas_hauteur = 300
        self.mot_longueur = len(self.list_mots[0])
        self.largeur_horiz = self.canvas_largeur / self.mot_longueur      #pas horizontal
        self.intervalle = self.canvas_hauteur / (self.data.nb_fils + 1)        
        self.w = self.intervalle                                          #pas vertical

        # Tkinter setup
        self.root = tk.Tk()
        self.root.title("Entrelacs - classe App")

        self.canvas = tk.Canvas(self.root, width=self.canvas_largeur, height=self.canvas_hauteur, bg='white')
        self.canvas.grid(row=0, column=0, columnspan=2)

        self.label = tk.Label(self.root, text=f"Croisements : {self.data.croisement}")
        self.label.grid(row=1, column=0, columnspan=2)

        self.btn_quit = tk.Button(self.root, text='Quitter', command=self.root.destroy)
        self.btn_quit.grid(row=2, column=0)

        self.btn_colors = tk.Button(self.root, text='Changer Couleurs', command=self.rotate_colors)
        self.btn_colors.grid(row=2, column=1)
        
        self.btn_tirerfil= tk.Button(self.root, text='tirer au hasard un entrelac', command=self.tirer_entrelac)
        self.btn_tirerfil.grid(row=2, column=2)

        self.redraw()  # Premier dessin

    def read_word(self, canvas, mot, h, w, x0=0, y0=50, couleur='black'):
        x1, y1 = 0, 0
        for letter in mot:
            if letter == 'H':
                x1, y1 = x0 + h, y0
            elif letter == 'U':
                x1, y1 = x0 + h, y0 - w
            elif letter == 'D':
                x1, y1 = x0 + h, y0 + w
            canvas.create_line(x0, y0, x1, y1, fill=couleur)
            x0, y0 = x1, y1


    def redraw(self):
        self.canvas.delete("all")
        for i, mot in enumerate(self.list_mots):
           y0 = self.intervalle + i * self.intervalle
           self.read_word(self.canvas, mot, self.largeur_horiz, self.w, y0=y0, couleur=self.color[i])



    def rotate_colors(self):
        self.color = [self.color[-1]] + self.color[:-1]
        self.redraw()
        
    def tirer_entrelac(self): 
        
        nb_fils=random.randint(2, MAX_FILS)
        nb_croisement=random.randint(1, MAX_CROISEMENTS)
        croisement=[random.randint(0, nb_fils-2) for _ in range (nb_croisement)]
        self.data = Data(croisement, nb_fils)
        self.list_mots = self.data.mot_croisement()
        self.color = ['red', 'green', 'blue', 'orange', 'purple', 'brown'][:nb_fils]
        self.mot_longueur = len(self.list_mots[0])
        self.largeur_horiz = self.canvas_largeur / len(croisement)
        self.intervalle = self.canvas_hauteur / (nb_fils+1)
        self.w = self.intervalle

        self.label.config(text=f"Croisements : {croisement}")
        self.redraw()
        
        

    def run_forever(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = App()
    app.run_forever()
