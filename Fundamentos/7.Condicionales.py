#Si, sno, entonces
#If, else y elif

variable1 = True
variable2 = False

#Operador
# 1

print(1 == 1)
print('Hola' == 'Hola')
print('hola' == 'Hola')

if variable1 and variable2 == True:
    print('La expresion es verdadera')
else:
    print('La expresion es falsa')

#Comprobaciones

texto = 'Bablo'
#Python se puede omitir la comparacion a verdadero
#if texto.startswith('A') == True:
#es igual a escribir
if texto.startswith('P'):
    print('Tu nombre empieza con P')
elif texto.startswith('B'):
    print('Tu nombre empieza con B')
else:
    print('Tu nombre no empieza con la letra P')

## Otro tipo comparaciones
print(10>=10)
print(20<30)
print(500 != 200)
print(200 != 200)
print('Anderson' != 'Fernando')

x = 10
print(0 < x < 12)
print(4 < 5 < 8 < 200)

print('A' > 'B')
print('oso' <= 'oso')