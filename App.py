import tkinter as tk
from tkinter import *

from MenuBar import MenuBar
from inicioPage import inicioPage
from inventarioPage import frameInventario
from combatePage import CombatePage
from narradorPage import narradorPage
from tiendaPage import tiendaPage
from crearPersonajePage import crearPersonajePage
from UsuarioRegistrarsePage import usuarioRegistrarsePage
from UsuarioIngresarPage import usuarioIngresarPage


### CLASE APP ES LA VENTANA PRINCIPAL
class App(tk.Tk):
    menuBar = None # JM
    def __init__(self):
        super().__init__()
        self.title("Calabozos en la Nacho")

        self.__create_widgets()

    def __create_widgets(self):
        frameinicio= inicioPage(self,"pagina de inicio")
        frameinicio.grid()

        frameinv=frameInventario(self,"frame inventario")
        frameCom=CombatePage(self,"frame combate")
        frameNarr=narradorPage(self,"frame Narrador")
        frametienda=tiendaPage(self,"frame Tienda", frameinicio.getPj())
        framecrear=crearPersonajePage(self,"frame crear personaje")
        frameReg=usuarioRegistrarsePage(self,"frame usuario")
        frameIngresar=usuarioIngresarPage(self,"frame usuario")
        combate = frameCom.combate        
        label = frameCom.label
        frame6 = frameCom.frame6
        mob = frameCom.mob
        labelMob = frameCom.labelMob  
        
        # create the menu
        self.menubar = MenuBar(self,frameinicio,frameinv,frameCom,frameNarr,frametienda,framecrear,frameReg,frameIngresar, combate, label, frame6, mob, labelMob)
        self.config(menu=self.menubar)