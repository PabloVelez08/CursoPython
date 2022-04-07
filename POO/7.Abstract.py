from abc import ABC, abstractmethod

# Interfaces -> solo tienen metodos, ya no especifique la implementacion de los metodos
# Metodos que aun no son implementados son conocidos como abstractos
# Para poder tener una interfaz necesariamente se necesita al menos un metodo abstracto

class Animal(ABC):
    @abstractmethod
    def darInformacion(self):
        pass

# Herencia -> Metodos
class Mamifero(Animal):
    def saludar(self):
        print('Hola')
    def darInformacion(self):
        print('Me alimento de leche')

class Reptil(Animal):
    def darInformacion(self):
        print('Soy de sangre fria')

mamifero = Mamifero()
mamifero.darInformacion()

reptil = Reptil()
reptil.darInformacion()