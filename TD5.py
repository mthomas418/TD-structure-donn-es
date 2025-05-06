import tkinter as tk

## Exo 1
mot = 'HUHHDUH'

def read_word(canvas, mot, h, w, x0 = 0 , y0 = 50, couleur = 'black') :
    x1, y1 = 0,0
    for letter in mot :
        if letter == 'H' :
            x1,y1 = x0 + h , y0
        elif letter == 'U' :
            x1, y1 = x0 + h, y0 - w
        elif letter == 'D' :
            x1, y1 = x0 + h, y0 + w
        canvas.create_line(x0,y0,x1,y1, fill = couleur)
        x0, y0 = x1, y1

# root = tk.Tk()
# can = tk.Canvas(root, width = 100, height = 200, bg='white')
# can.grid()
# read_word(can,mot, 10, 10)
# root.mainloop()

## Exo 2 et suite
def mot_croisement(croisement, nb_fils) :
    liste_mots = ['H' for _ in range(nb_fils)]
    ordre_fils = list(range(nb_fils))
    for noeud in croisement :
        for i in range(nb_fils) :
            fil_actuel = ordre_fils[i]
            if i == noeud :
                liste_mots[fil_actuel] += 'DH'
            elif i == noeud + 1 :
                liste_mots[fil_actuel] += 'UH'
            else :
                liste_mots[fil_actuel] += 'HH'
        ordre_fils[noeud], ordre_fils[noeud+1] = ordre_fils[noeud+1], ordre_fils[noeud]
    return liste_mots

tableau = [2,1,1,0,2]
nb_fils = 4
list_motb = mot_croisement(tableau, nb_fils)
color = ['blue','red','green','yellow']

mot_longueur = len(list_motb[0])  # mÃªme longueur pour tous les mots
canvas_largeur = 600
canvas_hauteur = 300
largeur_horiz= canvas_largeur / mot_longueur       # largeur horizontale par pas
intervalle = canvas_hauteur / (nb_fils + 1)
w = intervalle                 # amplitude des montÃ©es / descentes

root = tk.Tk()
canva = tk.Canvas(root, width=canvas_largeur, height=canvas_hauteur, bg='white')
canva.grid(row=0, column=0, columnspan=2)
    
def dessin(canvas, list_mots, h, w, couleur, y0, intervalle) :
     canvas.delete("all")
     for i in range(len(list_mots)) :
         y0i = y0 + i * intervalle
         read_word(canvas, list_mots[i], h, w, y0=y0i, couleur=couleur[i])
         
dessin(canva, list_motb, largeur_horiz, w, color, y0=intervalle, intervalle=intervalle)

def f_bouton1() :
    root.destroy()

def f_bouton2() :
    global color
    color = [color[-1]] + color[:-1]
    dessin(canva, list_motb, largeur_horiz, w, color, y0=intervalle, intervalle=intervalle)



btn1 = tk.Button(root, text='Quitter', command=f_bouton1)
btn2 = tk.Button(root, text='Couleurs', command=f_bouton2)

btn1.grid(row=2, column=0)
btn2.grid(row=2, column=1)

label_croisement = tk.Label(root, text= f"Croisements : {tableau}")
label_croisement.grid(row=1, column=0, columnspan=2)

root.mainloop()

