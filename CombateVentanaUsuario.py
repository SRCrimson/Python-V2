from cProfile import label
from cgitb import text
from math import comb
import os
from random import uniform
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from gestorAplicacion.mecanicas.Narrador import combate # JM
import gestorAplicacion.mecanicas.Narrador as narrador # JM
import gestorAplicacion.pjs.Player as player # JM
import gestorAplicacion.pjs.Enemy as Enemy #JM


window = tk.Tk()
window.title("Calabozos en la Nacho") #Zona 0
#window.geometry("1024x768")
window.resizable(width=False, height=False)
####Frames de ventana
frame1 = tk.Frame(window, background="#566573", bd=1, relief="sunken")
frame1.grid(sticky="nsew",padx=7, pady=3,row=0, column=0)
##ventana de inicio juego
framejugador= tk.Frame(frame1, background="#566573",width=600,height=250)
framejugador.grid()


##ventana de funcion Inventario
frameinventario=tk.Frame(frame1,background="#566573",bd=0, relief="sunken")
frame2= tk.Frame(frameinventario, background="#566573",width=400,height=200)
invLabel1 = tk.Label(frame2, text="Inventario",font=("Verdana",16))
invLabel1.grid(sticky=N,padx=20,pady=10)
invLabel2 = tk.Label(frame2, text="Descripción\nsdaf",font=("Verdana",16))
invLabel2.grid(padx=20,pady=10)
frame3= tk.Frame(frameinventario, background="#CCE4CA",width=600,height=250)
frame4=tk.Frame(frameinventario, background="#CCE4CA",width=600,height=250)
frame2.grid(padx=20, pady=10)
frame3.grid(padx=20, pady=10)
frame4.grid()

##ventana de funcion Combate


frameCombate=tk.Frame(frame1,background="#566573",bd=0, relief="sunken")
frame5= tk.Frame(frameCombate, background="#566573",width=400,height=200)
comLabel1 = tk.Label(frame5, text="Combate",font=("Verdana",16))
comLabel1.grid(padx=20,pady=10)
comLabel2 = tk.Label(frame5, text="Descripción",font=("Verdana",16))
comLabel2.grid(padx=20,pady=10)
frame6= tk.Frame(frameCombate, background="#CCE4CA",width=400,height=200)
frame6.pack_propagate(False) # JM
frame7= tk.Frame(frameCombate, background="#CCE4CA",width=400,height=200)
frame7.pack_propagate(False) # JM
frame5.grid(padx=20, pady=10)
frame6.grid(padx=20, pady=10)
frame7.grid()

frameNar = tk.Frame(frame6, background="#FFF0C1", width=150, height=200) # JM
frameNar.pack(side="right") # JM
frameNar.pack_propagate(False) # JM
frameScroll = tk.Scrollbar(frameNar) # JM
frameScroll.pack(side = RIGHT, fill = Y) # JM
labelNar = tk.Text(frameNar, width = 29, height = 15, yscrollcommand = frameScroll.set,  font=("Helvetica", 8)) # JM

labelNar.insert(END,"Registro de batalla") # JM

labelNar.pack() # JM
frameScroll.config(command=labelNar.yview) # JM


def countdown(count): # JM
    label['text'] = "El combate iniciará en " + str(count) # JM
    if count >= 0:        # JM
        frame6.after(1000, countdown, count-1) # JM            
    else: # JM
        label.destroy()
        text = mob.nombre + " HP: " + str(mob.HP)
        
        labelMob.pack(side=TOP)
        combate.setTurno() # JM

pj = player.Player() # JM
mob = Enemy.Enemy() #JM
mob.goblin() # JM

label = tk.Label(frame6) # JM
label.pack(side=TOP)  # JM
textPJ = pj.nombre + " HP: " + str(pj.HP) + " MP: " +str(pj.MP) # JM
labelPJ = tk.Label(frame6, text=textPJ) # JM
labelPJ.pack(side=BOTTOM) # JM
text = mob.nombre + " HP: " + str(mob.HP)
labelMob = tk.Label(frame6, text=text)
labelMob.pack(side=TOP)
combate = narrador.combate(pj, mob, frame7, frame6, labelNar, labelPJ, labelMob) # JM






