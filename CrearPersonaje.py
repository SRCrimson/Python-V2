import tkinter as tk
import os
from gestorAplicacion.pjs.Player import Player
import matplotlib.font_manager as fm

class NuevoPj():

    def __init__(self, crear_personaje):
        rootDir = os.getcwd ()
        path= str (rootDir) + "\game_over\game_over.ttf"
        font_files = fm.findSystemFonts (fontpaths=path)
        font_list = fm.createFontList (font_files)
        fm.fontManager.ttflist.extend (font_list)
        fm.rcParams['font.family'] = 'Game over'

        self.crear_personaje = crear_personaje
        self.crear_personaje.geometry("1080x600")
        self.crear_personaje.title("Seleccionar clase")
        self.crear_personaje.config(bg="black")

        self.frame1=tk.Frame(master=self.crear_personaje, height= 120, bg="black")
        self.frame1.place(relx=0,rely=0, relwidth=1, relheight=0.2)

        self.frame2 = tk.Frame(master=self.crear_personaje)
        self.frame2.config(bd=12, relief="sunken")
        self.frame2.place( relx=0.05, rely = 0.2, relwidth=0.3, relheight=0.64)

        self.frame3 = tk.Frame(master=self.crear_personaje)
        self.frame3.config(bd=12, relief="sunken")
        self.frame3.place( relx=0.35, rely = 0.2, relwidth=0.31, relheight=0.64)

        self.frame4 = tk.Frame(master=self.crear_personaje)
        self.frame4.place( relx=0.66, rely = 0.2,  relwidth=0.29, relheight=0.64)
        self.frame4.config(bd=12, relief="sunken")


        self.titulo=tk.Label(master=self.frame1,text="Elige una clase, aventurero", font=("Game over", 48), fg="red", bg="black")
        self.titulo.place(relx=0.36, rely=0.5)

        rootDir = os.getcwd ()
        imgDir = str (rootDir) + "\photos"
        base_folder = imgDir


        self.guerrero1 = os.path.join(base_folder, "guerrero1.gif")
        self.imgGuerrero= tk.PhotoImage(file=self.guerrero1)


        self.arquero1 = os.path.join(base_folder, "arquero1.gif")
        self.imgArquero= tk.PhotoImage(file=self.arquero1)

        self.mago1 = os.path.join(base_folder, "mago.gif")
        self.imgMago= tk.PhotoImage(file=self.mago1)


        self.btnGuerrero=tk.Button(master=self.frame2,image=self.imgGuerrero, command=lambda :personaje(1)).pack()
        self.btnArquero=tk.Button(master=self.frame3, image=self.imgArquero, command=lambda :personaje(2)).pack()
        self.btnMago=tk.Button(master=self.frame4, image=self.imgMago, command=lambda :personaje(3)).pack()


        self.txtGuerrero=tk.Label(master=self.crear_personaje, text="Guerrero", font=("Game over", 40), bg="black", fg="white").place(rely=0.84, relx=0.17)
        self.txtArquero=tk.Label(master=self.crear_personaje, text="Arquero", font=("Game over", 40), bg="black", fg="white").place(rely=0.84, relx=0.48)
        self.txtMago=tk.Label(master=self.crear_personaje, text="Mago", font=("Game over", 40), bg="black", fg="white").place(rely=0.84, relx=0.79)

        def personaje(eleccion):
            clase=eleccion
            diclase= {1:'Guerrero', 2:'Arquero', 3:'Mago'}
            datos=tk.Toplevel()
            datos.title("Crea tu personaje")
            self.crear_personaje
            crear_personaje.iconify()

            Dir = os.getcwd ()
            img = str (Dir) + "\photos"
            fondo = os.path.join (img, "fondo.gif")
            imgfondo = tk.PhotoImage (file=fondo)

            datos.geometry("1200x680")
            bg= tk.Label(master=datos, image=imgfondo).pack()

            fondo2= os.path.join (img, "papel.gif")
            imgfondo2=tk.PhotoImage(file=fondo2)

            frame_datos=tk.Frame(master=datos)
            frame_datos.place(relx=0.30, rely=0, relwidth=0.4, relheight=1)
            frame_datos.config(bd=10, relief="ridge")



            lblfondo=tk.Label(master=frame_datos, image=imgfondo2).pack()

            back=tk.Button(master= frame_datos, text='Volver', font=('Game over', 40))
            back.place(relx=0.2, rely=0.9, relwidth=0.22)

            title = tk.Label (master=frame_datos, text='Datos del personaje', font=("Game over", 55), bg='#e7dfd2')
            title.place (relx=0.24, rely=0.08)

            nombre= tk.Label(master=frame_datos, text='Nombre', font=("Game over", 50),bg='#e7dfd2').place(relx=0.2, rely=0.2)
            entreda_nombre=tk.Entry(master=frame_datos)
            entreda_nombre.place(relx=0.55, rely=0.205, relwidth=0.3, relheight=0.05)
            entreda_nombre.config(bd=2, relief='sunken', font=42)

            apellido= tk.Label(master=frame_datos, text='Apellido',font=("Game over", 50),bg='#e7dfd2').place(relx=0.2, rely=0.4)
            entreda_apellido = tk.Entry (master=frame_datos)
            entreda_apellido.place (relx=0.55, rely=0.405, relwidth=0.3, relheight=0.05)
            entreda_apellido.config (bd=2, relief='sunken', font=42)

            edad = tk.Label (master=frame_datos, text='Edad', font=("Game over", 50),bg='#e7dfd2').place (relx=0.2, rely=0.6)
            entreda_edad = tk.Entry (master=frame_datos)
            entreda_edad.place (relx=0.55, rely=0.605, relwidth=0.3, relheight=0.05)
            entreda_edad.config (bd=2, relief='sunken', font=42)

            lbl_clase=tk.Label(master=frame_datos, text='Clase: ', font=("Game over", 50),bg='#e7dfd2').place (relx=0.32, rely=0.75)
            lbl_clase = tk.Label (master=frame_datos, text=diclase[clase], font=("Game over", 50), bg='#e7dfd2').place(relx=0.48, rely=0.75)

            def crear():
                player=Player()
                namepj=entreda_nombre.get() + entreda_apellido.get()
                edadpj= entreda_edad.get()
                player.Jugador(namepj, edadpj, clase)



            continuar=tk.Button(master=frame_datos, text='Continuar', command=crear(), font=('Game over', 40) ).place(relx=0.58, rely=0.9, relwidth=0.22)

            datos.mainloop()


    def destruir(self):
        self.crear_personaje.destroy()


    def volver(self):

        self.crear_personaje.deiconify()



if __name__=="__main__":

    root=tk.Tk()
    NuevoPj(root)
    root.mainloop()