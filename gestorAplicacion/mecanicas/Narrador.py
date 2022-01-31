from cgitb import text
import tkinter as tk

window = tk.Tk()
window.geometry("1024x768")

class combate():    
    def __init__(self, pj, mob):
        self.pj = pj
        self.mob = mob
        self.ataque_basico= tk.Button(window,text="Atacar", command=lambda:[self.pj.ataque_basico(), self.turnoMob()], state="disabled")
        self.ataque_basico.pack()
        self.hechizo_1 = tk.Button(window,text="Hechizo 1", command=lambda:[self.pj.hechizo_1(), self.turnoMob()], state="disabled")
        self.hechizo_1.pack()
        self.hechizo_2 = tk.Button(window,text="Hechizo 2", command=lambda:[self.pj.hechizo_2(), self.turnoMob()], state="disabled")
        self.hechizo_2.pack()
        self.hechizo_3 = tk.Button(window,text="Hechizo 3", command=lambda:[self.pj.hechizo_3(), self.turnoMob()], state="disabled")
        self.hechizo_3.pack()

        self.frame = tk.Frame(window, background="#FFF0C1", width=400, height=100)
        self.frame.pack()
        self.label = tk.Label(self.frame, text="Hola")
        self.label.pack()

        

    def setTurno(self):        
        if self.pj.DES >= 18: #self.mob.DES:
            print("pj")
            self.turnoPlayer()
        else:
            print("mob")
            self.turnoMob()

    def turnoPlayer(self):                
        self.ataque_basico["state"] = "normal"
        self.hechizo_1["state"] = "normal"
        self.hechizo_2["state"] = "normal"
        self.hechizo_3["state"] = "normal"
        if self.pj.getHp() <= 0: #or self.obj.mob.getHp() <= 0:
            self.batallaTerminada()

    def turnoMob(self):        
        self.ataque_basico.config(state="disabled")
        self.ataque_basico["state"] = "disabled"
        self.hechizo_1["state"] = "disabled"
        self.hechizo_2["state"] = "disabled"
        self.hechizo_3["state"] = "disabled" 
        self.label.config(text="Enemigo atacó")
        window.after(1000, print("Enemigo atacó"))
        window.after(1000, print("Enemigo atacó"))
        window.after(1000, print("Enemigo atacó"))
        self.pj.HP -= 4
        if self.pj.getHp() <= 0: #or self.obj.mob.getHp() <= 0:
            self.batallaTerminada()
        else:
            window.after(1000, self.turnoPlayer())
    
        
    def batallaTerminada(self):
        self.ataque_basico.config(state="disabled")
        self.ataque_basico["state"] = "disabled"
        self.hechizo_1["state"] = "disabled"
        self.hechizo_2["state"] = "disabled"
        self.hechizo_3["state"] = "disabled" 
        print("Batalla terminada")
