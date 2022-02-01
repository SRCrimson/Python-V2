import tkinter as tk
from tkinter import *
from MenuBar import MenuBar
from inicioPage import inicioPage
from inventarioPage import frameInventario
from combatePage import CombatePage
from narradorPage import narradorPage
from tiendaPage import tiendaPage
from crearPersonajePage import crearPersonajePage
### CLASE APP ES LA VENTANA PRINCIPAL
class App(tk.Tk):
    def __init__(self,lista):
        super().__init__()
        self.title("Calabozos en la Nacho")
                # creating a frame and assigning it to container
       
        self.__create_widgets()
    def __create_widgets(self):
        frameinicio= inicioPage(self,"pagina de inicio")
        frameinicio.grid()

        frameinv=frameInventario(self,"frame inventario")
        frameCom=CombatePage(self,"frame combate")
        frameNarr=narradorPage(self,"frame Narrador")
        frametienda=tiendaPage(self,"frame Tienda")
        framecrear=crearPersonajePage(self,"frame crear personaje")

        # create the menu
        menubar = MenuBar(self,frameinicio,frameinv,frameCom,frameNarr,frametienda,framecrear)
        self.config(menu=menubar)