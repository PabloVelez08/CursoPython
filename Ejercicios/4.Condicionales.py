# Capicuas
# Palindromos

#Solicitar al usuario que ingrese por teclado un texto, le vamos a indicar si lo ingresado es o no un palindromo

texto = input('Ingrese una cadena de texto:')
print('Palabra de izquierda a derecha: ' + texto)
print('Palabra de derecha a izquierda: ' + texto[::-1])

if texto == texto[::-1]:
    print('Ingresaste un palindromo')
elif texto.lower() == texto[::-1].lower():
    print('Palindromo, ignorando las mayúsculas')
elif texto.replace(' ','') == texto[::-1].replace(' ',''):
    print('Palindromo, ignorando los espacios')
else:
    print('No ingresaste un palindromo')