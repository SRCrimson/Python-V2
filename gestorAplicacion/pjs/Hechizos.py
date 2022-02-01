import random

class Hechizo():
    def __init__(self, nombre, costo, dano, mensaje, efecto):
        self.nombre = nombre
        self.costo = costo
        self.dano = dano
        self.mensaje = mensaje
        self.efecto = efecto
    
    def escarcha_mistica(self, mob, consulta): 
        self.nombre = "Escarcha mística"
        self.costo = 2
        self.dano = self.lanzarDados(6)        
        if consulta == "consulta":
            self.efecto = None
        else:
            self.efecto = self.damage(self.dano, mob)
        self.mensaje = "\n-Realizaste " + str(self.dano) + " de daño"
        #self.labelNar.insert(tk.END,"\n-Realizaste " + str(dano) + " de daño")
        
    
    def flecha_fuego(self, mob, consulta): 
        self.nombre = "Flecha de fuego"
        self.costo = 2
        self.dano = self.lanzarDados(6)
        if consulta == "consulta":
            self.efecto = None
        else:
            self.efecto = self.damage(self.dano, mob)
        self.mensaje = "\n-Realizaste " + str(self.dano) + " de daño"

    
    def cura_celestial(self, pj, consulta): 
        
        self.nombre = "Cura celestial"
        self.costo = 2
        self.dano = self.lanzarDados(6)        
        if consulta == "consulta":
            self.efecto = None
        else:
            print("WTF")
            self.efecto = self.cura(self.dano, pj)
        self.mensaje = "\n-Realizaste " + str(self.dano) + " de curación"

    def damage(self, dano, mob):
        mob.HP -= dano

    def cura(self, cura, pj):
        pj.HP += cura

    def lanzarDados(self, max):
        resultadoDados = random.randint (1, max)
        return resultadoDados

