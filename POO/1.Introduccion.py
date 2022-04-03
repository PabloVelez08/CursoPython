# POO
# Prototipo, plantilla

# Clase
# Atributos (Caracteristicas y métodos)
# ADT -> Abstract Data Type

class Curso:
    # Atributos
    # Metodos
    pass

class Alumno:
    pass

# Instanciar una clase -> objeto

curso1 = Curso()
curso2 = Curso()
print(type(curso1))

cursos= [curso1, curso2]
print(cursos)

texto = 'holaa'
print(texto.capitalize())

# POO en python 
print('Comprobar si curso1 es instancia de Cursos: ', isinstance(curso1, Curso))
print('Comprobar si curso1 es instancia de Alumno: ', isinstance(curso1, Alumno))