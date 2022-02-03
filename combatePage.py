import os
import tkinter as tk
from tkinter import *
import os

from gestorAplicacion.mecanicas.Narrador import combate # JM
import gestorAplicacion.mecanicas.Narrador as narrador # JM
import gestorAplicacion.pjs.Player as player # JM
import gestorAplicacion.pjs.Enemy as Enemy #JM
import gestorAplicacion.mecanicas.iu # JM



class CombatePage(tk.Frame):
    combate = None
    label, frame6, mob, labelMob = 0,0,0,0
    def __init__(self, container,labeltext):
        super().__init__(container)

        
        frameCombate=tk.Frame(self,background="#1C1C1C",bd=0, relief="sunken")
        frameCombate.grid()
        frame5= tk.Frame(frameCombate, background="#1C1C1C",width=400,height=200)
        comLabel1 = tk.Label(frame5, text="Combate",font=("Impact",16),fg="red",bg="#1C1C1C")
        comLabel1.grid(padx=20,pady=10)
        comLabel2 = tk.Label(frame5, text="enfrentamiento entre el jugador y un enemigo,\nesta funcionalidad nos permite realizar subfunciones \ncomo atacar, ver posición o rendirse.",
                                font=("Monaco",12),fg="white",bg="#1C1C1C",relief= "solid",justify= LEFT)
        comLabel2.grid(padx=20,pady=10)
        self.frame6= tk.Frame(frameCombate, background="#CCE4CA",width=400,height=200)
        frame7= tk.Frame(frameCombate, background="#CCE4CA",width=400,height=200)
        frame5.grid(padx=20, pady=10)
        self.frame6.grid(padx=20, pady=10)
        frame7.grid()

                
        '''frameCombate=tk.Frame(self,background="#566573",bd=0, relief="sunken")
        frame5= tk.Frame(frameCombate, background="#566573",width=400,height=200)
        comLabel1 = tk.Label(frame5, text="Combate",font=("Verdana",16))
        comLabel1.grid(padx=20,pady=10)
        comLabel2 = tk.Label(frame5, text="Descripción",font=("Verdana",16))
        comLabel2.grid(padx=20,pady=10)
        frame6= tk.Frame(frameCombate, background="#CCE4CA",width=400,height=200)
        frame6.pack_propagate(False) # JM
        frame7= tk.Frame(frameCombate, background="#CCE4CA",width=400,height=200)
        frame7.pack_propagate(False) # JM
        frame5.grid(padx=20, pady=10)
        frame6.grid(padx=20, pady=10)
        frame7.grid()'''

        frameNar = tk.Frame(self.frame6, background="#FFF0C1", width=150, height=200) # JM
        frameNar.pack(side="right") # JM
        frameNar.pack_propagate(False) # JM
        frameScroll = tk.Scrollbar(frameNar) # JM
        frameScroll.pack(side = RIGHT, fill = Y) # JM
        labelNar = tk.Text(frameNar, width = 29, height = 15, yscrollcommand = frameScroll.set,  font=("Helvetica", 8)) # JM

        labelNar.insert(END,"Registro de batalla") # JM

        labelNar.pack() # JM
        frameScroll.config(command=labelNar.yview) # JM


        '''def countdown(count): # JM
            label['text'] = "El combate iniciará en " + str(count) # JM
            if count >= 0:        # JM
                frame6.after(1000, countdown, count-1) # JM            
            else: # JM
                label.destroy()
                text = mob.nombre + " HP: " + str(mob.HP)
                
                labelMob.pack(side=TOP)
                combate.setTurno() # JM'''

        pj = player.Player() # JM
        self.mob = Enemy.Enemy() #JM
        self.mob.goblin() # JM

        
        #self.label = tk.Label(self.frame6) # JM
        #self.label.pack(side=TOP)  # JM
        textPJ = pj.nombre + " HP: " + str(pj.HP) + " MP: " +str(pj.MP) # JM
        labelPJ = tk.Label(self.frame6, text=textPJ) # JM
        labelPJ.pack(side=BOTTOM) # JM
        text = self.mob.nombre + " HP: " + str(self.mob.HP)
        self.labelMob = tk.Label(self.frame6, text=text)
        self.labelMob.pack(side=TOP)
        option_a = Button(self.frame6, text="OPCIÓN A", width=70)        
        option_b = Button(self.frame6, text="OPCIÓN B", width=70)
        self.combate = narrador.combate(pj, self.mob, frame7, self.frame6, labelNar, labelPJ, self.labelMob, option_a, option_b) # JM

    def countdown(self, count, label, frame6, mob, labelMob): # JM
        self.combate.setTurno() # JM
        ''' label['text'] = "El combate iniciará en " + str(count) # JM
        if count >= 0:        # JM
            frame6.after(1000, self.countdown(count=count-1,label=label, frame6=frame6, mob=mob, labelMob=labelMob)) # JM            
        else: # JM
            label.destroy()
            text = mob.nombre + " HP: " + str(mob.HP)
            
            labelMob.pack(side=TOP)
            self.combate.setTurno() # JM'''
    