##ventana de funcion Narrador
frameNarrador=tk.Frame(frame1,background="#566573",bd=0, relief="sunken")
frame8= tk.Frame(frameNarrador, background="#566573",width=400,height=200)
narrLabel1 = tk.Label(frame8, text="Narrador",font=("Verdana",16))
narrLabel1.grid(padx=20,pady=10)
narrLabel2 = tk.Label(frame8, text="Descripción",font=("Verdana",16))
narrLabel2.grid(padx=20,pady=10)
frame9= tk.Frame(frameNarrador, background="#CCE4CA",width=400,height=200)
frame10= tk.Frame(frameNarrador, background="#CCE4CA",width=400,height=200)
frame8.grid(padx=20, pady=10)
frame9.grid(padx=20, pady=10)
frame10.grid()

##ventana de funcion Tienda
frameTienda=tk.Frame(frame1,background="#566573",bd=0, relief="sunken")
frame11= tk.Frame(frameTienda, background="#566573",width=400,height=200)
tiendaLabel1 = tk.Label(frame11, text="Tienda",font=("Verdana",16))
tiendaLabel1.grid(padx=20,pady=10)
tiendaLabel2 = tk.Label(frame11, text="Descripción",font=("Verdana",16))
tiendaLabel2.grid(padx=20,pady=10)
frame12= tk.Frame(frameTienda, background="#CCE4CA",width=400,height=200)
frame13= tk.Frame(frameTienda, background="#CCE4CA",width=400,height=200)
frame11.grid(padx=20, pady=10)
frame12.grid(padx=20, pady=10)
frame13.grid()

##ventana de funcion Crear personaje
frameCrear=tk.Frame(frame1,background="#566573",bd=0, relief="sunken")
frame14= tk.Frame(frameCrear, background="#566573",width=400,height=200)
crearLabel1 = tk.Label(frame14, text="Crear Personaje",font=("Verdana",16))
crearLabel1.grid(padx=20,pady=10)
crearLabel2 = tk.Label(frame14, text="Descripción\ng\ng",font=("Verdana",16))
crearLabel2.grid(padx=20,pady=10)
frame15= tk.Frame(frameCrear, background="#CCE4CA",width=400,height=200)
frame16= tk.Frame(frameCrear, background="red",width=600,height=250)
frame14.grid(padx=20, pady=10)
frame15.grid(padx=20, pady=10)
frame16.grid()
#frame15
Label(frame15, text="Nombre:").grid(pady=5, row=0, column=0)
Entry(frame15, width=40).grid(padx=5, row=0, column=1)
Label(frame15, text="Apellido:").grid( pady=5, row=1, column=0)
Entry(frame15, width=40).grid(padx=5, row=1, column=1)
#elegir clase
Label(frame15, text="CLASE:").grid( pady=5, row=2, column=0)

Button(frame15, text="GUERRERO").grid(padx=5, row=2, column=1)
frameguerrero=Frame(frame15,width=50,height=50).grid(row=3,column=1)
imgmago = PhotoImage(file='photos/eider_img1.gif') # definir imagen
label1 = Label(frameguerrero)
label1.photo=imgmago

Button(frame15, text="MAGO").grid(padx=5, row=3, column=2)
Button(frame15, text="AQUERO").grid(padx=5, row=3, column=3)
Button(frame15, text="Aceptar", width=50).grid(padx=10, pady=10, row=4, column=0, columnspan=3)
'''
labelmago=Label(frame15,width=20,height=20)
imgmago = PhotoImage(file='photos/mago1.gif') # definir imagen
labelmago['image'] = imgmago
labelmago.grid()
Button(frame15, text="MAGO").grid(padx=5, row=3, column=2)

labelArquero=Label(frame15,width=20,height=20)
Button(frame15, width=40).grid(padx=5, row=0, column=1)
imgarquero = PhotoImage(file='photos/arquero.gif') # definir imagen
labelArquero['image'] = imgarquero
labelArquero.gridd(pady=5, row=2, column=3)
Button(frame15, text="AQUERO").grid(padx=5, row=3, column=3)
Button(frame15, text="Aceptar", width=50).grid(padx=10, pady=10, row=3, column=0, columnspan=3)'''


