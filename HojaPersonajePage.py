
import tkinter as tk
from tkinter import *

class HojaPersonajePage (tk.Frame):
    def __init__(self, container,labeltext):
        super().__init__(container)

        framePersonaje=tk.Frame(self,background="#1C1C1C",bd=0, relief="sunken")
        framePersonaje.grid()
        frame2= tk.Frame(framePersonaje, background="#1C1C1C",width=400,height=200)
        invLabel1 = tk.Label(frame2, text="HOJA PERSONAJE",font=("Impact",16),fg="red",bg="#1C1C1C")
        invLabel1.grid(sticky=N,padx=20,pady=10)
        invLabel2 = tk.Label(frame2, text="Aqui se dara un breve resumen del personaje,\nmostrando su inventario sus habilidades, etc",
                            font=("Monaco",12),fg="white",bg="#1C1C1C",relief= "solid",justify= LEFT)
        invLabel2.grid(padx=20,pady=10)
        frame3= tk.Frame(framePersonaje, background="#CCE4CA",width=600,height=250)
        frame2.grid(padx=20, pady=10)
        label3 = tk.Label(frame3)
        frame3.grid(padx=20, pady=10)