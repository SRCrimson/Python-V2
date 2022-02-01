import tkinter as tk
from tkinter import ttk,messagebox
from tkinter import *
import sys
from tkinter.messagebox import showinfo


class FieldFrame(ttk.Frame):
    def __init__(self,container,tituloCriterios, criterios, tituloValores, valores, habilitado):
        super().__init__(container)
        # setup the grid layout manager
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)
        
        self.__create_widgets()

    def __create_widgets(self):
        # Find what
        ttk.Label(self, text='Codigo:').grid(column=0, row=1, sticky=tk.W)
        keyword = ttk.Entry(self, width=30)
        keyword.focus()
        keyword.grid(column=1, row=1, sticky=tk.W)

        # Replace Nombre:
        ttk.Label(self, text='Nombre:').grid(column=0, row=2, sticky=tk.W)
        replacement = ttk.Entry(self, width=30)
        replacement.grid(column=1, row=2, sticky=tk.W)


        for widget in self.winfo_children():
            widget.grid(padx=0, pady=5)


class ButtonFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)

        self.__create_widgets()

    def __create_widgets(self):
        ttk.Button(self, text='Criterios').grid(column=0, row=0)
        ttk.Button(self, text='Valor').grid(column=1, row=0)
        ttk.Button(self, text='Aceptar').grid(column=0, row=5)
        ttk.Button(self, text='Borrar').grid(column=1, row=5)

        for widget in self.winfo_children():
            widget.grid(padx=0, pady=3)











mensajeAplicacion='''La aplicación es un demo jugable que rememora a los clásicos juegos de rol de texto, para ello implementaremos los conceptos de la programación orientada a objetos vistos en clase. Se desarrollará la narración en un clásico ecosistema de fantasía medieval, inspirado en el juego Calabozos & Dragones.'''
def Aplicacion():
    messagebox.showinfo(title='Aplicación',
    message='Informacion Basica',
    detail=mensajeAplicacion)

def ayuda():
    messagebox.showinfo(title='Ayuda',
    message='Autores',
    detail='''Brayan David Caballero Fernández\nJohn Mauricio Mesa Echeverri\nEider Alejandro Peña Dagua\nSantiago Rivera Mejía''')


class MenuBar(tk.Menu):
    def __init__(self, container):
        super().__init__(container)
        # setup the grid layout manager
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)

        self.__create_widgets()

    def __create_widgets(self):
        tk.Menu.__init__(self)
        menuArchivo = tk.Menu(self, tearoff=False)
        self.add_cascade(menu=menuArchivo,label='Archivo')
        menuArchivo.add_command(label="Aplicación", command=Aplicacion)
        menuArchivo.add_command(label="Salir", command=self.regresarInicio)
        menuProcesos= tk.Menu(self, tearoff=False)
        self.add_cascade(menu=menuProcesos, label='Procesos y Consultas')
        menuProcesos.add_command(label="Inventario",command=self.funInventario)
        menuProcesos.add_command(label="Combate", command=self.funCombate)
        menuProcesos.add_command(label="Narrador", command=self.funNarrador)
        menuProcesos.add_command(label="Tienda", command=self.funTienda)
        menuProcesos.add_command(label="Crear Personaje", command=self.funCrearpersonaje)
        menuayuda = tk.Menu(self, tearoff=False)
        self.add_cascade(label="Ayuda",menu=menuayuda)
        menuayuda.add_command(label="Ayuda", command=ayuda)

    def quit(self):
        sys.exit(0)

    def regresarInicio():
        pass
    def funInventario(self):
        filewin = Toplevel(self)
        frameinventario=tk.Frame(filewin,background="#566573",bd=0, relief="sunken")
        frameinventario.grid()
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

    def funCombate(self):
        filewin = Toplevel(self)
        frameCombate=tk.Frame(filewin,background="#566573",bd=0, relief="sunken")
        frameCombate.grid()
        frame5= tk.Frame(frameCombate, background="#566573",width=400,height=200)
        comLabel1 = tk.Label(frame5, text="Combate",font=("Verdana",16))
        comLabel1.grid(padx=20,pady=10)
        comLabel2 = tk.Label(frame5, text="Descripción",font=("Verdana",16))
        comLabel2.grid(padx=20,pady=10)
        frame6= tk.Frame(frameCombate, background="#CCE4CA",width=400,height=200)
        frame7= tk.Frame(frameCombate, background="#CCE4CA",width=400,height=200)
        frame5.grid(padx=20, pady=10)
        frame6.grid(padx=20, pady=10)
        frame7.grid()
    def funNarrador(self):
        filewin = Toplevel(self)
        frameNarrador=tk.Frame(filewin,background="#566573",bd=0, relief="sunken")
        frameNarrador.grid()
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
    def funTienda(self):
        filewin = Toplevel(self)
        frameTienda=tk.Frame(filewin,background="#566573",bd=0, relief="sunken")
        frameTienda.grid()
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
        
        
        # create the button frame
        button_frame = ButtonFrame(frame12)
        button_frame.grid()
        
        # create the input frame
        input_frame = FieldFrame(frame12,"Criterio", criterios, "Valor", None,habilitado)
        input_frame.grid()
    
    def funCrearpersonaje(self):
        filewin = Toplevel(self)
        frameCrear=tk.Frame(filewin,background="#566573",bd=0, relief="sunken")
        frameCrear.grid()
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

##pagina inicail
class inicioPage(tk.Frame):
    def __init__(self, container):
        super().__init__(container)

        frameinicio=tk.Frame(self,background="#2E363D",bd=0, relief="sunken")
        frameinicio.grid()
        frame2= tk.Frame(frameinicio, background="#566573",width=400,height=200)
        invLabel1 = tk.Label(frame2, text="pagina inicio jugador",font=("Verdana",16))
        invLabel1.grid(sticky=N,padx=20,pady=10)
        invLabel2 = tk.Label(frame2, text="Descripción\nsdaf",font=("Verdana",16))
        invLabel2.grid(padx=20,pady=10)
        frame3= tk.Frame(frameinicio, background="#CCE4CA",width=600,height=250)
        frame4=tk.Frame(frameinicio, background="#CCE4CA",width=600,height=250)
        frame2.grid(padx=20, pady=10)
        frame3.grid(padx=20, pady=10)
        frame4.grid()
  


### CLASE APP ES LA VENTANA PRINCIPAL
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calabozos en la Nacho")
                # creating a frame and assigning it to container
       
        self.__create_widgets()
    def __create_widgets(self):
        # create the menu
        menubar = MenuBar(self)
        self.config(menu=menubar)
        input_frame = inicioPage(self)
        input_frame.grid()



##valores por defecto para el formulario
criterios = ["Codigo", "Nombre", "Descripción", "Ubicación"]
valores=[]
habilitado=[]
#fp = FieldFrame ("Criterio", criterios, "Valor", None)
##corre la interfaz
if __name__ == "__main__":
    app = App()
    app.mainloop()