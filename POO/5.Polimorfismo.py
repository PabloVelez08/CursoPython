# Polimorfismo
# Adecuar los comportamientos en cada una de las clases

from Personaje import Personaje, nombreArchivo

class SuperHeroe(Personaje):
    def __init__(self, nombre, virtud='Buneo'):
        super().__init__(nombre)
        self.virtud = virtud
    def saludar(self):
        print('Salvando al mundo')

class Villano(Personaje):
    def __init__(self, nombre, defecto='Codicioso'):
        super().__init__(nombre)
        self.defecto = defecto
    def saludar(self):
        print('Acabando con el mundo')

print(nombreArchivo())

personaje = Personaje(nombre = 'Personaje 1')
personaje.saludar()

superHeroe = SuperHeroe(nombre='Batman')
villano = Villano(nombre='Guason')

superHeroe.saludar()
villano.saludar()