import os
import tkinter as tk
from tkinter import *
import os
from turtle import width
from FieldFrame import FieldFrame
import gestorAplicacion.mecanicas.Narrador as narrador # JM
import gestorAplicacion.pjs.Player as player # JM
import gestorAplicacion.pjs.Enemy as Enemy #JM

class inicioPage(tk.Frame):
    pejota = None
    def __init__(self, container,labeltext):
        super().__init__(container)

        frameinicio=tk.Frame(self,background="#1C1C1C",bd=0, relief="sunken")
        frameinicio.pack()
        
        #frameinicio.pack_propagate(False)
        invLabel1 = tk.Label(frameinicio, text="CALABOZOS EN LA NACHO",font=("Impact",18),fg="red",bg="#1C1C1C")
        invLabel1.grid(row=0, column=0)
        
        frame3= tk.Frame(frameinicio, bg="#1C1C1C")
        frame3.grid(row=1, column=0, columnspan=2)

        

        ##
        frame5 = tk.Frame(frameinicio, bg="#1C1C1C")
        frame5.grid(row=1, column=2, columnspan=2)
        
        frame6= tk.Frame(frame5, background="#CCE4CA",width=310, height= 301)
        frame6.pack_propagate(False) # JM
        frame7= tk.Frame(frame5, background="#1C1C1C", width=210, height= 40)
        frame7.pack_propagate(False) # JM        
        
        
        frameinicio.grid_columnconfigure(0, weight=1, uniform="fred")
        frameinicio.grid_columnconfigure(1, weight=1, uniform="fred")
        frameinicio.grid_columnconfigure(2, weight=1, uniform="fred")
        
        frame6.grid(row=1, column=1, sticky="nsew")
        frame7.grid(row=2, column=1, sticky="nsew")
        frame6.grid_columnconfigure(0, weight=1)
        
        frameNar = tk.Frame(frame6, background="#1C1C1C", width=140, height=301) # JM
        frameNar.pack(side="right") # JM
        frameNar.pack_propagate(False) # JM
        frameNar.grid_columnconfigure(0, weight=1)
        sframeScroll = tk.Scrollbar(frameNar) # JM
        sframeScroll.pack(side = RIGHT, fill = Y) # JM
        slabelNar = tk.Text(frameNar, width = 29, height = 22, yscrollcommand = sframeScroll.set,  font=("Helvetica", 8)) # JM

        slabelNar.insert(END,"Registro de batalla") # JM

        slabelNar.pack() # JM
        sframeScroll.config(command=slabelNar.yview) # JM

        

        pj = player.Player() # JM
        self.pejota = pj
        mob = Enemy.Enemy() #JM
        mob.goblin() # JM

        
        #self.label = tk.Label(self.frame6) # JM
        #self.label.pack(side=TOP)  # JM
        textPJ = pj.nombre + " HP: " + str(pj.HP) + " MP: " +str(pj.MP) # JM
        labelPJ = tk.Label(frame6, text=textPJ) # JM
        labelPJ.pack(side=BOTTOM) # JM
        text = mob.nombre + " HP: " + str(mob.HP)
        labelMob = tk.Label(frame6, text=text)
        labelMob.pack(side=TOP)
        combate = narrador.combate(pj, mob, frame7, frame6, slabelNar, labelPJ, labelMob) # JM
        combate.botonera()

        
        ##

        
        #frameScroll.pack(side = RIGHT, fill = Y) 
        
        frameScroll = tk.Scrollbar(frame3) # JM
        frameScroll.pack(side = RIGHT, fill = Y) # JM
        
        labelNar = tk.Text(frame3, width = 80, height = 25, yscrollcommand = frameScroll.set,  font=("Helvetica", 8))
        labelNar.pack()
        #labelNar.grid()
        frameScroll.config(command=labelNar.yview) # JM
        #frame4= tk.Frame(frameinicio,width=100,height=100)
        #frame3.grid(padx=20, pady=10,row=1, column=0, columnspan=6,rowspan=7,sticky="nsew")
        #Label(frameinicio, text="Opcion",width=10,font=("Monaco",14),fg="white",bg="#1C1C1C").grid(padx=5, row=6 ,column=0)
        Button(frameinicio, text="OPCIÓN A", width=70).grid(row=5, column=0,columnspan=2)
        Button(frameinicio, text="OPCIÓN B", width=70).grid(row=6, column=0,columnspan=2)
        #Button(frameinicio, text="1",width=20).grid(row=6, column=1)
        #Button(frameinicio, text="2",width=20).grid(row=6, column=3)

        #Button(frameinicio, text="Atacar",width=20).grid(row=7 ,column=1)
        #Button(frameinicio, text="Pocion",width=20).grid(row=7, column=2)
        #Button(frameinicio, text="Escapar",width=20).grid(row=7, column=2)

        #Button(frameinicio, text="Hoja Personaje",width=20).grid(row=5, column=2)
        Button(frameinicio, text="save",width=20).grid(row=6, column=2)
        Button(frameinicio, text="help",width=20).grid(row=7, column=2)

        #BOTONES DE REGISTRO Y LOGIN
        #Button(frameinicio, text="Registrarse",width=20,command = self.funRegistrarse).grid(row=0, column=3)
        #Button(frameinicio, text="Ingresar",width=20,command=self.funIngresar).grid(row=1, column=3)

    def funRegistrarse(self):
        tituloCriterios="Criterios"
        criterios=["Nombre","Correo","Contraseña"]
        tituloValores="Valor"
        valores=["eider",None,"dola"]
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
    
    def getPj(self):
        return self.pejota