#Enteros -> int
#Conversiones de datos 

#Importacion
import math as math

'''
num1 = input('Ingrese un número')
print(type(num1))
num1 = int(num1) #Conversio de string a entero
print(num1+20)

#En una sola linea de codigo, tomo la entrad de input y la convierto a entero
num2 = int(input('Ingrese otro numero: '))
print(num2+2)

#
num3 = int(True)
#True -> 1
#False -> 0
print(num3)
'''
#Operadores numericos
a,b = 2,3
print('\n\tOperaciones con numeros\n')
#Suma
print('Suma: ', a+b)
#Resta
print('Resta: ', a-b)
#Multiplicacion
print('Mulriplicacion: ', a*b)
#Divisionde dos numeros siempre sera un numero flotante
print('Division: ', a/b)

#Potencia
print('Potencia: ', 2**3)

#Modulo
print('Modulo: ', a%b)

#Division entera
print('Division entera: ', 10//3)

#Raiz
print('Raiz: ',25**(1/2))
print('Raiz con libreria: ', math.sqrt(64))

#-------------------
#Floats -> float
#-------------------
numeroFlotante = float(input('Ingrese un numero decimal:'))
print(numeroFlotante)

#Operadores son los mismos que los enteros