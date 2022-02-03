from distutils import command
import os
import tkinter as tk
from tkinter import *
import os
from gestorAplicacion.Loadout.Inventario import Inventario

class frameInventario(tk.Frame):
    def __init__(self, container,labeltext):
        super().__init__(container)

        frameinventario=tk.Frame(self,background="#1C1C1C",bd=0, relief="sunken")
        frameinventario.grid()
        frame2= tk.Frame(frameinventario, background="#1C1C1C",width=400,height=200)
        invLabel1 = tk.Label(frame2, text="Inventario",font=("Impact",16),fg="red",bg="#1C1C1C")
        invLabel1.grid(sticky=N,padx=20,pady=10)
        invLabel2 = tk.Label(frame2, text="El jugador puede tener un recuento de \nlos recursos. Armaduras, Armas, Pociones.", font=("Monaco",12),fg="white",bg="#1C1C1C",relief= "solid",justify= LEFT)
        invLabel2.grid(padx=20,pady=10)
        frame3= tk.Frame(frameinventario, background="#CCE4CA",width=600,height=250)
        frame2.grid(padx=20, pady=10)
        frame3.grid(padx=20, pady=10)






        
    
