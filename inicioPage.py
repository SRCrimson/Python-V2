import os
import tkinter as tk
from tkinter import *
import os
from turtle import width
from FieldFrame import FieldFrame


class inicioPage(tk.Frame):
    def __init__(self, container,labeltext):
        super().__init__(container)

        frameinicio=tk.Frame(self,background="#1C1C1C",bd=0, relief="sunken")
        frameinicio.pack()
        #frameinicio.pack_propagate(False)
        invLabel1 = tk.Label(frameinicio, text="CALABOZOS EN LA NACHO",font=("Impact",16),fg="red",bg="#1C1C1C")
        invLabel1.grid(sticky=E,padx=20,pady=10,row=0, column=0, columnspan=2)
        
        frame3= tk.Frame(frameinicio,width=600,height=400)
        frame3.grid(padx=20,pady=10,row=2, column=0,columnspan=3,rowspan=3)

        #frame4= tk.Frame(frameinicio,width=100,height=100)
        #frame3.grid(padx=20, pady=10,row=1, column=0, columnspan=6,rowspan=7,sticky="nsew")
        Button(frameinicio, text="Atacar",width=10).grid(padx=20, row=6 ,column=0)
        Button(frameinicio, text="Pocion",width=20).grid(padx=5, row=6, column=1)
        Button(frameinicio, text="Escapar",width=20).grid(padx=5, row=6, column=2)

        Button(frameinicio, text="Hoja Personaje",width=20).grid(padx=5, row=3, column=5)
        Button(frameinicio, text="save",width=20).grid(padx=5, row=4, column=5)
        Button(frameinicio, text="help",width=20).grid(padx=5, row=5, column=5)

        #BOTONES DE REGISTRO Y LOGIN
        Button(frameinicio, text="Registrarse",width=20,command = self.funRegistrarse).grid(padx=5, row=0, column=5)
        Button(frameinicio, text="Ingresar",width=20).grid(padx=5, row=1, column=5)

    def funRegistrarse(self):
        tituloCriterios="Criterios"
        criterios=["Nombre","Correo","Contraseña"]
        tituloValores="Valor"
        valores=[None,None,"dola"]
        habilitado=[None,None,"2"]
        filewin = Toplevel(self)
        #entry = ttk.Entry(root, state=tk.DISABLED) habilitacion
        formato=FieldFrame(filewin,tituloCriterios, criterios, tituloValores, valores, habilitado)
        formato.pack()
        def login():
            pass

