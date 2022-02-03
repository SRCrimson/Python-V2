import tkinter as tk
from tkinter import ttk
from bd import registrarse3

class FieldFrame(ttk.Frame):
    def __init__(self,container,tituloCriterios, criterios, tituloValores, valores, habilitado):
        super().__init__(container)
        # definimos los titulos y las listas
        self.tituloCriterios=tituloCriterios
        self.criterios=criterios
        self.tituloValores=tituloValores
        self.valores=valores
        self.habilitado=habilitado
        
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)
        
        self.titulos()
        self.__create_widgets()
        self.botones()

    def titulos(self):
        ttk.Button(self, text=self.tituloCriterios).grid(column=0, row=0)
        ttk.Button(self, text=self.tituloValores).grid(column=1, row=0)

    def __create_widgets(self):
        # Find what
        criterio=self.criterios
        valor=self.valores
        hab=self.habilitado
        for i in range(0,len(criterio)):
            if valor[i]==None:
                if hab[i]==None:
                    ttk.Label(self, text=criterio[i]).grid(column=0, row=i+1, sticky=tk.W)
                    
                    self.keyword = ttk.Entry(self, width=30)
                    self.keyword.focus()
                    self.keyword.grid(column=1, row=1+i, sticky=tk.W)
                elif hab[i]=="*":
                    ttk.Label(self, text=criterio[i]).grid(column=0, row=i+1, sticky=tk.W)
                    self.keyword1= ttk.Entry(self, width=30,show = "*")
                    self.keyword1.focus()
                    self.keyword1.grid(column=1, row=1+i, sticky=tk.W)
                else:
                    ttk.Label(self, text=criterio[i]).grid(column=0, row=i+1, sticky=tk.W)
                    self.keyword2 = ttk.Entry(self, width=30,state=tk.DISABLED)
                    self.keyword2.focus()
                    self.keyword2.grid(column=1, row=1+i, sticky=tk.W)
            else:
                if hab[i]==None:
                    ttk.Label(self, text=criterio[i]).grid(column=0, row=i+1, sticky=tk.W)
                    self.keyword3 = ttk.Entry(self,width=30)
                    self.keyword3.insert(0,valor[i])
                    self.keyword3.focus()
                    self.keyword3.grid(column=1, row=1+i, sticky=tk.W)
                else:
                    ttk.Label(self, text=criterio[i]).grid(column=0, row=i+1, sticky=tk.W)
                    #mystr = tk.StringVar()
                    #mystr.set('username@xyz.com')
                    keyword4 = ttk.Entry(self,width=30)
                    keyword4.insert(0, valor[i])
                    keyword4.focus()
                    keyword4.config(state=tk.DISABLED)
                    keyword4.grid(column=1, row=1+i, sticky=tk.W)
                    

        for widget in self.winfo_children():
            widget.grid(padx=5, pady=5)


    def botones(self):
        self.botonaceptar=ttk.Button(self, text="Aceptar",command=lambda: registrarse3(self)).grid(column=0, row=len(self.criterios)+2)
        ttk.Button(self, text="Borrar").grid(column=1, row=len(self.criterios)+2)