'''label = Label(frame15)
imgobj = PhotoImage(file='photos/eider_img1.gif') # definir imagen
label['image'] = imgobj
label.grid()'''



##Funciones de menu
mensajeAplicacion='''La aplicación es un demo jugable que rememora a los clásicos juegos de rol de texto, para ello implementaremos los conceptos de la programación orientada a objetos vistos en clase. Se desarrollará la narración en un clásico ecosistema de fantasía medieval, inspirado en el juego Calabozos & Dragones.'''
def evento():
    pass
def Aplicacion():
    messagebox.showinfo(title='Aplicación',
    message='Informacion Basica',
    detail=mensajeAplicacion)
def regresarInicio():
    frame1.grid()
def ayuda():
    messagebox.showinfo(title='Ayuda',
    message='Autores',
    detail='''Brayan David Caballero Fernández\nJohn Mauricio Mesa Echeverri\nEider Alejandro Peña Dagua\nSantiago Rivera Mejía''')

def funInventario():
    framejugador.grid_forget()
    frame1.grid()
    frameinventario.grid()
    frameCombate.grid_forget()
    frameNarrador.grid_forget()
    frameTienda.grid_forget()
    frameCrear.grid_forget()
def funCombate():
    framejugador.grid_forget()
    frame1.grid()
    frameinventario.grid_forget()
    frameCombate.grid()
    frameNarrador.grid_forget()
    frameTienda.grid_forget()
    frameCrear.grid_forget()
    combate.botonera()
    countdown(0) # JM
    
def funNarrador():
    framejugador.grid_forget()
    frame1.grid()
    frameinventario.grid_forget()
    frameCombate.grid_forget()
    frameNarrador.grid()
    frameTienda.grid_forget()
    frameCrear.grid_forget()
def funTienda():
    framejugador.grid_forget()
    frame1.grid()
    frameinventario.grid_forget
    frameCombate.grid_forget()
    frameNarrador.grid_forget()
    frameTienda.grid()
    frameCrear.grid_forget()
def funCrearpersonaje():
    framejugador.grid_forget()
    frame1.grid()
    frameinventario.grid_forget()
    frameCombate.grid_forget()
    frameNarrador.grid_forget()
    frameTienda.grid_forget()
    frameCrear.grid()


###botones de menu zona 1 en rojo
window.option_add('*tearOff', FALSE)
menubar = Menu(window)
window.config(menu=menubar)
menuArchivo= Menu(menubar)
menubar.add_cascade(menu=menuArchivo, label='Archivo', command=evento)
menuArchivo.add_command(label="Aplicación", command=Aplicacion)
menuArchivo.add_separator()
menuArchivo.add_command(label="Salir", command=regresarInicio)
menuProcesos= Menu(menubar)
menubar.add_cascade(menu=menuProcesos, label='Procesos y Consultas')
menuProcesos.add_command(label="Inventario",command=funInventario)
menuProcesos.add_command(label="Combate", command=funCombate)
menuProcesos.add_command(label="Narrador", command=funNarrador)
menuProcesos.add_command(label="Tienda", command=funTienda)
menuProcesos.add_command(label="Crear Personaje", command=funCrearpersonaje)

menuAyuda=Menu(menubar)
menubar.add_cascade(menu=menuAyuda,label="Ayuda")
menuAyuda.add_checkbutton(label="ayuda",command=ayuda)
window['menu'] = menubar



window.mainloop()