import tkinter


import tkinter as tk

window = tk.Tk()
window.geometry("1024x768")


class combate():    
    def __init__(self, pj, mob):
        self.pj = pj
        self.mob = mob
    
    def setFrame(self):
        ataque_basico= tk.Button(window,text="Atacar", command=self.pj.ataque_basico)
        ataque_basico.pack()
        hechizo_1 = tk.Button(window,text="Hechizo 1", command=self.pj.hechizo_1)
        hechizo_1.pack()
        hechizo_2 = tk.Button(window,text="Hechizo 2", command=self.pj.hechizo_2)
        hechizo_2.pack()
        hechizo_3 = tk.Button(window,text="Hechizo 2", command=self.pj.hechizo_3)
        hechizo_3.pack()


    def turnoPj(self):
        self.pj.DES = 10 # PROVISIONAL
        self.mob.DES = 8 # PROVISIONAL
        if self.pj.DES >= self.mob.DES:
            return True
    

combate = combate("pj", "mob")

if combate.turnoPj:
    combate.setFrame()

window.mainloop()