import sqlite3
import tkinter as tk
from tkinter import *
from FieldFrame import FieldFrame
class usuarioIngresarPage(tk.Frame):
    def __init__(self, container,labeltext):
        super().__init__(container)
        tituloCriterios="Criterios"
        criterios=["Nombre","Contraseña"]
        tituloValores="Valor"
        valores=[None,None]
        habilitado=[None,"*"]
        conn = sqlite3.connect('usuariosBD.sqlite')
        frameinventario=tk.Frame(self,background="#1C1C1C",bd=0, relief="sunken")
        frameinventario.grid()
        frame2= tk.Frame(frameinventario, background="#1C1C1C",width=400,height=200)
        invLabel1 = tk.Label(frame2, text="Ingresar",font=("Verdana",16),fg="red",bg="#1C1C1C")
        invLabel1.grid(sticky=N,padx=20,pady=10)
        invLabel1.grid_propagate(0)
        frame3= tk.Frame(frameinventario, background="#CCE4CA",width=600,height=250)
        frame2.grid(padx=20, pady=10)
        frame3.grid(padx=20, pady=10)
        formato=FieldFrame(frame3,tituloCriterios, criterios, tituloValores, valores, habilitado)
        formato.pack()