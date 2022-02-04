import math as math
#Programa que permite resolver ecuacion de segundo grado
#ax^{2}+bx+c=0 // a, b, c son numeros reales
#Pedir al usuario que ingrese los valos de a, b, c
a = int(input('Ingrese el valor de a: '))
b = int(input('Ingrese el valor de b: '))
c = int(input('Ingrese el valor de c: '))

#Imprimir en consola la ecuacion de segundo grado
print('La ecuacion ',a,'x^2 ',b,'x ',c,' = 0, tiene las soluciones:')

#Mostrar las dos soluciones x1, x2
x1 = ((-1*b) + math.sqrt((b**2) - (4*a*c))) / (2*a)
x2 = ((-1*b) - math.sqrt((b**2) - (4*a*c))) / (2*a)

print('x1: ', x1, '\tx2: ',x2)