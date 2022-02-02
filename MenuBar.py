import tkinter as tk
from tkinter import *
from tkinter import ttk,messagebox
import gestorAplicacion.mecanicas.Narrador as narrador

mensajeAplicacion='''La aplicación es un demo jugable que rememora a los clásicos juegos de rol de texto, para ello implementaremos los conceptos de la programación orientada a objetos vistos en clase. Se desarrollará la narración en un clásico ecosistema de fantasía medieval, inspirado en el juego Calabozos & Dragones.'''
def Aplicacion():
    messagebox.showinfo(title='Aplicación',
    message='Informacion Basica',
    detail=mensajeAplicacion)

def ayuda():
    messagebox.showinfo(title='Ayuda',
    message='Autores',
    detail='''Brayan David Caballero Fernández\nJohn Mauricio Mesa Echeverri\nEider Alejandro Peña Dagua\nSantiago Rivera Mejía''')


class MenuBar(tk.Menu):
    def __init__(self, container,frameinicio,frameinv,frameCom,frameNarr,frametienda,framecrear, combate, label, frame6, mob, labelMob):
        
        super().__init__(container)
        #definir frames

        self.frameinicio=frameinicio
        self.frameinv=frameinv
        self.frameCom=frameCom
        self.frameNarr=frameNarr
        self.frametienda=frametienda
        self.framecrear=framecrear
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        # Chambonada para combate
        self.combate = combate
        self.label = label
        self.frame6 = frame6
        self.mob = mob
        self.labelMob = labelMob
        #self.countdown = countdown
        self.__create_widgets()

    def __create_widgets(self):
        tk.Menu.__init__(self)
        menuArchivo = tk.Menu(self, tearoff=False)
        self.add_cascade(menu=menuArchivo,label='Archivo')
        menuArchivo.add_command(label="Aplicación", command=Aplicacion)
        menuArchivo.add_command(label="Salir", command=self.regresarInicio)
        menuProcesos= tk.Menu(self, tearoff=False)
        self.add_cascade(menu=menuProcesos, label='Procesos y Consultas')
        menuProcesos.add_command(label="Inventario",command=self.funInventario)
        menuProcesos.add_command(label="Combate", command=self.funCombate)
        menuProcesos.add_command(label="Narrador", command=self.funNarrador)
        menuProcesos.add_command(label="Tienda", command=self.funTienda)
        menuProcesos.add_command(label="Crear Personaje", command=self.funCrearpersonaje)
        menuayuda = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Ayuda",menu=menuayuda)
        menuayuda.add_command(label="Ayuda", command=ayuda)
    
    def regresarInicio(self):
        self.frameinicio.grid()
        self.frameinv.grid_forget()
        self.frameCom.grid_forget()
        self.frameNarr.grid_forget()
        self.frametienda.grid_forget()
        self.framecrear.grid_forget()

    def funInventario(self):
        self.frameinicio.grid_forget()
        self.frameinv.grid()
        self.frameCom.grid_forget()
        self.frameNarr.grid_forget()
        self.frametienda.grid_forget()
        self.framecrear.grid_forget()

    def funCombate(self):
        self.frameinicio.grid_forget()
        self.frameinv.grid_forget()
        self.frameCom.grid()
        self.frameNarr.grid_forget()
        self.frametienda.grid_forget()
        self.framecrear.grid_forget()
        self.combate.botonera() # JM        
        self.frameCom.countdown(5,self.label, self.frame6, self.mob, self.labelMob)
        
        

    def funNarrador(self):
        self.frameinicio.grid_forget()
        self.frameinv.grid_forget()
        self.frameCom.grid_forget()
        self.frameNarr.grid()
        self.frametienda.grid_forget()
        self.framecrear.grid_forget()
    def funTienda(self):
        self.frameinicio.grid_forget()
        self.frameinv.grid_forget()
        self.frameCom.grid_forget()
        self.frameNarr.grid_forget()
        self.frametienda.grid()
        self.framecrear.grid_forget()
    def funCrearpersonaje(self):
        self.frameinicio.grid_forget()
        self.frameinv.grid_forget()
        self.frameCom.grid_forget()
        self.frameNarr.grid_forget()
        self.frametienda.grid_forget()
        self.framecrear.grid()