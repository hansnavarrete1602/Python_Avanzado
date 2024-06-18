# Modulo collections

# Funciones mas importantes:
# counter -> contar elementos

'''from collections import Counter, defaultdict, namedtuple
from os import system

numeros = [8,6,9,5,4,5,5,2,4,2,8]
print(Counter(numeros))
print(Counter('HaHaHa'))
frase = 'al pan pan y al vino vino'
print(Counter(frase.split()))
serie = Counter(numeros)
print(serie.most_common())
print(serie.most_common(1))
print(serie.most_common(2))
print(list(serie))'''

# defaultdict

#system('cls')

"""mi_dic = {'uno':'verde','dos':'azul','tres':'rojo'}
print(mi_dic['dos'])"""

'''mi_dic = defaultdict(lambda: 'nada') # en caso de que el key no esta dentro del diccionario, se le asigna "nada"
mi_dic['uno'] = 'verde'
print(mi_dic['dos'])
print(mi_dic)'''


# namedtuple

#system('cls')

"""mi_tupla = (500,18,65)
print(mi_tupla[1])"""

'''Persona = namedtuple('Persona', ['nombre', 'altura', 'peso'])
ariel = Persona('Ariel', 1.76, 79)
print(ariel.nombre)
print(ariel.peso)'''

'''from collections import Counter
lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]
contador = Counter(lista)'''

'''from collections import defaultdict
mi_diccionario = defaultdict(lambda: 'Valor no hallado')
mi_diccionario['edad'] = 44'''

#from collections import deque

'''ciudades = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
lista_ciudades = deque(ciudades)'''

'''# complemento:
ciudades = ["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]
lista_ciudades = deque(ciudades)
listaCasteadaCiudades = list(lista_ciudades)
print(listaCasteadaCiudades)

# insertar por la derecha
lista_ciudades.append("Bogota")
dequeCasteadoDerecha = list(lista_ciudades)
print(dequeCasteadoDerecha)

# insertar por la izquierda
lista_ciudades.appendleft("Tokyo")
dequeCasteadoIzquierda = list(lista_ciudades)
print(dequeCasteadoIzquierda)'''


# OS
# shuttil

'''import os

print(os.getcwd())
archivo = open('curso.txt', 'w')
archivo.write('texto de prueba')
archivo.close()
print(os.listdir(os.getcwd()))'''

# import shutil
# shutil.move('curso.txt', 'destino')
# os.unlink() -> eliminar archivo
# os.rmdir() -> eliminar directorio
# shutil.rmt() -> eliminar all
# pip install send2trash -> para enviar a la papelera
'''import send2trash
send2trash.send2trash('path')'''
# walk -> camina por el directorio almacena la ruta, subcarpetas y archivos
# print(os.walk('path'))
'''
import os
for carpeta, subcarpeta , archivo in os.walk(os.getcwd()):
    print(f'En la carpeta: {carpeta}')
    print('Las subcarpetas son: ')
    for sub in subcarpeta:
        print(f'\t{sub}')
    print('Los archivos son:')
    for arch in archivo:
        """if arch.startswith('2015'):
            print(f'\t{arch}')"""
        print(f'\t{arch}')
    print('\n')
'''

# datetime
# almacenar hora y fecha en variables
# calculos de tiempo
# mostrar en diferentes formatos

'''import datetime

mi_hora = datetime.time(17, 35)
print(type(mi_hora))
print(mi_hora)
print(mi_hora.minute)

mi_fecha = datetime.date(2025,10,17)
print(mi_fecha)
print(mi_fecha.year)
print(mi_fecha.ctime())

print(datetime.date.today())'''

# para mezclar fecha y hora:

'''from datetime import datetime

mi_fecha = datetime(2025, 5 ,15, 22 ,10, 5)
print(mi_fecha)
mi_fecha = mi_fecha.replace(month=2)
print(mi_fecha)'''

# para comparar fechas

'''from datetime import date

nacimiento = date(1997,2,16)
defuncion = date(2023,9,1)
dif = defuncion - nacimiento
print(dif)'''

# para comparar horas

'''from datetime import datetime

despierta = datetime(2023,9,1,8,30)
dormida = datetime(2023,9,2,3,30)
dif = dormida - despierta
print(dif)'''

'''from datetime import date
hoy = date.today()'''

'''from datetime import datetime
minutos = datetime.now().minute'''

# modulos para medir el tiempo
# time

# import time


'''def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista


def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista'''


#print(prueba_for(15))
#print(prueba_while(15))

# time no tiene mucha precision

'''inicio = time.time()
prueba_for(15000000)
final = time.time()
print(final - inicio)
inicio = time.time()
prueba_while(15000000)
final = time.time()
print(final - inicio)'''

# timeit

"""import timeit

declaracion = '''
prueba_for(10)
'''
declaracion2 = '''
prueba_while(10)
'''
setup_ = '''
def prueba_for(numero):
    lista = []
    for num in range(1, numero + 1):
        lista.append(num)
    return lista
'''
setup2_ = '''
def prueba_while(numero):
    lista = []
    contador = 1
    while contador <= numero:
        lista.append(contador)
        contador += 1
    return lista
'''
duracion = timeit.timeit(declaracion,setup_,number=1000000) # numbers = cuantas veces
print(duracion)
duracion2 = timeit.timeit(declaracion2,setup2_,number=1000000) # numbers = cuantas veces
print(duracion2)"""

# Modulo math
# kit completo para trabajar con matematicas

'''import math

resultado = math.floor(1.82) # redondear a piso
print(resultado)
resultado = math.ceil(1.82) # redondear a techo
print(resultado)
resultado = math.pi # pi
print(resultado)
resultado = math.log(25, 5)
print(resultado)
resultado = math.tan(15)
print(resultado)'''
# resultado = math.log10(25)
# resultado = math.sqrt(math.pi)
'''from math import factorial
resultado = factorial(7)'''

