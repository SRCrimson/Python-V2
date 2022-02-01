import string
from random import randint

from gestorAplicacion.pjs.NPC import NPC
from gestorAplicacion.pjs.Clase import Clase
import gestorAplicacion.pjs.Hechizos as hechizos
##import java.io.Serializable;

#from gestorAplicacion.Loadout.Inventario import Inventario
#from gestorAplicacion.Loadout.Armadura import Armadura
#from gestorAplicacion.Loadout.Arma import Arma


class Player(NPC):     #serializable

	min = 1
	max = 20
	clase= Clase
	
	 
	def __init__(self,nombre="Freud Baggins",HP=20,MP=3,AC=6,nivel=1,xp=0,clase= 1,edad=50,FUE=12,DES=12,CON=12,INT=12,SAB=12,CAR=12, dano = 4): #Jugador por defecto
		#reemplazado clase = Clase.GUERRERO: Clase debe ser tipo int
		super().__init__(nombre, edad, clase, nivel)

		self.AC = AC
		self.nivel = nivel
		self.HP = HP
		self.MP = MP
		self.xp = xp
		self.FUE = FUE
		self.DES = DES
		self.CON = CON
		self.INT = INT
		self.SAB = SAB
		self.CAR = CAR
		self.dano = dano
		#self.inventario = Inventario()
		self.wallet = 0    #agrego a la clase por defecto la billetera para la tienda, implementar en general
		#self.armadura = Armadura("Escudo de cuero", "Escudo pequeño hecho de cuero", 3, 300)
		##Inventario.listaArmaduras.add(self.armadura)
		#self.arma = Arma("Espada corta", "Pequeña espada corta forjada por herreros locales",4,1)
		#Inventario.listaArmasGuerrero.add(self.arma)
		self.descripcion = "Humano del Este adiestrado en el arte de la guerra."


	def Jugador (self,nombre,edad,clase):
		super().__init__(nombre, edad,  clase, 1)
		clase= super().getClase()
		self.AC = 8
		self.HP = 20 + clase.getConstitucion() + self.getHp()
		self.MP = 3 # EL MAGO DEBE TENER MÁS
		self.FUE += clase.getFuerza() + self.lanzarDados()
		self.DES += clase.getDestreza() + self.lanzarDados()
		self.CON += clase.getConstitucion() + self.lanzarDados()
		self.CAR += clase.getCarisma() + self.lanzarDados()
		self.INT += clase.getInteligencia() + self.lanzarDados()
		self.SAB += clase.getSabiduria() + self.lanzarDados()
		self.arquetipo(self.HP, self.AC, self.FUE,self.DES, self.CON,self.INT, self.SAB,self.CAR)
		self.dano = 4

	def arquetipo(self,aHP,aAC,aFUE,aDES,aCON,aINT,aSAB,aCAR):
		self.aHP = self.HP
		self.aAC = self.AC					
		self.aFUE = self.FUE
		self.aDES = self.DES
		self.aCON = self.CON
		self.aINT = self.INT	
		self.aSAB = self.SAB
		self.aCAR = self.CAR

	def lanzarDados(self) :
		resultadoDados = randint (1, 20)
		return resultadoDados


	def ataque_basico(self):#, enemigo):
		#danio = self.arma.dano
		#enemigo.setHp(enemigo.getHp - danio)		
		print("Ataque básico")

	def hechizo_1(self, mob, pj, consulta):#, enemigo):
		#danio = int(self.getInteligencia()* 0.7 + self.arma.dano)
		#enemigo.setHp (enemigo.getHp - danio)
		
		hechizo = hechizos.Hechizo(0,0,0,0,0)
		hechizo.escarcha_mistica(mob, consulta)
				
		return hechizo
		

	def hechizo_2 (self, mob, pj, consulta):#, enemigo) :
		#danio = int(self.getDestreza() * 0.7 + self.arma.dano)
		#enemigo.setHp (enemigo.getHp - danio)
		hechizo = hechizos.Hechizo(0,0,0,0,0)
		hechizo.flecha_fuego(mob, consulta)
				
		return hechizo

	def hechizo_3(self, mob, pj, consulta):#, enemigo) :
		#danio = int(self.getFuerza () * 0.7 + self.arma.dano)
		#enemigo.setHp (enemigo.getHp - danio)
		hechizo = hechizos.Hechizo(0,0,0,0,0)
		hechizo.cura_celestial(pj, consulta)
				
		return hechizo

	def SubirNivel(self):
		self.nivel += 1
		self.subirNivel(self.nivel)

	def cambiarArmadura(self):
		pass

	def cambiarArma(self):
		pass

	def getNombre(self):	
		return self.nombre

	def getNivel(self):
		return self.nivel

	def getClase(self):
		return self.clase.name


