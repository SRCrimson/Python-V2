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
        invLabel1 = tk.Label(frameinicio, text="CALABOZOS EN LA NACHO",font=("Impact",18),fg="red",bg="#1C1C1C")
        invLabel1.grid(sticky=E,padx=20,pady=10,row=0, column=0, columnspan=3,rowspan=2)
        
        frame3= tk.Frame(frameinicio,width=600,height=400)
        frame3.grid(padx=20,pady=10,row=2, column=0,columnspan=4,rowspan=3)

        frameScroll = tk.Scrollbar(frame3) 
        frameScroll.pack(side = RIGHT, fill = Y) 
        labelNar = tk.Text(frame3, width = 80, height = 25, yscrollcommand = frameScroll.set,  font=("Helvetica", 8))
        labelNar.pack()
        #frame4= tk.Frame(frameinicio,width=100,height=100)
        #frame3.grid(padx=20, pady=10,row=1, column=0, columnspan=6,rowspan=7,sticky="nsew")
        Label(frameinicio, text="Opcion",width=10,font=("Monaco",14),fg="white",bg="#1C1C1C").grid(padx=5, row=6 ,column=0)
        Button(frameinicio, text="1",width=20).grid(padx=5, row=6, column=1)
        Button(frameinicio, text="2",width=20).grid(padx=5, row=6, column=2)

        Button(frameinicio, text="Atacar",width=20).grid(padx=5, row=7 ,column=1)
        Button(frameinicio, text="Pocion",width=20).grid(padx=5, row=7, column=2)
        Button(frameinicio, text="Escapar",width=20).grid(padx=5, row=7, column=3)

        Button(frameinicio, text="Hoja Personaje",width=20).grid(padx=5, row=5, column=5)
        Button(frameinicio, text="save",width=20).grid(padx=5, row=6, column=5)
        Button(frameinicio, text="help",width=20).grid(padx=5, row=7, column=5)

        #BOTONES DE REGISTRO Y LOGIN
        Button(frameinicio, text="Registrarse",width=20,command = self.funRegistrarse).grid(padx=5, row=0, column=5)
        Button(frameinicio, text="Ingresar",width=20,command=self.funIngresar).grid(padx=5, row=1, column=5)

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

    def funIngresar(self):
        tituloCriterios="Criterios"
        criterios=["Nombre","Contraseña"]
        tituloValores="Valor"
        valores=[None,None]
        habilitado=[None,"*"]
        filewin = Toplevel(self)
        #entry = ttk.Entry(root, state=tk.DISABLED) habilitacion
        formato=FieldFrame(filewin,tituloCriterios, criterios, tituloValores, valores, habilitado)
        formato.pack()
        def login():
            pass
        
