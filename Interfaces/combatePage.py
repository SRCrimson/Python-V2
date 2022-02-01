import os
import tkinter as tk
from tkinter import *
import os
class CombatePage(tk.Frame):
    def __init__(self, container,labeltext):
        super().__init__(container)

        
        frameCombate=tk.Frame(self,background="#1C1C1C",bd=0, relief="sunken")
        frameCombate.grid()
        frame5= tk.Frame(frameCombate, background="#1C1C1C",width=400,height=200)
        comLabel1 = tk.Label(frame5, text="Combate",font=("Impact",16),fg="red",bg="#1C1C1C")
        comLabel1.grid(padx=20,pady=10)
        comLabel2 = tk.Label(frame5, text="Descripción",font=("Verdana",16))
        comLabel2.grid(padx=20,pady=10)
        frame6= tk.Frame(frameCombate, background="#CCE4CA",width=400,height=200)
        frame7= tk.Frame(frameCombate, background="#CCE4CA",width=400,height=200)
        frame5.grid(padx=20, pady=10)
        frame6.grid(padx=20, pady=10)
        frame7.grid()