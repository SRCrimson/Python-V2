from tkinter import *
import tkinter as tk
import photos
import os

crear_personaje = Tk()

crear_personaje.geometry("1080x600")
crear_personaje.title("Seleccionar clase")
crear_personaje.config(bg="black")

frame1=tk.Frame(master=crear_personaje, height= 120, bg="black")
frame1.place(relx=0,rely=0, relwidth=1, relheight=0.2)

frame2 = tk.Frame(master=crear_personaje)
frame2.config(bd=12, relief="sunken")
frame2.place( relx=0.05, rely = 0.2, relwidth=0.3, relheight=0.64)

frame3 = tk.Frame(master=crear_personaje)
frame3.config(bd=12, relief="sunken")
frame3.place( relx=0.35, rely = 0.2, relwidth=0.31, relheight=0.64)

frame4 = tk.Frame(master=crear_personaje)
frame4.place( relx=0.66, rely = 0.2,  relwidth=0.29, relheight=0.64)
frame4.config(bd=12, relief="sunken")




titulo=tk.Label(master=frame1,text="Elige una clase, aventurero", font=("Game over", 48), fg="red", bg="black")
titulo.place(relx=0.36, rely=0.5)

rootDir = os.path.dirname(os.path.dirname(os.getcwd()))
imgDir = str(rootDir)+"\photos"
base_folder = imgDir
guerrero1 = os.path.join(base_folder, "guerrero1.gif")
imgGuerrero= PhotoImage(file=guerrero1)

arquero1 = os.path.join(base_folder, "arquero1.gif")
imgArquero= PhotoImage(file=arquero1)

mago1 = os.path.join(base_folder, "mago.gif")
imgMago= PhotoImage(file=mago1)

btnGuerrero=tk.Button(master=frame2, image=imgGuerrero)
btnGuerrero.pack()

btnArquero=tk.Button(master=frame3, image=imgArquero).pack()

btnMago=tk.Button(master=frame4, image=imgMago).pack()

txtGuerrero=Label(master=crear_personaje, text="Guerrero", font=("Game over", 40), bg="black", fg="white").place(rely=0.84, relx=0.17)
txtArquero=Label(master=crear_personaje, text="Arquero", font=("Game over", 40), bg="black", fg="white").place(rely=0.84, relx=0.48)
txtMago=Label(master=crear_personaje, text="Mago", font=("Game over", 40), bg="black", fg="white").place(rely=0.84, relx=0.79)





crear_personaje.mainloop()