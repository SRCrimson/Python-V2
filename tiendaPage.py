import os
import tkinter as tk
from tkinter import *
import os
import inicioPage
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
        Button(frame3, text="Armas",width=20,command=self.funarmas).grid(padx=5, row=0,column=0)
        Button(frame3, text="Armadura",width=20).grid(padx=5, row=0, column=1)
        Button(frame3, text="Pocion",width=20).grid(padx=5, row=0, column=2)
    def funarmas(self):
        filewin = Toplevel(self)
        frame4=tk.Frame(filewin, background="#CCE4CA",width=600,height=250)
        invLabel1 = tk.Label(frame4, text="Tienda",font=("Impact",16),fg="red",bg="#1C1C1C")
        invLabel1.grid(sticky=N,padx=20,pady=10)
        frame4.grid()
        filewin.grid()
