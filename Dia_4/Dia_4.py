# operadores de comparacion
# == igual que
# != diferente que
# < menor que
# > mayor que
# <= menor o igual que
# >= mayor o igual que
'''
mi_bool = 10==25
print(mi_bool)
mi_bool = 'blanco' == 'negro'
print(mi_bool)
mi_bool = 'blanco' == 'Blanco'.lower()
print(mi_bool)
mi_bool = 100.0 == 100
print(mi_bool)
mi_bool = 100 != 100
print(mi_bool)
'''

# operadores logicos
# and and y -> para que de verdadero las comparaciones se deben de cumplir
# or or o -> si alguna se cumple entonces es verdadera, para que sea falso tiene que ser ambos falsos
# not no no -> saber lo contrario
'''
mi_bool = 4 < 5 and 4 < 6
print(mi_bool)
mi_bool = (55==55) and ('perro' == 'perro')
print(mi_bool)
texto = 'esta frase'
mi_bool = 'frase' in texto
print(mi_bool)
mi_bool = ('frase' in texto) and ('esta' in texto)
print(mi_bool)
mi_bool = not 'a' == 'a'
print(mi_bool)
'''

# Control de flujo
# si se cumple una condicion entonces siga el juego, esto es control de flujo
# if -> si
# elif -> otro si
# else -> sino
'''
if 10>9:
    print('es correcto')

x = True
if x:
    print('correcto')

if 5==2:
    print('correcto')
else:
    print('no correcto')

mascota = 'perro'
if mascota == 'gato':
    print('gato')
elif mascota == 'perro':
    print('perro')
else:
    print('na')
'''

# Loop for
# loop -> bucle
# for -> bucle definido
'''
lista = ['a','b','c']
for letra in lista:
    numero = lista.index(letra)+1
    print(f'Letra {numero}: {letra}')

lista = ['hans','sebastian','navarrete','lopez']
for nombre in lista:
    if nombre.startswith('l'):
        print(nombre)
    else:
        print('Nombre que no comienza con l {}'.format(nombre))

numeros = [1,2,3,4,5]
mi_valor = 0
for  numero in numeros:
    mi_valor = mi_valor+numero
print(mi_valor)

palabra = 'python'
for letra in palabra:
    print(letra)

for objeto in [[1,2],[3,4],[5,6]]:
    print(objeto)

for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

dic = {'clave1':'a','clave2':'b','clave3':'c'}
for item in dic.items():
    print(item)
for item in dic.values():
    print(item)
for item in dic:
    print(item)
'''

# loop while
# mientras que se cumpla una condicion
# break -> termina el while inmediatamente
# continue -> interrumpe la iteracion y vuelve a la parte inicial del bucle para continuar
# pass -> pasar o no hacer nada
'''
monedas = 5
while monedas > 0:
    print(f'Tengo {monedas} monedas')
    monedas -= 1
else:
    print('No tengo mas dinero')

respuesta = 's'
while respuesta == 's':
    respuesta = input('Quieres seguir? [s/n]')
else:
    print('Gracias')

respuesta = 's'
while respuesta == 's':
    pass
print('hola')

nombre = input('Tu nombre: ')
for letra in nombre:
    if letra == 'r':
        break
    print(letra)

nombre = input('Tu nombre: ')
for letra in nombre:
    if letra == 'r':
        continue
    print(letra)

numero = 50
while numero >= 0:
    if numero % 5 == 0:
        print(f'{numero}')
    else:
        pass
    numero -= 1 

lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for item in lista_numeros:
    if item < 0:
        break
    print(item)
'''

# Rango:
# funcion que permite establecer un rango de numeros empezando desde el 0 y no incluye el ultimo
# Range(1,5) -> de donde hasta donde
# Range(1,5,1) -> de donde hasta donde y cada cuanto
'''
for numero in range(0,25,5):
    print(numero)

lista = list(range(1,101))

suma_cuadrados = 0
for i in range(1,16):
    cuadrado=(i)*(i)
    suma_cuadrados=suma_cuadrados+cuadrado
print(f"La suma es:{suma_cuadrados}")
'''

# enumerador:
# acceder a los indices de una coleccion o lista
'''
lista = ['a','b','c']
indice = 0
for item in lista:
    print(indice,item)
    indice += 1

lista = ['a','b','c']
for indice,item in enumerate(lista):
    print(indice,item)

lista = ['a','b','c']
mi_tuple = list(enumerate(lista))
print(mi_tuple)

lista = list("Python")
lista_indices = list(enumerate(lista))
print(lista_indices)
'''

