# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 23:36:51 2017

@author: Charles
"""

import Tkinter as tk
from PIL import ImageTk, Image

# Faire une liste des photos à importer
photos = ["./Images/xfiles.jpg",
          "./Images/Coop_twinpeaks.png",
          "./Images/2001.jpg",
          "./Images/perruche.jpg",
          "./Images/RAFspitfire.jpg",
          ]

def update_pic(n):
    """
    Cette fonction met à jour la figure quand le slider bouge
    """
    path = photos[int(n)] # Décide quelle figure afficher selon la valeur du slider
    #Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
    image = Image.open(path)
    image.thumbnail(maxsize, Image.ANTIALIAS) # Réduit la taille de la figure
    pic = ImageTk.PhotoImage(image) # Converti la figure en objet pour tkinter
    pic_panel.configure(image=pic) # Met à jour la figure
    pic_panel.image = pic # Met à jour la figure
    pic_label.configure(text=path) # Met à jour le titre de la figure
    print path 

#This creates the main window of an application
window = tk.Tk()
window.title("Application utile")
#window.geometry("1024x768") # Tu peux décider des dimensions de la fenêtre si tu veux les fixer
#window.configure(background='black') # Tu peux changer la couleur du background avec ça

# Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
image = Image.open(photos[0]) # Utiliser la première photo dans la liste pour initialiser la fenêtre
maxsize = (800, 600) # Sert à réduire la taille de la figure pour qu'elle rentre dans le panneau
image.thumbnail(maxsize, Image.ANTIALIAS) # Réduit la taille de la figure
pic = ImageTk.PhotoImage(image) # Converti la figure en objet pour tkinter

# The Label widget is a standard Tkinter widget used to display a text or image on the screen.
# Faire un panneau pour mettre la figure dedans
pic_panel = tk.Label(window, width=800, height=600, image = pic) 
# Faire un panneau pour écrire le titre de la figure
pic_label = tk.Label(window, text=photos[0])
# Faire le slider
slider = tk.Scale(window, from_=0, to=len(photos)-1, length=500, 
                  orient=tk.HORIZONTAL, command=update_pic) # command passe la valeur du slider à la fonctin update_pic par défault

# The grid geometry manager places widgets in rows or columns.
# Placer les panneau à bonne place
pic_panel.grid(row=0, column=0)
pic_label.grid(row=1, column=0)
slider.grid(row=2, column=0) # Placer le slider à bonne place

#Start the GUI
window.mainloop()