# modulo re
# expresiones regulares -> permiten hacer busquedas especificas
# se contruye un patron para corroborar si existe en algun lugar

# ### - ### - ####
# patron = r'\d\d\d-\d\d\d-\d\d\d\d' -> caracteres especiales
# patron = r'\d{3}-\d{3}-\d{4} -> cuantificadores
'''
caracter        descripcion           ejemplo
   /d         digito numerico         \d\d\d
   /w      caracter alfanumerico     \w\w\w-\w
   /s        espacio en blanco      numero\s\d\d
   /D           No numerico          \D\D\D\D
   /W         No alfanumerico         \W\W\W
   /S       No espacio en blanco      \S\S\S
'''
'''
caracter        descripcion           ejemplo
   +           1 o mas veces           \d\d+
  {n}        se repite n veces         \d{4}
 {n,m}    se repite de n a m veces     \w{3,5}
  {n,}     desde n hacia arriba        \d{4,}
   *           0 o mas veces          \w\s*\w
   ?             1 o 0 veces          casas?
'''

'''import re

texto = 'Si necesitas ayuda llama al (658)-598-9977 las 24 horas al servicio de ayuda online'
"""palabra = 'ayuda' in texto
print(palabra)"""

patron = 'ayuda'
busqueda = re.search(patron, texto)
print(busqueda)
print(busqueda.span())
print(busqueda.start())
print(busqueda.end())

busqueda = re.findall(patron, texto)
print(busqueda)
print(len(busqueda))

for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())'''

'''import re

texto = "llama al 564-525-6588 ya mismo"
patron = r'\d{3}-\d{3}-\d{4}'
resultado = re.search(patron, texto)
print(resultado)
print(resultado.group())
patron = re.compile(r'(\d{3})-(\d{3})-(\d{4})')
resultado = re.search(patron, texto)
print(resultado.group(1))'''

'''import re

clave = input('clave: ')
patron = r'\D{1}\w{7}'
chequear = re.search(patron, clave)
print(chequear)'''

'''import re

texto = 'no se atiende el lunes por la tarde'
buscar = re.search(r'lunes|martes', texto)
print(buscar)
buscar = re.search(r'demos', texto)
print(buscar)
buscar = re.search(r'.demos', texto)
print(buscar)
buscar = re.search(r'....demos', texto)
print(buscar)
buscar = re.search(r'....demos....', texto)
print(buscar)
buscar = re.search(r'^\D', texto) # ^ -> al comienzo del string
print(buscar)
buscar = re.search(r'\D$', texto) # ^ -> al final del string
print(buscar)
buscar = re.findall(r'[^\s]+', texto) # [] -> excluya espacios
print(buscar)
print(''.join(buscar))'''

'''import re

def verificar_email(email):
    patron = r'\w*@\w*\.com'
    buscar = re.search(patron, email)
    if buscar:
        print('Ok')
    else:
        print("La dirección de email es incorrecta")'''

'''import re

def verificar_saludo(frase):
    patron = r'Hola\w*'
    busqueda = re.search(patron, frase)
    if busqueda:
        print('Ok')
    else:
        print('No has saludado')'''

'''import re

def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    buscar = re.search(patron, cp)
    if buscar:
        print('Ok')
    else:
        print("El código postal ingresado no es correcto")'''


# comprimir y descomprimir archivos en python
# zipfile
# shutil

# import zipfile
# para comprimir
'''mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')
mi_zip.write('prueba.txt')
mi_zip.write('prueba1.txt')
mi_zip.close()'''
# para descomprimir
'''zip_abierto = zipfile.ZipFile('archivo_comprimido.zip', 'r')
zip_abierto.extractall()'''

#import shutil
#import os
# comprimir
'''carpeta_origen = os.getcwd()
archivo_destino = 'todo_comprimido'
shutil.make_archive(archivo_destino, 'zip', carpeta_origen)'''

# descomprimir
# shutil.unpack_archive('todo_comprimido.zip', 'extraccion', 'zip')


#####################################################Proyecto 9 ##############################################

import re
import os
import time
import datetime
from pathlib import Path
import math

inicio = time.time()

ruta = 'C:\\Users\\hansn\\PycharmProjects\\Curso_Python_Avanzado\\Dia_9\\Mi_Gran_Directorio'
mi_patron = r'N\D{3}-\d{5}'
hoy = datetime.date.today()
num_encontrados = []
archivos_encontrados = []


def buscar_numero(archivo, patron):
    este_archivo = open(archivo, 'r')
    texto = este_archivo.read()
    if re.search(patron, texto):
        return re.search(patron, texto)
    else:
        return ''


def crear_listas():
    for carpetas, subcarpetas, archivos in os.walk(ruta):
        for a in archivos:
            resultado = buscar_numero(Path(carpetas, a), mi_patron)
            if resultado != '':
                num_encontrados.append(resultado.group())
                archivos_encontrados.append(a.title())


def mostrar_todo():
    indice = 0
    print('-'*50)
    print(f'fecha de busqueda: {hoy.day}/{hoy.month}/{hoy.year}')
    print('\n')
    print('Archivo\t\t\tNo. Serie')
    print('------------\t\t\t---------')
    for a in archivos_encontrados:
        print(f'{a}\t{num_encontrados[indice]}')
        indice += 1
    print('\n')
    print(f'Numeros escontrados: {len(num_encontrados)}')
    fin = time.time()
    duracion = fin - inicio
    print(f'Duracion de la busqueda: {math.ceil(duracion)} segundos')
    print('-' * 50)


crear_listas()
mostrar_todo()

















