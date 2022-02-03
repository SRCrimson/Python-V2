import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import *
from FieldFrame import FieldFrame
class usuarioRegistrarsePage(tk.Frame):
    def __init__(self, container,labeltext):
        super().__init__(container)
        ####valores y criterios que conformaran el fomulario por defecto
        tituloCriterios="Criterios"
        criterios=["Nombre","Contraseña","Correo"]
        tituloValores="Valor"
        valores=[None,None,"mono@gmail.com"]
        habilitado=[None,"*",None]
        frameinventario=tk.Frame(self,background="#1C1C1C",bd=0, relief="sunken")
        frameinventario.grid()
        frame2= tk.Frame(frameinventario, background="#1C1C1C",width=400,height=200)
        invLabel1 = tk.Label(frame2, text="Registrarse",font=("Verdana",16),fg="red",bg="#1C1C1C")
        invLabel1.grid(sticky=N,padx=20,pady=10)
        invLabel1.grid_propagate(0)
        frame3= tk.Frame(frameinventario, background="#1C1C1C",width=600,height=250)
        frame2.grid(padx=20, pady=10)
        frame3.grid(padx=20, pady=10)
        #se llama a la clase FieldFreame 
        formato=FieldFrame(frame3,tituloCriterios, criterios, tituloValores, valores, habilitado)
        formato.grid(column=0,columnspan=2)
