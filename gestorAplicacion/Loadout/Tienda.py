from pip      import main
from tkinter import *
from tkinter import ttk,messagebox
from . Arma import Arma
from . Armadura import Armadura
from . Pocion   import Pocion
from . Inventario import Inventario
import tiendaPage


def ayudaGood():
    messagebox.showinfo(title='Ayuda',
    message = 'Enhorabuena! compra exitosa!',)

def ayudaBad():
    messagebox.showinfo(title='Ayuda',
    message = 'No tienes suficiente dinero :c',)

class Tienda:
        
    W1 = Arma("Bisturi",   "De poco filo",       5, 25)
    W2 = Arma("Excalibur", "Espada legendaria", 10, 50)
    W3 = Arma("Ragnarok",  "World ender",       15, 100)
                
    A1 = Arma("Arco de Madera",  "Para alguien habil no resultara dificil usarlo",            5, 25)
    A2 = Arma("Arco Compuesto",  "Destaca por su precision y dureza",                        10, 50,)
    A3 = Arma("Azkar",  		 "Solo es posible usarlo en manos del el mas habil arquero", 15, 100)
                
    M1 = Arma("Baston de runas",   "Arma preferida por jovenes aprendices", 5, 25)
    M2 = Arma("Baston astral ",    "Pocos han podido emplearlo a su maximo potencial", 10, 50)
    M3 = Arma("Omnirod",           "Pasado de generacion en generacion, con poderes ocultos latentes", 15, 100)

    Armor1 = Armadura("Armadura de bronce", "De poco costo y dureza respetable", 5, 10)
    Armor2 = Armadura("Armadura de plata",  "Otorgada a distinguidos heroes por sus hazañas", 10, 20)
    Armor3 = Armadura("Armadura de Oro",    "Solo puede ser forjada una vez cada 100 años", 20, 40) 

    P1 = Pocion("Pocion Small",  "Otorga 10 de vida al jugador", 10, 10,)
    P2 = Pocion("Pocion Medium", "Otorga 25 de vida al jugador", 25, 20)
    P3 = Pocion("Pocion Large",  "Otorga la mitad de la vida al jugador", 50, 30)


    def comprarWarrior(nombre, wallet):
        if (nombre == '1')  and (wallet >= Tienda.W1.precio): 
            Inventario.InvArmas.append(Tienda.W1)
            tiendaPage.Jugador.wallet -= Tienda.W1.precio
            ayudaGood()
        elif (nombre == '2') and (wallet >= Tienda.W2.precio): 
            Inventario.InvArmas.append(Tienda.W2)
            tiendaPage.Jugador.wallet -= Tienda.W2.precio
            ayudaGood()
        elif (nombre == '3') and (wallet >= Tienda.W3.precio): 
            Inventario.InvArmas.append(Tienda.W3)
            tiendaPage.Jugador.wallet -= Tienda.W3.precio
            ayudaGood()
        else:
            print('not enough cash for swords')
            ayudaBad()

    def comprarArcher(nombre, wallet):
        if   (nombre == '1') and (wallet >= Tienda.A1.precio): #precio del arma
            Inventario.InvArmas.append(Tienda.A1)
            tiendaPage.Jugador.wallet -= Tienda.A1.precio
            ayudaGood()
        elif (nombre == '2') and (wallet >= Tienda.A2.precio): #precio del arma
            Inventario.InvArmas.append(Tienda.A2)
            tiendaPage.Jugador.wallet -= Tienda.A2.precio
            ayudaGood()
        elif (nombre == '3') and (wallet >= Tienda.A3.precio): #precio del arma
            Inventario.InvArmas.append(Tienda.A3)
            tiendaPage.Jugador.wallet -= Tienda.A3.precio
            ayudaGood()
        else:
            print('not enough cash for bows')
            ayudaBad()

    def comprarMage(nombre, wallet):
        if   (nombre == '1') and (wallet >= Tienda.M1.precio): #precio del arma
            Inventario.InvArmas.append(Tienda.M1)
            tiendaPage.Jugador.wallet -= Tienda.M1.precio
            ayudaGood()
        elif (nombre == '2') and (wallet >= Tienda.M2.precio): #precio del arma
            Inventario.InvArmas.append(Tienda.M2)
            tiendaPage.Jugador.wallet -= Tienda.M2.precio
            ayudaGood() 
        elif (nombre == '3') and (wallet >= Tienda.M3.precio): #precio del arma
            Inventario.InvArmas.append(Tienda.M3)
            tiendaPage.Jugador.wallet -= Tienda.M1.precio
        else:
            print('not enough cash for staves')
            ayudaBad()

    def comprarArmor(nombre, wallet):
        if   (nombre == '1') and (wallet >= Tienda.Armor1.precio): #precio del arma
            Inventario.InvArmaduras.append(Tienda.Armor1)
            tiendaPage.Jugador.wallet -= Tienda.Armor1.precio
            ayudaGood()
        elif (nombre == '2') and (wallet >= Tienda.Armor2.precio): #precio del arma
            Inventario.InvArmaduras.append(Tienda.Armor2)
            tiendaPage.Jugador.wallet -= Tienda.Armor2.precio
            ayudaGood()
        elif (nombre == '3') and (wallet >= Tienda.Armor3.precio): #precio del arma
            Inventario.InvArmaduras.append(Tienda.Armor3)
            tiendaPage.Jugador.wallet -= Tienda.Armor3.precio
            ayudaGood()
        else:
            print('not enough cash dude for armors')
            ayudaBad()

    def comprarPotion(nombre, wallet):
        if   (nombre == '1') and (wallet >= Tienda.P1.precio): #precio del arma
            Inventario.InvPociones.append(Tienda.P1)
            tiendaPage.Jugador.wallet -= Tienda.P1.precio
            ayudaGood()
        elif (nombre == '2') and (wallet >= Tienda.P2.precio): #precio del arma
            Inventario.InvPociones.append(Tienda.P2)
            tiendaPage.Jugador.wallet -= Tienda.P2.precio
            ayudaGood()
        elif (nombre == '3') and (wallet >= Tienda.P3.precio): #precio del arma
            Inventario.InvPociones.append(Tienda.P3)
            tiendaPage.Jugador.wallet -= Tienda.P2.precio
            ayudaGood()
        else:
            print('not enough cash for potions')
            ayudaBad()

