from distutils import command
import tkinter as tk
from tkinter import *
from gestorAplicacion.pjs.Player import Player
from gestorAplicacion.Loadout.Tienda import Tienda
Jugador = Player()  

class tiendaPage(tk.Frame):

    def __init__(self, container,labeltext, pj):   
        super().__init__(container)   
        frameinventario=tk.Frame(self,background="#1C1C1C",bd=0, relief="sunken")
        frameinventario.grid()
        frame2= tk.Frame(frameinventario, background="#1C1C1C",width=400,height=200)
        invLabel1 = tk.Label(frame2, text="Tienda",font=("Impact",16),fg="red",bg="#1C1C1C")
        invLabel1.grid(sticky=N,padx=20,pady=10)
        invLabel2 = tk.Label(frame2, text="El jugador tendrá una tienda en donde podrá adquirir o vender \nartículos de tipo arma, poción y armadura. Esto se hace \ncon el fin de hacer más dinámico el juego ya que cada \nvez que se derrote a un enemigo, se obtendrá oro que podrá \nser utilizado para comprar e interactuar en la tienda ",
                    font=("Monaco",12),fg="white",bg="#1C1C1C",relief= "solid",justify= LEFT)
        invLabel2.grid(padx=20,pady=10)
        frame3= tk.Frame(frameinventario,bg="#1C1C1C",width=600,height=250)
        frame2.grid(padx=20, pady=10)
        frame3.grid(padx=20, pady=10)
        
        
        ##botones
        if  Player.clase.GUERRERO.__name__  == "GUERRERO":
            Button(frame3, text="Armas",width=20,command=self.ShowArmasWarrior).grid(padx=5, row=0,column=0)
        elif Player.clase.ARQUERO.__name__  == "ARQUERO":
            Button(frame3, text="Armas",width=20,command=self.ShowArmasArcher).grid(padx=5, row=0,column=0)
        elif Player.clase.MAGO.__name__     == "MAGO":
            Button(frame3, text="Armas",width=20,command=self.ShowArmasMage).grid(padx=5, row=0,column=0)
       
        Button(frame3, text="Armadura",width=20,command=self.ShowArmaduras).grid(padx=5, row=0, column=1)
        Button(frame3, text="Pocion",width=20,command=self.ShowPociones).grid(padx=5, row=0, column=2)

    def ShowArmasWarrior(self):
        filewin  = Toplevel(self)
        frame4   = tk.Frame(filewin, background="#1C1C1C",width=600,height=250)
        Button(frame4, text=Tienda.W1.nombre + ": " +Tienda.W1.descripcion + " $" + str(Tienda.W1.precio), command = lambda: Tienda.comprarWarrior('1', Jugador.getWallet())).grid()
        Button(frame4, text=Tienda.W2.nombre + ": " +Tienda.W2.descripcion + " $" + str(Tienda.W2.precio), command = lambda: Tienda.comprarWarrior('2', Jugador.getWallet())).grid()   
        Button(frame4, text=Tienda.W3.nombre + ": " +Tienda.W3.descripcion + " $" + str(Tienda.W3.precio), command = lambda: Tienda.comprarWarrior('3', Jugador.getWallet())).grid()
        frame4.grid()
       
    def ShowArmasArcher(self):
        filewin  = Toplevel(self)
        frame4   = tk.Frame(filewin, background="#1C1C1C",width=600,height=250)
        BA1      = Button(frame4, text=Tienda.A1.nombre + ": " +Tienda.A1.descripcion + " $" + str(Tienda.A1.precio))
        BA2      = Button(frame4, text=Tienda.A2.nombre + ": " +Tienda.A2.descripcion + " $" + str(Tienda.A2.precio))
        BA3      = Button(frame4, text=Tienda.A3.nombre + ": " +Tienda.A3.descripcion + " $" + str(Tienda.A3.precio))
        frame4.grid()
        BA1.grid()
        BA2.grid() 
        BA3.grid()
       
    def ShowArmasMage(self):
        filewin  = Toplevel(self)
        frame4   = tk.Frame(filewin, background="#1C1C1C",width=600,height=250)
        BM1      = Button(frame4, text=Tienda.M1.nombre + ": " +Tienda.M1.descripcion + " $" + str(Tienda.M1.precio))
        BM2      = Button(frame4, text=Tienda.M2.nombre + ": " +Tienda.M2.descripcion + " $" + str(Tienda.M2.precio))
        BM3      = Button(frame4, text=Tienda.M3.nombre + ": " +Tienda.M3.descripcion + " $" + str(Tienda.M3.precio))
        frame4.grid()
        BM1.grid()
        BM2.grid() 
        BM3.grid()

    def ShowArmaduras(self):
        filewin  = Toplevel(self)
        frame4   = tk.Frame(filewin, background="#1C1C1C",width=600,height=250)
        BAR1      = Button(frame4, text=Tienda.Armor1.nombre + ": " +Tienda.Armor1.descripcion + " $" + str(Tienda.Armor1.precio))
        BAR2      = Button(frame4, text=Tienda.Armor2.nombre + ": " +Tienda.Armor2.descripcion + " $" + str(Tienda.Armor2.precio))
        BAR3      = Button(frame4, text=Tienda.Armor3.nombre + ": " +Tienda.Armor3.descripcion + " $" + str(Tienda.Armor3.precio))
        frame4.grid()
        BAR1.grid()
        BAR2.grid() 
        BAR3.grid()
   
    def ShowPociones(self):
        filewin  = Toplevel(self)
        frame4   = tk.Frame(filewin, background="#1C1C1C",width=600,height=250)
        BP1      = Button(frame4, text=Tienda.P1.nombre + ": " +Tienda.P1.descripcion + " $" + str(Tienda.P1.precio))
        BP2      = Button(frame4, text=Tienda.P2.nombre + ": " +Tienda.P2.descripcion + " $" + str(Tienda.P2.precio))
        BP3      = Button(frame4, text=Tienda.P3.nombre + ": " +Tienda.P3.descripcion + " $" + str(Tienda.P3.precio))
        frame4.grid()
        BP1.grid()
        BP2.grid() 
        BP3.grid() 

       

    