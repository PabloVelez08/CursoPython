# Funciones -> def
# A (regla de correspondencia) -> B
# a -> f -> b

# Proedimiento (funcion vacia)
def saludar():
    print('Hola!!!')

saludar()

edades = [18,5,20,22,17,14,5,2]

# Funciones
    # 1. Recibir parametros 
def esMayorEdad(edad: int):
    if edad >= 18:
        return True
    return False

for edad in edades:
    print(esMayorEdad(edad))

    # 2. Recibir varios parametros
def saludar2(nombre: str, apellido):
     return f'Saludos {nombre} {apellido}'

print(saludar2('Pablo', 'Velez'))

    # 3. Parametros por defecto
def saludar3(nombre= 'Hector', apellido='Zambrano'):
    return f'Saludos {nombre} {apellido}'

print(saludar3())
print(saludar3('Alexander'))
print(saludar3(apellido = 'Real'))
print(saludar3('Alexander', 'Velez'))

    # 4. Llamar a una funcion dentro de otra
def saludar4():
    print('Hola a todos!!!')
    print(saludar3())

saludar4()

# Documentacion 

def calcularCubo(numero: int):
    '''
    Permite calcular el cubo de un numero
    numero: Número entero
    return: El cubo de la entrada
    '''
    return numero**3

print(calcularCubo(3))
print(calcularCubo.__doc__)

# Funciones args
# *args
# Numero indefinido de valors
def listarAlumnos(*alumnos):
    print(f'Alumno: {alumnos}')

listarAlumnos('Pablo')
listarAlumnos('Pablo', 'Pedro', 'Alex', 'Kevin')

def listarAlumnos2(*alumnos):
    for alumno in alumnos:
        print(f'Alumno: {alumno}')

listarAlumnos2('Pablo')
listarAlumnos2('Pablo', 'Pedro', 'Alex', 'Kevin')

# **kargs
# key word args
# Numero indefinido de parametros
def listarAlumnos3(**alumnos):
    print('La edad es: ', alumnos['edad'])

listarAlumnos3(nombre = 'Pablo', apellido = 'Velez', edad = 22)
