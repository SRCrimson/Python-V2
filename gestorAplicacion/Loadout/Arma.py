class Arma:
    def __init__(self, nombre, descripcion, dano, precio):
        self.nombre      = nombre
        self.descripcion = descripcion
        self.dano        = dano 
        self.precio      = precio
 
  # getter method
    def get_dano(self):
        return self.dano