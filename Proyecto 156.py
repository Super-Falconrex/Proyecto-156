# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 08:50:37 2024

@author: anyta
"""

from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title("juego de cartas smash bros ultimate")
root.geometry("800x700")
root.configure(background = "red")

img1 = ImageTk.PhotoImage(Image.open("Sonic.JPG"))
img2 = ImageTk.PhotoImage(Image.open("Kirby.JPG"))
img3 = ImageTk.PhotoImage(Image.open("Mario.JPG"))
img4 = ImageTk.PhotoImage(Image.open("Bowser.JPG"))
img5 = ImageTk.PhotoImage(Image.open("Donkey Kong.JPG"))
img6 = ImageTk.PhotoImage(Image.open("Rey Dedede.JPG"))
img7 = ImageTk.PhotoImage(Image.open("Meta Knight.jpg"))
img8 = ImageTk.PhotoImage(Image.open("Link.JPG"))
img9 = ImageTk.PhotoImage(Image.open("Samus.JPG"))
img10 = ImageTk.PhotoImage(Image.open("Samus Oscura.JPG"))
img11 = ImageTk.PhotoImage(Image.open("Pikachu.JPG"))
img12 = ImageTk.PhotoImage(Image.open("Luigi.JPG"))

player1 = Label(root, text= "jugador1", bg = "blue", fg = "green")
player2 = Label(root, text= "jugador2", bg = "blue", fg = "yellow")

score1 = Label(root, bg = "purple", fg = "orange")
score2 = Label(root, bg = "purple", fg = "brown")

randomN = Label(root, bg = "goldenrod", fg = "silver")

player1.place(relx = 0.1, rely = 0.3, anchor = CENTER)
player2.place(relx = 0.9, rely = 0.3, anchor = CENTER)



score1.place(relx = 0.1, rely = 0.4, anchor = CENTER)
score2.place(relx = 0.9, rely = 0.4, anchor = CENTER)


randomN.place(relx = 0.5, rely = 0.5, anchor = CENTER)

lista_smasher = [img1, img2, img3, img4, img5,img6,img7,img8,img9,img10,img11,img12]
lista_poder = [100, 95, 90, 60, 50, 60, 80, 85, 50, 55, 60, 80]

imagen = Label(root)

player1_score = 0
player2_score = 0

def Jugador1():
    global player1_score
    numero_aleatorio = random.randint(0,11)
    lista_jugador = lista_smasher[numero_aleatorio]
    
    imagen["image"] = lista_jugador
    
    lista_super = lista_poder[numero_aleatorio]
    
    player1_score = player1_score + lista_super
    
    score1["text"] = str(player1_score)
    
def Jugador2():
    global player2_score
    numero_aleatorio = random.randint(0,11)
    lista_jugador = lista_smasher[numero_aleatorio]
        
    imagen["image"] = lista_jugador
        
    lista_super = lista_poder[numero_aleatorio]
        
    player2_score = player2_score + lista_super
        
    score2["text"] = str(player2_score)
    
btn = Button(root, command = Jugador1)

btn2 = Button(root, command = Jugador2)

imagen.place(relx=0.5, rely=0.5, anchor=CENTER)

btn.place(relx=0.1, rely=0.6, anchor=CENTER)

btn2.place(relx=0.9, rely=0.6, anchor=CENTER)

root.mainloop()