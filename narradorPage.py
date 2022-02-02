import os
import tkinter as tk
from tkinter import *
import os
class narradorPage(tk.Frame):
    def __init__(self, container,labeltext):
        super().__init__(container)

        frameinventario=tk.Frame(self,background="#1C1C1C",bd=0, relief="sunken")
        frameinventario.grid()
        frame2= tk.Frame(frameinventario, background="#1C1C1C",width=400,height=200)
        invLabel1 = tk.Label(frame2, text="Narrador",font=("Impact",16),fg="red",bg="#1C1C1C")
        invLabel1.grid(sticky=N,padx=20,pady=10)
        invLabel2 = tk.Label(frame2, text="Descripción\nsdaf",font=("Verdana",16))
        invLabel2.grid(padx=20,pady=10)
        frame3= tk.Frame(frameinventario, background="#CCE4CA",width=600,height=250)
        frame4=tk.Frame(frameinventario, background="#CCE4CA",width=600,height=250)
        frame2.grid(padx=20, pady=10)
        frame3.grid(padx=20, pady=10)
        frame4.grid()