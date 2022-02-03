#from email.mime import image
import os
from random import uniform
import tkinter as tk
from tkinter import CENTER, LEFT, messagebox
from App import App

class bienvenida(tk.Tk):
    numero = 2
    def __init__(self):
        super().__init__()
        self.geometry("1280x720")
        self.title("Calabozos en la Nacho")
        #self.geometry("500x350")
        self.config(bg="black")
        self.__create_widgets()

    def __create_widgets(self):
        self.resizable(width=False, height=False)
        p1Frame = tk.Frame(self, background="#202020", bd=30, relief="sunken")
        p2Frame = tk.Frame(self, background="#202020", bd=30, relief="sunken")
        p1Frame.grid(row=1, column=0, sticky="nsew", padx=0, pady=0)
        p2Frame.grid(row=1, column=1, sticky="nsew", padx=0, pady=0)
        base_folder = os.path.dirname(__file__)
        # Centrar
        p1Frame.rowconfigure(0, weight=1)
        p1Frame.columnconfigure(0, weight=1)
        p2Frame.rowconfigure(0, weight=1)
        p2Frame.columnconfigure(0, weight=1)


        p3Frame = tk.Frame(p1Frame, background="#808080", width=400, height=200)
        p3Frame.grid(padx=20, pady=10)
        p3Frame.grid_propagate(0)
        p3Label = tk.Label(p3Frame, text="Bienvenida")
        p3Label.pack(expand=True)
        p3Frame.pack_propagate(False)

        p4Frame = tk.Frame(p1Frame, background="#404040", width=400, height=500)

        p4Frame.grid(padx=20, pady=10)
        p4Frame.grid_propagate(0)
        p4Frame.pack_propagate(False)
        self.actualDeveloper = "john"

        
        def imgAsoc(event, num, photo_):
            global numero
            photo_.config(image="")
            if self.numero <=4:
                self.numero += 1
            else:
                self.numero = 1

            img = os.path.join(base_folder, 'photos/as'+str(num)+'.gif')
            imgPI = tk.PhotoImage(file=img)
            photo_ = tk.Label(p41Frame, image=imgPI)
            photo_.photo = imgPI
            photo_.grid(row=0, column=0, padx=0, pady=0)
                

        """p4Label = tk.Label(text="asdas")
        p4Label.grid()
        p4Label.bind("<Button-1>", lambda event:imgAsoc(event, numero))"""



        p41Frame = tk.Frame(p4Frame)
        p41Frame.pack()
        img = os.path.join(base_folder, 'photos/as1.gif')
        imgPI = tk.PhotoImage(file=img)
        photo_ = tk.Label(p41Frame, image=imgPI)
        photo_.photo = imgPI
        photo_.grid(row=0, column=0)
        photo_.rowconfigure(0, weight=1)
        photo_.columnconfigure(0, weight=1)
        p41Frame.bind('<Enter>', lambda event:imgAsoc(event,self.numero, photo_))

        descripcion = """Este relato contiene muchas elecciones: las hay sencillas, sensatas, temerarias... e incluso muy peligrosas.

        Estas elecciones las encontrarás siempre al final de cada narración.

        Decide entre uno u otro camino escribiendo '1' o '2' según corresponda y presionando a continuación la tecla 'Enter'.

        Puedes realizar otras acciones usando comandos especiales. Puedes ver una lista de comandos escribiendo: help"""

        enterButton = tk.Button(p4Frame, text="JUGAR YA",command=lambda :pageusuario(self))
        enterButton.pack(side="bottom")
        p4Label = tk.Label(p4Frame, text=descripcion, wraplength=290, anchor='e', justify='left', padx=20,pady=20)
        p4Label.pack(side="bottom")


        def imgSel(developer):
            
            p1 = os.path.join(base_folder, 'photos/'+developer+'_img1.gif')
            p2 = os.path.join(base_folder, 'photos/'+developer+'_img2.gif')
            p3 = os.path.join(base_folder, 'photos/'+developer+'_img3.gif')
            p4 = os.path.join(base_folder, 'photos/'+developer+'_img4.gif')
            img1 = tk.PhotoImage(file=p1)
            img2 = tk.PhotoImage(file=p2)
            img3 = tk.PhotoImage(file=p3)
            img4 = tk.PhotoImage(file=p4)
            
            photo1 = tk.Label(p6Frame, image=img1)
            photo1.photo = img1
            photo1.grid(row=0, column=0, padx=15, pady=15)

            photo2 = tk.Label(p6Frame, image=img2)
            photo2.photo = img2
            photo2.grid(row=0, column=1, padx=15, pady=15)

            photo3 = tk.Label(p6Frame, image=img3)
            photo3.photo = img3
            photo3.grid(row=1, column=0, padx=15, pady=15)

            photo3 = tk.Label(p6Frame, image=img4)
            photo3.photo = img4
            photo3.grid(row=1, column=1, padx=15, pady=15)
            

        def clicked(event):
            if self.actualDeveloper == "john":
                self.actualDeveloper = "eider"
                imgSel(self.actualDeveloper)
                p5Label.config(text = pjEider)
            elif self.actualDeveloper == "eider":
                self.actualDeveloper = "brayan"
                imgSel(self.actualDeveloper)
                p5Label.config(text = pjBrayan)
            elif self.actualDeveloper == "brayan":
                self.actualDeveloper = "santiago"
                imgSel(self.actualDeveloper)
                p5Label.config(text = pjSantiago)
            else:
                self.actualDeveloper = "john"
                imgSel(self.actualDeveloper)
                p5Label.config(text = pjJohn)

        pjJohn = "Nombre: John Mauricio\nApellidos: Mesa Echeverri\nEdad: 32\nPregrado: Ciencias de la computación"
        pjEider = "Nombre: Eider Alejandro\nApellidos: Peña Dagua\nEdad: 23\nPregrado: Ing Sistemas e Informatica"
        pjSantiago = "Nombre: Santiago\nApellidos: Rivera Mejia\nEdad: 21\nPregrado: Ciencias de la computación"
        pjBrayan = "Hoja de vida de Brayan"

        p5Frame = tk.Frame(p2Frame, background="#808080", width=400, height=200)
        p5Frame.grid(padx=20, pady=10)
        p5Frame.grid_propagate(0)
        p5Label = tk.Label(p5Frame, text=pjJohn)
        p5Label.pack(expand=True)



        p5Frame.bind("<Button-1>", lambda event:clicked(event))
        p5Label.bind("<Button-1>", lambda event:clicked(event))
        p5Frame.pack_propagate(False)





        p6Frame = tk.Frame(p2Frame, background="#FFF0C1", width=400, height=500)
        p6Frame.grid(padx=20, pady=10)
        p6Frame.grid_propagate(0)

        p6Frame.rowconfigure(0, weight=1)
        p6Frame.columnconfigure(0, weight=1)



        imgSel(self.actualDeveloper)

        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1, uniform="fred")
        self.grid_columnconfigure(1, weight=1, uniform="fred")

        varGuiaJuego = """Acá va la guía para aprender a jugar

        Acá va la guía para aprender a jugar

        Acá va la guía para aprender a jugar

        Acá va la guía para aprender a jugar
        """

        def guiaJuego():
            p4Label.config(text=varGuiaJuego)
        def doNothing():
            pass
        menuBar = tk.Menu(self)
        fileMenu = tk.Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="Descripción", command=guiaJuego)
        fileMenu.add_separator()
        fileMenu.add_command(label="Salir", command=doNothing)
        menuBar.add_cascade(label = "Inicio", menu = fileMenu)
        self.config(menu = menuBar)
        

        def pageusuario(self):
            self.destroy()
            if __name__ == "__main__":
                apusu = App()
                apusu.mainloop()
                self.destroy()

if __name__ == "__main__":
    app = bienvenida()
    app.mainloop()
