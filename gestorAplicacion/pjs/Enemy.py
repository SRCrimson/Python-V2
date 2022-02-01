import string
from random import randint

from gestorAplicacion.pjs.NPC import NPC
from gestorAplicacion.pjs.Clase import Clase
##import java.io.Serializable;

#from gestorAplicacion.Loadout.Inventario import Inventario
#from gestorAplicacion.Loadout.Armadura import Armadura
#from gestorAplicacion.Loadout.Arma import Arma


class Enemy():     #serializable

	min = 1
	max = 20

	nombre, dano, AC, HP, FUE, DES, CON, INT, SAB, CAR, descripcion = 0,0,0,0,0,0,0,0,0,0,0
	def __init__(self,nombre="Monstruo de prueba",HP=20,AC=6,FUE=12,DES=12,CON=12,INT=12,SAB=12,CAR=12): #Jugador por defecto
		self.nombre = nombre
		self.AC = AC
		self.HP = HP
		self.FUE = FUE
		self.DES = DES
		self.CON = CON
		self.INT = INT
		self.SAB = SAB
		self.CAR = CAR
		self.descripcion = ""

	def goblin(self):
		self.nombre = "Goblin"
		self.nivel = 1
		self.AC = 10
		self.HP = 10
		self.FUE = 10
		self.DES = 10
		self.CON = 10
		self.INT = 10
		self.SAB = 10
		self.CAR = 10
		self.descripcion = "Goblin feo y maloliente"
		self.dano = 2

	
	def trasgo(self):
		self.AC = 12
		self.HP = 12
		self.FUE = 12
		self.DES = 12
		self.CON = 12
		self.INT = 12
		self.SAB = 12
		self.CAR = 12
		self.descripcion = "Trasgo de las cavernas de Dor-magren"
	
	
	def golem(self):
		self.AC = 14
		self.HP = 14
		self.FUE = 14
		self.DES = 14
		self.CON = 14
		self.INT = 14
		self.SAB = 14
		self.CAR = 14
		self.descripcion = "Golem de arena"

	def lanzarDados(self) :
		resultadoDados = randint (1, 20)
		return resultadoDados


	def ataque_basico(self, mob):#, enemigo):
		#danio = self.arma.dano
		#enemigo.setHp(enemigo.getHp - danio)
		print(mob + "realizó Ataque básico")

	def hechizo_1(self, mob):#, enemigo):
		#danio = int(self.getInteligencia()* 0.7 + self.arma.dano)
		#enemigo.setHp (enemigo.getHp - danio)
		print(mob + " lanzó Hechizo 1")

	def hechizo_2 (self,mob):#, enemigo) :
		#danio = int(self.getDestreza() * 0.7 + self.arma.dano)
		#enemigo.setHp (enemigo.getHp - danio)
		print(mob + " lanzó Hechizo 2")

	def hechizo_3(self, mob):#, enemigo) :
		#danio = int(self.getFuerza () * 0.7 + self.arma.dano)
		#enemigo.setHp (enemigo.getHp - danio)
		print(mob + " lanzó Hechizo 3")


	def getNombre(self):	
		return self.nombre

