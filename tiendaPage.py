import os
import tkinter as tk
from tkinter import *
import os
from gestorAplicacion.pjs.Clase import Clase
from gestorAplicacion.pjs.Player import Player
import inicioPage
from gestorAplicacion.Loadout.Tienda import Tienda

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
        if Player.clase == 1:
            Button(frame3, text="Armas",width=20,command=self.ShowArmasWarrior).grid(padx=5, row=0,column=0)
        elif pj  == Clase.ARQUERO:
            Button(frame3, text="Armas",width=20,command=self.ShowArmasArcher).grid(padx=5, row=0,column=0)
        else: #Player.clase  == Clase.MAGO:
            Button(frame3, text="Armas",width=20,command=self.ShowArmasMage).grid(padx=5, row=0,column=0)
        Button(frame3, text="Armadura",width=20).grid(padx=5, row=0, column=1)
        Button(frame3, text="Pocion",width=20).grid(padx=5, row=0, column=2)

    def ShowArmasWarrior(self):
        filewin  = Toplevel(self)
        frame4   = tk.Frame(filewin, background="#1C1C1C",width=600,height=250)
        BW1      = Button(frame4, text=Tienda.W1.nombre + ": " +Tienda.W1.descripcion + " $" + str(Tienda.W1.precio))
        BW2      = Button(frame4, text=Tienda.W2.nombre + ": " +Tienda.W2.descripcion + " $" + str(Tienda.W2.precio))
        BW3      = Button(frame4, text=Tienda.W3.nombre + ": " +Tienda.W3.descripcion + " $" + str(Tienda.W3.precio))
        frame4.grid()
        BW1.grid()
        BW2.grid() 
        BW3.grid()
       
    def ShowArmasArcher(self):
        filewin  = Toplevel(self)
        frame4   = tk.Frame(filewin, background="#1C1C1C",width=600,height=250)
        BW1      = Button(frame4, text=Tienda.A1.nombre + ": " +Tienda.A1.descripcion + " $" + str(Tienda.A1.precio))
        BW2      = Button(frame4, text=Tienda.A2.nombre + ": " +Tienda.A2.descripcion + " $" + str(Tienda.A2.precio))
        BW3      = Button(frame4, text=Tienda.A3.nombre + ": " +Tienda.A3.descripcion + " $" + str(Tienda.As3.precio))
        frame4.grid()
        BW1.grid()
        BW2.grid() 
        BW3.grid()
       
    def ShowArmasMage(self):
        #print(pj.clase)
        filewin  = Toplevel(self)
        frame4   = tk.Frame(filewin, background="#1C1C1C",width=600,height=250)
        BW1      = Button(frame4, text=Tienda.M1.nombre + ": " +Tienda.M1.descripcion + " $" + str(Tienda.M1.precio))
        BW2      = Button(frame4, text=Tienda.M2.nombre + ": " +Tienda.M2.descripcion + " $" + str(Tienda.M2.precio))
        BW3      = Button(frame4, text=Tienda.M3.nombre + ": " +Tienda.M3.descripcion + " $" + str(Tienda.M3.precio))
        frame4.grid()
        BW1.grid()
        BW2.grid() 
        BW3.grid()

    