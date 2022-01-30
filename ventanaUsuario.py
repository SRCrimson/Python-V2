from cgitb import text
import os
from random import uniform
import tkinter as tk
from tkinter import messagebox
from tkinter import *


window = tk.Tk()
window.title("Calabozos en la Nacho") #Zona 0
window.resizable(width=False, height=False)
###Frames de ventana
frame1 = tk.Frame(window, background="#566573", bd=1, relief="sunken",width=985, height=625)
frame1.grid(sticky="nsew", padx=0, pady=0)
frame2 = tk.Frame(frame1, background="#CCE4CA", width=500, height=600)
frame2.grid(row=3, column=3,padx=2, pady=1)
'''label = Label(frame2)
imgobj = PhotoImage(file='uiMain/photos/unal3.png') # definir imagen
label['image'] = imgobj'''
##frame de menu procesos y consultas



##Funciones de menu
mensajeAplicacion='''La aplicación es un demo jugable que rememora a los clásicos juegos de rol de texto, para ello implementaremos los conceptos de la programación orientada a objetos vistos en clase. Se desarrollará la narración en un clásico ecosistema de fantasía medieval, inspirado en el juego Calabozos & Dragones.'''
def evento():
    pass
def Aplicacion():
    messagebox.showinfo(title='Aplicación',
    message='Informacion Basica',
    detail=mensajeAplicacion)
def regresarInicio():
    frame1.grid()
def procesos():
    frame1.grid_forget()

def ayuda():
    messagebox.showinfo(title='Ayuda',
    message='Autores',
    detail='''Brayan David Caballero Fernández\nJohn Mauricio Mesa Echeverri\nEider Alejandro Peña Dagua\nSantiago Rivera Mejía''')


###botones de menu zona 1 en rojo
window.option_add('*tearOff', FALSE)
menubar = Menu(window)
window.config(menu=menubar)
menuArchivo= Menu(menubar)
menubar.add_cascade(menu=menuArchivo, label='Archivo', command=evento)
menuArchivo.add_command(label="Aplicación", command=Aplicacion)
menuArchivo.add_separator()
menuArchivo.add_command(label="Salir", command=regresarInicio)
menuProcesos= Menu(menubar)
menubar.add_cascade(menu=menuProcesos, label='Procesos y Consultas')
menuProcesos.add_command(label="Inventario", command=procesos)
menuProcesos.add_command(label="Combate", command=procesos)
menuProcesos.add_command(label="Narrador", command=procesos)
menuProcesos.add_command(label="Tienda", command=procesos)
menuProcesos.add_command(label="Crear Personaje", command=procesos)

menuAyuda=Menu(menubar)
menubar.add_cascade(menu=menuAyuda,label="Ayuda")
menuAyuda.add_checkbutton(label="ayuda",command=ayuda)
window['menu'] = menubar



window.mainloop()