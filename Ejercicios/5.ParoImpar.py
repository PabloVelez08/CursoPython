#Usuario ingrese un numero y le diremos si es par o impar

numero = int(input('Ingrese un número: '))

if numero%2 == 0:
    print('Es un numero par')
else:
    print('Es un numero impar')

if numero > 0:
    print('Es un numero mayor a cero')
else:
    print('Es un numero menor a cero')