from cProfile import label
from cgitb import text
import tkinter as tk
from turtle import right
from random import randint

class combate():    
    
    def __init__(self, pj, mob, window, narrativa, labelNar, labelPJ, labelMob):
        self.window = window
        self.narrativa = narrativa
        self.labelNar = labelNar
        self.labelPJ = labelPJ
        self.labelMob = labelMob
        self.pj = pj
        self.mob = mob
        self.objetivoPj = 10 + self.mob.nivel + self.pj.AC # - Armadura.getDefensa()
        self.objetivoRival = 14 + self.pj.nivel + self.mob.AC

    def botonera(self):
        hechizo1 = self.pj.hechizo_1(self.mob,self.pj, "consulta")
        hechizo2 = self.pj.hechizo_2(self.mob,self.pj, "consulta")
        hechizo3 = self.pj.hechizo_3(self.mob,self.pj, "consulta")
        self.ataque_basico= tk.Button(self.window,text="Atacar", command=lambda:[self.ataque_basico_nar(), self.pj.ataque_basico(), self.turnoMob()], state="disabled")
        self.ataque_basico.grid(column=0,row=0)
        
        self.hechizo_1 = tk.Button(self.window,text=hechizo1.nombre +"("+str(hechizo1.costo)+")", command=lambda:[self.hechizo_1_nar(self.pj.hechizo_1(self.mob,self.pj, "")), self.turnoMob()], state="disabled")
        self.hechizo_1.grid(column=1,row=0)
        self.hechizo_2 = tk.Button(self.window,text=hechizo2.nombre +"("+str(hechizo2.costo)+")", command=lambda:[self.hechizo_1_nar(self.pj.hechizo_2(self.mob,self.pj, "")), self.turnoMob()], state="disabled")
        self.hechizo_2.grid(column=2,row=0)
        self.hechizo_3 = tk.Button(self.window,text=hechizo3.nombre +"("+str(hechizo3.costo)+")", command=lambda:[self.hechizo_1_nar(self.pj.hechizo_3(self.mob,self.pj, "")), self.turnoMob()], state="disabled")
        self.hechizo_3.grid(column=3,row=0)

        
    def ataque_basico_nar(self):
        
        self.labelNar.insert(tk.END,"\nHas atacado")
        if self.lanzarDados(20) <= self.objetivoRival:
            dano = self.lanzarDados(self.pj.dano)
            crit = ""
            if self.lanzarDados(20) >= 19:
                dano *= 2
                crit = " crítico!"
            self.mob.HP -= dano
            self.labelNar.insert(tk.END,"\n-Realizaste " + str(dano) + " de daño"+crit)
            text = self.mob.nombre + " HP: " + str(self.mob.HP)
            self.labelMob.config(text=text)
        else:
            self.labelNar.insert(tk.END,"\n-Fallaste tu ataque")

    def hechizo_1_nar(self, hechizo):
                
        self.labelNar.insert(tk.END,"\nHas usado " + hechizo.nombre)
        self.pj.MP -= hechizo.costo        
        if self.lanzarDados(20) <= self.objetivoRival:
            hechizo.efecto
            #dano = self.lanzarDados(self.pj.dano+3)
            #self.mob.HP -= dano
            self.labelNar.insert(tk.END, hechizo.mensaje)
            text = self.mob.nombre + " HP: " + str(self.mob.HP)            
            self.labelMob.config(text=text)
            textPJ = self.pj.nombre + "HP: " + str(self.pj.HP) + " MP: " +str(self.pj.MP) 
            self.labelPJ.config(text=textPJ)
        else:
            self.labelNar.insert(tk.END,"\n-Fallaste " + hechizo.nombre)
    

    def setTurno(self):        
        """self.frameNar = tk.Frame(self.narrativa, background="#FFF0C1", width=200, height=100)
        self.frameNar.pack(side="right")
        self.frameNar.pack_propagate(False)
        self.labelNar = tk.Label(self.frameNar, text="Turno del rival")
        self.labelNar.pack()"""
        if self.pj.DES >= self.mob.DES:
            self.turnoPlayer()
        elif self.pj.DES < 18:            
            self.turnoMob()
        
        
        

    def turnoPlayer(self):                
        self.labelNar.insert(tk.END,"\n------------------------\nTurno de: "+ self.pj.nombre)
        self.ataque_basico["state"] = "normal"
        hechizo1 = self.pj.hechizo_1(self.mob,self.pj, "consulta")
        hechizo2 = self.pj.hechizo_2(self.mob,self.pj, "consulta")
        hechizo3 = self.pj.hechizo_3(self.mob,self.pj, "consulta")
        
        if self.pj.MP < hechizo1.costo:
            self.hechizo_1["state"] = "disabled"
        else:
            self.hechizo_1["state"] = "normal"

        if self.pj.MP < hechizo2.costo:
            self.hechizo_2["state"] = "disabled"
        else:
            self.hechizo_2["state"] = "normal"            

        if self.pj.MP < hechizo3.costo:
            self.hechizo_3["state"] = "disabled"
        else:
            self.hechizo_3["state"] = "normal"
        

        '''if self.pj.MP < 1:
            self.hechizo_1["state"] = "disabled"
            self.hechizo_2["state"] = "disabled"
            self.hechizo_3["state"] = "disabled"
        else:
            self.hechizo_1["state"] = "normal"
            self.hechizo_2["state"] = "normal"
            self.hechizo_3["state"] = "normal"'''

        if self.mob.HP <= 0:
            self.batallaTerminada(self.pj.nombre)

    def turnoMob(self):                
        #self.window.after(1000, 
        self.labelNar.insert(tk.END,"\n------------------------\nTurno de: "+ self.mob.nombre)
        self.labelNar.insert(tk.END,"\n"+self.mob.nombre+" Enemigo atacó")
#        self.labelNar.pack()
        
        if self.lanzarDados(20) <= self.objetivoPj:
            dano = self.lanzarDados(self.mob.dano)
            crit = ""
            if self.lanzarDados(20) >= 19:
                dano *= 2
                crit = " crítico!"
            self.pj.HP -= dano
            self.labelNar.insert(tk.END,"\n-Realizó " + str(dano) + " de daño"+crit)
            textPJ = self.pj.nombre + "HP: " + str(self.pj.HP) + " MP: " +str(self.pj.MP) 
            self.labelPJ.config(text=textPJ)
        else:
            self.labelNar.insert(tk.END,"\n-Falló su ataque")
        if self.pj.getHp() <= 0:
            self.batallaTerminada(self.mob.nombre)
        else:
            self.window.after(1000, self.turnoPlayer())
        
    
    def lanzarDados(self, max):
        resultadoDados = randint (1, max)
        return resultadoDados

    def batallaTerminada(self, winner):
        self.ataque_basico.config(state="disabled")
        self.ataque_basico["state"] = "disabled"
        self.hechizo_1["state"] = "disabled"
        self.hechizo_2["state"] = "disabled"
        self.hechizo_3["state"] = "disabled" 
        self.labelNar.insert(tk.END,"\nBatalla terminada\n" + winner + " Gana!")
