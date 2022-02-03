#Asignacion
# =

x = 5
print('El valor de la variable es: ',x)

#Asignacion sin valor
#None = no tiene ningun tipo de datos 
variable1 = None
print(type(variable1))
print('El valor de la variable 1 es: ', variable1)

#Inicializar una variable y con el valor de 100
y = 10
print(y)
#Multiplicar por dos
y = y * 2
print(y)
#Multiplicar por dos
print(y*2)
print(y)

#Asignacion con diferentes tipos
y = 'Saludo'
print(y)

#Multiples asignaciones
#Crear las variables a y b con los valores de 2 y 3
a = 2
b = 3

a, b, c, saludo = 2, 3, 5, 'Hola'
print(a+b+5)
print(saludo)

#Asignacion del valor de una vriable a otra variable
#Se copia el contenido en ese instante
saludo2 = saludo
print(saludo2)
saludo = 'Buenas tardes'
print(saludo2)

#Ejercicio
x1 = 4
y1 = x1 + 1
x1 = 2
print(x1, y1)

#Ejercicio 2
x2, y2 = 10, 11
z2 = x2
y2 = z2 + 2

print(x2,' ',y2,' ',z2)