# CALCULADORA

first = input('ingrese primer numero: ')
try:
    first = int(first)
except:
    first = 'chanchito feliz'

if first == 'chanchito feliz':
    print('el valor ingresado no es un entero')
    exit()

second = input('ingrese segundo numero: ')
try:
    second = int(second)
except:
    second = 'chanchito feliz'

if second == 'chanchito feliz':
    print('el valor ingresado no es un entero')
    exit()

print(first + second)


