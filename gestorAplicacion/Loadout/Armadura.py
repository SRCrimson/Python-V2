class Armadura:
    def __init__(self,nombre,descripcion,defensa,precio):
        self.nombre      = nombre
        self.descripcion = descripcion
        self.defensa     = defensa
        self.precio      = precio

      # getter method
    def get_defensa(self):
        return self.defensa

    def cambiarDefensa(dano):
        Armadura.defensa -= dano
        return Armadura.defensa