from gestorAplicacion.pjs.Clase import Clase

class NPC:
    def __init__(self,nombre, edad, clase, nivel):
        self.nombre = nombre
        self.edad = edad

        self.nivel= nivel

        self.clas= Clase(clase)

        self.subirNivel(nivel)


    def subirNivel(self, nivel):

        if self.clas.name== "Guerrero":
            self.FUE = self.clas.getFuerza() + 3* self.nivel
            self.CON = self.clas.getConstitucion() + 2* self.nivel
            self.DES = self.clas.getDestreza() + 1* self.nivel
            self.INT = self.clas.getInteligencia() + 1* self.nivel
            self.SAB = self.clas.getSabiduria() + 1*self.nivel
            self.CAR = self.clas.getCarisma() + 1* self.nivel
            self.HP =  self.clas.getConstitucion()* self.nivel
        elif self.clas.name== "Arquero":
            self.FUE = self.clas.getFuerza() + 1* self.nivel
            self.CON = self.clas.getConstitucion() + 1*self.nivel
            self.DES = self.clas.getDestreza() + 3* self.nivel
            self.INT = self.clas.getInteligencia() + 1* self.nivel
            self.SAB = self.clas.getSabiduria() + 2* self.nivel
            self.CAR = self.clas.getCarisma() + 1* self.nivel
            self.HP = self.clas.getConstitucion() * self.nivel
        elif self.clas.name== "Mago":
            self.FUE = self.clas.getFuerza() + 1* nivel
            self.CON = self.clas.getConstitucion() + 1*nivel
            self.DES = self.clas.getDestreza() + 1*nivel
            self.INT = self.clas.getInteligencia() + 3*nivel
            self.SAB = self.clas.getSabiduria() + 2*nivel
            self.CAR = self.clas.getCarisma() + 1* nivel
            self.HP = self.clas.getConstitucion() * self.nivel

        self.clas.aplicarVentajas()

    def getFuerza(self):
        return self.FUE

    def getDestreza(self):
        return self.DES

    def getInteligencia(self):
        return self.INT

    def getCarisma(self):
        return self.CAR

    def getSabiduria(self):
        return self.SAB

    def getConstitucion(self):
        return self.CON

    def getClase(self):
        return self.clas

    def getTipoClase(self):
        return self.clas.name

    def getHp(self):
        return self.HP




