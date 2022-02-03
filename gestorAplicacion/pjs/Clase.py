

class Clase:
    CRIT_CHANCE = 3.5
    BLOCK_CHANCE=3.5
    HP_RECOV=3.5

    def __init__(self, clase):  #Clase debe ser de tipo int
        if clase==1:
            self.GUERRERO()
        elif clase == 2:
            self.ARQUERO()
        else:
            self.MAGO()

    def GUERRERO(self, FUE=8, DES=1,INT=1,CON=5,CAR=1,SAB=1):
        self.FUE=FUE
        self.DES=DES
        self.INT=INT
        self.CON=CON
        self.CAR=CAR
        self.SAB=SAB
        self.name ="Guerrero"

    def ARQUERO(self, FUE=1, DES=8,INT=1,CON=1,CAR=5,SAB=1):
        self.FUE = FUE
        self.DES = DES
        self.INT = INT
        self.CON = CON
        self.CAR = CAR
        self.SAB = SAB
        self.name = "Arquero"

    def MAGO(self, FUE=1, DES=1,INT=8,CON=1,CAR=1,SAB=5):
        self.FUE = FUE
        self.DES = DES
        self.INT = INT
        self.CON = CON
        self.CAR = CAR
        self.SAB = SAB
        self.name = "Mago"

    def getNombre(self):
        return self.name

    def getCrit(self):
        return self.CRIT_CHANCE

    def getBlock(self):
        return self.BLOCK_CHANCE

    def getHp(self):
        return self.HP_RECOV

    def setCrit(self, crit):
        self.CRIT_CHANCE = crit

    def setBlock(self, block):
        self.BLOCK_CHANCE = block

    def setHp(self, hp):
        self.HP_RECOV = hp

    def aplicarVentajas(self):
        if self.name=="Guerrero":
            self.setBlock(4.8)

        elif self.name== "Arquero":
            self.setCrit(5.5)

        else :
            self.setCrit(4)

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


