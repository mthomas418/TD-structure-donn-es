# -*- coding: utf-8 -*-
"""
Created on Wed May 14 09:48:13 2025

@author: Thoma
"""
from math import *
import tkinter as tk
import numpy as np
import random
WIDTH, HEIGHT=800,600


graph = [[2, 7, 3], [3, 4, 9, 10], [5, 8, 0], [10, 1, 4, 6, 0], 
[3, 1, 6], [2], [3, 10, 4], [0], [2], [10, 1], [3, 1, 6, 9]]

pos = np.array([(random.random()*(WIDTH), random.random()*(HEIGHT)) for i in range(len(graph))])

vit = np.array([((random.random()-0.5)*10, (random.random()-0.5)*10) for i in range(len(graph))])


fenetre=tk.Tk()
fenetre.title('Dessin du graphe')

canva=tk.Canvas(fenetre, width=WIDTH, height=HEIGHT, bg='grey')
canva.grid(column=0, row=0)


def draw(can, graph, pos):
    can.delete(tk.ALL)
    for i in range(len(graph)):
        for j in graph[i]:  # sucs de i a j
            can.create_line(pos[i][0], pos[i][1], pos[j][0], pos[j][1])
    for (x, y) in pos:
        can.create_oval(x-4,y-4,x+4,y+4,fill="#f3e1d4")
        
        
def ressort (s,t):
    l0=random.uniform(10,100)
    k=0.05
    vec=pos[t]-pos[s]
    l=(vec[0]**2+vec[1]**2)**0.5
    direction=vec/l
    force=k*(l-l0)*direction
    return force


    
    
    
def force(g,s):
    force=np.zeros_like(pos)
    for j in graph[s]:
        force[s]=force[s]+ressort(s,j)
    return force[s]

def next(g, pos, vit):
    for i in range (len(g)):
        f=force(g,i)
        vit[i]=vit[i]+f*0.15
        pos=pos+vit*0.15
    draw(canva, g, pos)


btn_quit=tk.Button(fenetre, text='Quitter', command=fenetre.destroy, bg='red')
btn_quit.grid(row=1, column=0, columnspan=2)
fenetre.bind("<f>", lambda e : next(graph, pos, vit))
draw(canva, graph, pos)

fenetre.mainloop()



