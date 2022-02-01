class Pocion:
    def __init__(self,nombre,descripcion,curacion,precio):
        self.nombre      = nombre
        self.descripcion = descripcion
        self.curacion    = curacion 
        self.precio      = precio

         
    def get_curacion(self):
        return self.curacion