# zip
# sirve para integrar 2 listas en 1, ambas tienen que tener el mismo largo
'''
nombre = ['a','b','c']
edad = [1,2,3]
combinado = zip(nombre,edad)
print(combinado) # asi no se puede ver
#para poder verlo de manera correcta se hace asi:
combinado = list(zip(nombre,edad))
print(combinado)
ciudad = ['x','y','z']
combinado = list(zip(nombre,edad,ciudad))
print(combinado)

for nombre,edad,ciudad in combinado:
    print(f'{nombre} tiene {edad} años y vive en {ciudad}')

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
combinado = list(zip(capitales,paises))
for cap,pais in combinado:
    print(f'La capital de {pais} es {cap}')

uno = ['uno','dos','tres','cuatro','cinco']
dos = ['um', 'dois', 'tres', 'quatro', 'cinco']
tres = ['one','two','three','four','five']
numeros = list(zip(uno,dos,tres))
print(numeros)
'''

# min y max
# sirven para detectar los valores mas altos y mas bajos
'''
menor = min(20,70,2,1,45)
print(menor)
nayor = max(20,70,2,1,45)
print(nayor)

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
print(min((capitales)))

nombre = 'Hans'
print(min(nombre.lower()))

dic = {'c1':45, 'c2':11}
print(min(dic)) #clave
print(min(dic.values())) #valor

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades)
'''

# random
# generar numeros aleatorios
# para usar randint() se debe de importar una libreria -> from random import randint ó from random import * -> importa all de la libreria
# randint() -> metodo para escoger un numero entero aleatorio
# uniform() -> metodo para escoger un numero decimal aleatorio
# random() -> metodo para escoger un numero decimal aleatorio entre 0 y 1
# choice() -> metodo para escoger un elemento aleatorio dentro de un coleccionable
# shuffle() -> metodo para ordenar aleatoriamente los elementos de un coleccionable de numeros no de strings
'''
from random import *

aleatorio = randint(1,50)
print(aleatorio)
aleatorio = round(uniform(1,5),1) #se redondea a 1 numero decimal
print(aleatorio)
aleatorio = random()
print(aleatorio)
colores = ['a','b','c']
aleatorio = choice(colores)
print(aleatorio)
num = list(range(5,50,5))
shuffle(num)
print(num)
'''

# comprension de listas
# manera dinamica de construir listas
# para evitar esto:
'''
lista = []
palabra = 'python'
for letra in palabra:
    lista.append(letra)
'''
'''
lista = [letra for letra in 'python']
print(lista)

lista = [n for n in range(0,21,2)]
print(lista)

lista = [n/2 for n in range(0,21,2)]
print(lista)

lista = [n for n in range(0,21,2) if n*2 > 10] #si no se necesita un else, toca ponerlo al final
print(lista)

lista = [n if n*2 > 10 else 'no' for n in range(0,21,2)] #si se necesita un else, toca ponerlo al inicio
print(lista)

med = [10,20,30,40,50]
met = [n*3.281 for n in med]
print(met)

valores = [1, 2, 3, 4, 5, 6, 9.5] 
valores_pares = [n for n in valores if n%2 == 0]
print(valores_pares)

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(n-32)*(5/9) for n in temperatura_fahrenheit]
print(grados_celsius)
'''

# python 3.10
# match -> un switch case de python que solo existe desde python 3.10 en adelante
'''
serie = 'n-02'

if serie == 'n-01':
    print('a')
if serie == 'n-02':
    print('b')
if serie == 'n-03':
    print('c')
else:
    print('no')
'''
# se hace mejor asi con match:
'''
serie = 'n-02'

match serie:
    case 'n-01':
        print('a')
    case 'n-01':
        print('a')
    case 'n-01':
        print('a')
    case _:
        print('no')
'''
#####################################################Proyecto 4 ##############################################

from random import *
nombre = input('Cual es tu nombre?: ')
print(f'Hola {nombre}, bienvenido a este juego')
print('He pensado en un numero de 0 a 100 y tienes 8 intentos para adivinar cual es\n')
al = randint(1,101)
t = 1
while t < 9:
    valor = input(f'intento #{t} ingresa un numero:')
    if valor.isdigit():
        valor = int(valor)
        if valor < 0 or valor > 100:
            print('error, debes seleccionar un numero entre 0 y 100')
            pass
        elif valor < al:
            print('casi, pero el numero es mas grande!!!')
            pass
        elif valor > al:
            print('casi, pero el numero es mas pequeño!!!')
            pass
        elif valor == al:
            print(f'Eureka! lo has adivinado\nte tomaron {t} intentos')
            break
    else:
        print('Error, debes de ingresar solo numeros')
    t += 1
