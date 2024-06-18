# Strings: metodo index()
# un string es una secuencia de caracteres, cada uno de ellos tiene una posicion asignada
# HOLA -> H O L A -> H(0) O(1) L(2) A(3) -> index
# HOLA -> H O L A -> H(0) O(-3) L(-2) A(-1) -> index inverso
# El metodo index puede buscar incluso una palabra pero da la posicion nicial de ella
# El metodo index es sensible a mayusculas y minusculas, es decir no reconoce si es lo mismo
# Si existe mas de un caracter igual en la palabra u oracion, index solo dara la posicion del primero que encuentre
# index(string o caracter, desde donde, hasta donde) -> busca de izquierda a derecha
# rindex(string o caracter, desde donde, hasta donde) -> busca de derecha a izquierda

'''
mi_texto = 'hola'
mi_texto.index('o') -> Conocer el inidice de un caracter
mi_texto[3] -> Conocer que caracter hay en un indice determinado
'''

'''
mi_texto = 'Esta es una prueba'
resultado = mi_texto[0]
print(resultado)
try:
    resultado = mi_texto.index('una')
    print(resultado)
except ValueError:
    print('no existe el caracter')
resultado = mi_texto.rindex('a')
print(resultado)
'''

# Extraer Sub-Strings: Slicing
# se extrae una fraccion de cadenas de caracteres y se puede alamacenar en una nueva variable
# mi_variable = 'esta palabra'
# mi_variable[5:12:2] -> 5(inicio), 12(fin), 2(cada cuanto)
# mi_variable[2:] -> desde el 2 hasta el final
# mi_variable[:5] -> desde el incio hasta el 5
# mi_variable[::3] -> desde el inicio hasta el final cada 3
# mi_variable[::-1] -> se obtiene la cadena completa pero invertida (dato curioso)

'''
texto = 'ABCDEFGHIJKLM'
fragmento = texto[2]
print(fragmento)
fragmento = texto[2:5]
print(fragmento)
fragmento = texto[2:10:2]
print(fragmento)
fragmento = texto[::-1]
print(fragmento)
'''

# Metodos mas comunes:
# upper() -> pasar a mayusculas
# lower() -> pasar a minusculas
# split() -> separar en partes (se puede crear una lista de palabras o caracteres)
# join() -> une una lista de caracteres en un solo string
# find() -> encontrar un sub-string -> si find no encuentra lo buscado entonces devuelve un -1
# replace() -> reemplazar un substring

'''
texto = 'Este es el texto de Hans'
a = 'a'
b = 'b'
c = 'c'
resultado = texto
print(resultado)
resultado = texto.upper()
print(resultado)
resultado = texto[2].upper()
print(resultado)
resultado = texto.lower()
print(resultado)
resultado = texto.split()
print(resultado)
resultado = texto.split('t')
print(resultado)
d = ' '.join([a,b,c])
print(d)
resultado = texto.find('H')
print(resultado)
resultado = texto.replace('texto','codigo')
print(resultado)
'''

# Propiedades de los strings
# un string es inmutable -> que no se puede cambiar
# se concatena con el signo + o * para multiplicar un string
# se puede calcular el tamaño con la funcion len()

"""
nombre = 'Hanz'
#nombre[3] = 's' -> error porque no se puede cambiar el string asi
nombre = 'Hans' # -> asi se cambia
print(nombre)
n1 = 'ha'
n2 = 'ns'
nombre = n1+n2
print(nombre)
poema = '''a 
bdb
c'''
print(poema)
print('a' in poema) # -> saber si se encuentra algo dentro del string, devuelve true o false
print('a' not in poema)
print(len(poema))
"""

# Listas
# una lista es una secuencia ordenada de elementos, que pueden ser diferentes tipos de datos, estan en corchetes y se separan por comas
# se pueden recorrer, fraccionar y reorganizar su contenido
# tambien se puede reemplazar el contenido desde su indice
# la propiedad append() sirve para agregar otro elemento al final de la lista
# La propiedad pop() sirve para eliminar un elemento de la lista, por default y sin parametros elimina el ultimo elemento
# pop(0) -> elimina el primer elemnto de la lista, solo se introduce el indice del elemento
# sort() -> sirve para ordenar los elementos de una lista de menor a mayor
# reverse() -> sirve para ordenar del ultimo al primero los elementos de una lista

'''
mi_lista = ['a','b','c']
otra_lista = ['a', 55, 34.5, 'hola']
print(type(mi_lista))
print(len(mi_lista))
resultado = mi_lista[1]
print(resultado)
resultado = mi_lista+otra_lista
print(resultado)
resultado[0] = 'alpha'
print(resultado)
resultado.append('beta')
print(resultado)
resultado.pop()
print(resultado)
resultado.pop(0)
print(resultado)
eliminado = resultado.pop(0)
print(eliminado)
lst = ['f','d','c']
lst.sort()
print(lst)
lst.reverse()
print(lst)
'''

