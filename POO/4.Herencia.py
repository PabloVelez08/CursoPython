# Herencia 

from re import sub


class Personaje:
    def __init__(self, nombre):
        self.nombre = nombre
    def registrado(self):
        print('Personaje registrado!!')

class SuperHeroe(Personaje):
    def __init__(self, nombre, virtud='Bondadoso'):
        super().__init__(nombre)
        self.virtud = virtud

    def registrado(self):
        print('Superheroe registrado!!')

    def salvarMundo(self):
        print('Estoy salvando al mundo')

    def pelear(self):
        print('Peleando por la justicia')

class Villano(Personaje):
    def __init__(self, nombre, defecto='Ambisioso'):
        super().__init__(nombre)
        self.defecto = defecto
    def pelear(self):
        print('Peleando por destruir el mundo')


personaje = Personaje('Personaje random')
personaje.registrado()
superheroe = SuperHeroe('Spiderman', 'Honesto')
superheroe.registrado()
superheroe.salvarMundo()
superheroe.pelear()
villano = Villano('Guason')
villano.pelear()
