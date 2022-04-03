# Clases con metodos y atributos

# Metodo init (constructor)
# Siempre se va a ejecutary es lo primero en ejecutarse

class Personaje:
    # Atributos
    def __init__(self, nombre, tipo, edad):
        self.nombrePersonaje = nombre
        self.tipo = tipo
        self.edad = edad
    # Metodos especaiales get y set
    def getNombrePersonaje(self):
        return self.nombrePersonaje
    def setNombrePersonaje(self, nuevoNombre: str):
        self.nombrePersonaje = nuevoNombre
    # Metodos
    def saludar(self):
        print(f'Hola, soy un personaje\nMi nombre es {self.nombrePersonaje} y soy un {self.tipo}')

    

personaje1 = Personaje('Batman', 'Heroe',35)
personaje2 = Personaje('Spiderman', 'Heroe', 23)
personaje1.saludar()
personaje2.saludar()

print('Nombre antes del set: ',personaje2.getNombrePersonaje())
personaje2.setNombrePersonaje('Venom')
print('Nombre despues del set: ',personaje2.getNombrePersonaje())