# Diccionarios
# pares compuestos por clave y valor asociado a la clave, no se pueden repetir las claves
# a diferencia de las listas, no tienen un indice ni orden especifico
# se buscan los valores basandose en las claves

'''
diccionario = {'c1':'valor1','c2':'valor2'}
print(type(diccionario))
print(diccionario)
resultado = diccionario['c1']
print(resultado)
cliente = {'nombre':'Hans','apellido':'Navarrete','peso':68, 'talla':1.70}
consulta = cliente['apellido']
print(consulta)
dic = {'c1':55, 'c2':[10,20,30], 'c3': {'cx':'x','cy':'y'}}
print(dic)
print(dic['c2'])
print(dic['c2'][2])
print(dic['c3'])
print(dic['c3']['cx'])
dx = {'c1':['a','b','c'],'c2':['d','e','f']}
print(dx['c2'][1].upper())
dy = {'c1':'a','c2':'b'}
print(dy)
dy['c3'] = 'c'
print(dy)
dy['c2'] = 'B'
print(dy)
print(dy.keys())
print(dy.values())
print(dy.items())
'''

# tuples
# son una coleccion de elementos, se diferencia a las listas en que son inmutables, no se pueden cambiar
# los tuples ocupan menos espacio de memoria y son mas veloces que las listas
# al no poderse modificar crea un poco de seguridad y es a prueba de daños

'''
mi_tuple = (1,2,3,4)
print(type(mi_tuple))
print(mi_tuple)
mi_tuple = (4,23.3,'a')
print(mi_tuple[1])
print(mi_tuple[-2])
mi_tuple = (1,2,(10,20),5)
print(mi_tuple[2])
mi_tuple = list(mi_tuple)
print(type(mi_tuple))
print(mi_tuple)
mi_tuple = tuple(mi_tuple)
print(type(mi_tuple))
print(mi_tuple)
t = 1,2,3
x,y,z = t
print(x,y,z)
t = 1,2,3,1
print(len(t))
print(t.count(1)) #->cantidad de apariciones de 1 en el tuple
print(t.index(2)) #->indica el indice de donde se encuentra 2
'''

# sets
# son una coleccion de elementos
# set([1,2,3])
# {1,2,3}
# solo admite elementos unicos
# no estan ordenados en inidices
# son inmutables
# solo admite un argumento, es decir los elementos deben estar encerrados en {} o []
# no se puede poner listas o diccionarios dentro de un set pero si admite tuples

'''
mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)
otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)
print(len(mi_set))
print(2 in mi_set)
s3 = mi_set.union(otro_set)
print(s3)
s3.add(6)
print(s3)
s3.remove(6)
print(s3)
s3.discard(7) #->descartar un elemento y si no existe no pasa nada
print(s3)
s3.pop() #->elimina aleatoriamente
print(s3)
s3.clear() #vacia el set
print(s3)
'''

# booleanos
# solo son True o False

'''
var1 = True
var2 = False
print(type(var1))
print(var1)
numero = 5 == 2+3
print(numero)
numero = bool(5>6)
print(numero)
numero = bool() #->valor False por default
print(numero)
lista = [1,2,3,4]
control = 5 in lista
print(control)
'''
#####################################################Proyecto 3 ##############################################

txt = input('...Buen dia \n...Por Favor ingrese el texto que desea analizar: ')
txt = txt.lower()
if len(txt) != 0 or None:
    print(f'\nEl texto ingresado es: {txt}\n')
    ########################################## 1 ###############################################
    print('...A continuación debe de ingresar 3 letras cualquiera a su elección')
    lst = []
    for i in range(3):
        x = input('Digite la letra #{}: '.format(i+1))
        x = x.lower()
        lst.append(x)
        del(x)
    print(f'\nEsta es la lista de las letras ingresadas: {lst}\n')
    print('...A continuación se mostrara el analisis del texto...\n')
    lst_result = []
    for i in range(3):
        lst_result.append(txt.count(lst[i]))
    for i in range(3):
        print('La letra {} se encuentra en el texto insertado {} veces'.format(lst[i],lst_result[i]))
    ########################################## 2 ###############################################
    lst_2 = txt.split(' ')
    print(f'\nLa cantidad total de palabras que hay en el texto son: {len(lst_2)}\n')
    ########################################## 3 ###############################################
    print('La primera letra del Texto es: {}'.format(txt[0]))
    print('La ultima letra del Texto es: {}\n'.format(txt[-1]))
    ########################################## 4 ###############################################
    print(f'El texto invertido quedaria asi: {txt[::-1]}\n')
    lst_2.reverse()
    print(f'El texto con las palabras invertidas quedaria asi: {" ".join(lst_2)}\n')
    ########################################## 5 ###############################################
    result = txt.find('python')
    if result == -1:
        print('La palabra Python no estaba en el texto ingresado')
    else:
        print('La palabra Python si se encuentra en el texto ingresado y esta en la posicion {}'.format(result))
else:
    print('...Debe de ingresar un texto de almenos 1 letra para poder realizar el analisis\nVuelve a ejecutar el algoritmo...')
