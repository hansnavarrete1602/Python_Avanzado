'''
dic = {'clave':100,'clave2':200}
a = dic.popitem()
print(a)
print(dic)
'''
'''
print(",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#".lstrip(',:%_#'))

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
frutas.insert(3,'naranja')
print(frutas)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
conjuntos_aislados = marcas_smartphones.isdisjoint(marcas_tv) #false si tienen algo en comun, true si no tienen nada
print(conjuntos_aislados)
'''

# funciones
'''
def saludar(nombre):
    print('Hola {}'.format(nombre))
saludar('Hans')

def sumar(n1,n2):
    return n1+n2
res = sumar(5,10)
print(res)

def invertir_palabra(a):
    return a[::-1].upper()
palabra = 'hola'
'''

# funciones dinamicas
'''
def check(num):
    return num in range(100,1000)
result = check(523)
print(result)

def check2(lst):
    l = []
    for n in lst:
        if n in range(100,1000):
            l.append(n)
        else:
            pass
    return l
lst = [1,4353,3432,30,14,22,3]
result = check2(lst)
print(len(result))

def todos_positivos(a):
    l = []
    for n in a:
        if n > 0:
            l.append(n)
        else:
            return False
    return True
lista_numeros = [2,-1,3,5]

def suma_menores(a):
    suma = 0
    for n in a:
        if n>0 and n<1001:
            suma = suma+n
    return suma
lista_numeros = [2,5,4,-2,6]

def cantidad_pares(a):
    count = 0
    for n in a:
        if n % 2 == 0:
            count += 1
    return count
lista_numeros = [2,3,4,5,7]
'''

# ejemplo avanzado
'''
precios = [('cafe',1.5),('jugo',1.2),('gaseosa',2.3)]
for cafe,precio in precios:
    print(cafe,precio)

def cafe_(a):
    precio = 0
    ca = ''
    for c,p in a:
        if p>precio:
            precio = p
            ca = c
        else:
            pass
    return (ca,precio)
print(cafe_(precios))
c,p = cafe_(precios)
'''

# interaccion entre funciones
'''
from random import *

# lista inicial
palitos = ['-','--','---','----']

# mezclar palitos
def mezclar(a):
    shuffle(a)
    return a

# pedir intento
def probar():
    intento = ''
    while intento not in ['1','2','3','4']:
        intento = input('Dime un numero de 1 a 4: ')
    return int(intento)

# comprobar intento
def check(a,i):
    if a[i-1] == '-':
        print('perdiste')
    else:
        print('Te salvaste!')
    print(f'escogiste: {a[i-1]}')

palitos_ = mezclar(palitos)
inte = probar()
check(palitos_,inte)
'''

'''
from random import *

def evaluar_jugada(a, b):
    res = a+b
    if res <= 6:
        return 'La suma de tus dados es {}. Lamentable'.format(res)
    elif res > 6 and res < 10:
        return 'La suma de tus dados es {}. Tienes buenas chances'.format(res)
    elif res >= 10:
        return 'La suma de tus dados es {}. Parece una jugada ganadora'.format(res)

def lanzar_dados():
    return randint(1,6), randint(1,6)

a,b = lanzar_dados()
evaluar_jugada(a,b)
'''

'''
from random import *

def lanzar_moneda():
    lst = ['Cara', 'Cruz']
    return choice(lst)

def probar_suerte(a,b):
    if a == 'Cara':
        print('La lista se autodestruirá')
        b = []
        return b
    elif a == 'Cruz':
        print('La lista fue salvada')
        return b

lista_numeros = [1,2,3,4,5]
a = lanzar_moneda()
c = probar_suerte(a, lista_numeros)
print(c)
'''

# Argumentos indefinidos (*args)
# Si se necesita una funcion que va a recibir tantos parametros que no se sabe cuales o cuantos son
# se utiliza estos dos:
# *args = arguments ->

'''
def suma(a, b):
    return a + b
print(suma(1,2))
def suma_args(*args):
    total = 0
    for arg in args:
        total += arg
    return total
print(suma_args(10,20,30,40,50))
def suma_args_pro(*args):
    return sum(args)
print(suma_args_pro(10,20,30,40,50))
'''

'''
def suma_cuadrados(*args):
    return sum(arg**2 for arg in args)
'''

'''
def suma_absolutos(*args):
    return sum(abs(arg) for arg in args)
'''

'''
def numeros_persona(name, *args):
    return '{}, la suma de tus números es {}'.format(name, sum(args))
'''

# **kwargs
# funciona como args pero como diccionario

'''
def suma(**kwargs):
    print(type(kwargs))
suma(x=3,y=5,z=2)
'''

'''
def recorrer(**kwargs):
    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')
recorrer(x=3,y=5,z=2)
'''

'''
def recorrer_pro(**kwargs):
    total = 0
    for clave,valor in kwargs.items():
        print(f'{clave} = {valor}')
        total += valor
    return total
print(recorrer_pro(x=3,y=5,z=2))
'''

'''
def prueba(num1, num2, *args, **kwargs):
    print(f'El primer valor es {num1}')
    print(f'El segundo valor es {num2}')
    for arg in args:
        print(f'arg = {arg}')
    for clave, valor in kwargs.items():
        print(f'{clave} = {valor}')
prueba(15,50,1,2,3,4,5,6,x='uno',y='dos',z='tres')
args = [1,2,3,4,5,6]
kwargs = {'x':'uno', 'y':'dos', 'z':'tres'}
prueba(10,50, *args, **kwargs)
'''

'''
def cantidad_atributos(**kwargs):
    return len(kwargs)
'''

'''
def lista_atributos(**kwargs):
    return [valor for clave,valor in kwargs.items()]
'''

'''
def describir_persona(name, **kwargs):
    print(f'Características de {name}:')
    for clave,valor in kwargs.items():
        print(f'{clave}: {valor}')
'''


# Ejercicios practicos

'''
def devolver_distintos(a,b,c):
    suma = a+b+c
    lista = [a,b,c]
    if suma > 15:
        return max(lista)
    elif suma < 10:
        return min(lista)
    else:
        lista.sort()
        return lista[1]
devolver_distintos(3,7,2)  
'''

'''
def unique(palabra):
    mi_set = set()
    for letra in palabra:
        mi_set.add(letra)
    mi_lista = list(mi_set)
    mi_lista.sort()
    return mi_lista
print(unique('entretenido'))
'''

'''
def ceros_vecinos(*args):
    contador = 0
    for num in args:
        if contador + 1 == len(args):
            return False
        if args[contador] == 0 and args[contador + 1] == 0:
            return True
        else:
            contador += 1
    return False
print(ceros_vecinos(1,2,5,4,0,0,2,3,5))
'''

'''
def contar_primos(numero):
    primos = [2]
    iteracion = 3
    if numero < 2:
        return 0
    while iteracion <= numero:
        for n in range(3, iteracion, 2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2
    print(primos)
    return len(primos)
print(contar_primos(50))
'''

#####################################################Proyecto 5 ##############################################

from random import *

dic = {'astronomia' : ['planetas', 'estrellas', 'constelacion', 'universo', 'foton'],
        'quimica' : ['atomo', 'molecula', 'celula', 'mitocondria', 'adn'],
       'fisica' : ['energia', 'trabajo', 'esfuerzo', 'velocidad', 'aceleracion'],
       'vengadores' : ['ultron', 'wakanda', 'blackpanter', 'multiverso', 'gemas'],
       'star wars' : ['sith', 'jedi', 'fuerza', 'droide', 'clon']}


def palabra_azar(a):
    return choice(a)


def palabra_encrypt(a):
    sw = ''
    for i in range(len(a)):
        sw += '-'
    return sw


def check_position(a, b):
    return [i for i, ltr in enumerate(a) if ltr == b]


def encrypt_position(a, b, c):
    if len(a) != 0:
        s = list(b)
        for i in range(len(a)):
            s[a[i]] = c
        return "".join(s)
    else:
        return False


def juego():
    while True:
        try:
            intentos = 0
            new_ = ''
            print('\nA continuacion debe de escoger un tema de su interes\nescribiendo el numero que le corresponde')
            for i in range(len(dic.keys())):
                print(f'{i+1}. {list(dic.keys())[i]}')
            c = input('Porfavor seleccione: ')
            print(f'\nEscogiste {list(dic.keys())[int(c)-1]}\nen este tema encontraras estas palabras:')
            for i in range(len(list(dic[list(dic.keys())[int(c)-1]]))):
                print(f'{i+1}. {list(dic[list(dic.keys())[int(c)-1]])[i]}')
            ch = input('¿Deseas empezar el juego? [S/N]: ')
            if ch.lower() == 's' or ch.lower() == 'y':
                azar = palabra_azar(list(dic[list(dic.keys())[int(c)-1]]))
                encrypt = palabra_encrypt(azar)
                print('\nBienvenido al juego del ahorcado :)\nTienes que adivinar la palabra secreta\nSolo tienes 6 intentos para fallar')
                while intentos < 6:
                    print('\nTienes {} vidas'.format(6-intentos))
                    a = input('Ingresa una letra: ')
                    if not a.isdigit():
                        ck = check_position(azar, a.lower())
                        if ck:
                            if a not in new_:
                                new_ = encrypt_position(ck, encrypt, a)
                                encrypt = new_
                                print(f'\n{new_}')
                                if new_ == azar:
                                    print('\n¡Ganaste con {} vidas restantes!'.format(6-intentos))
                                    break
                                continue
                            else:
                                print('\n...Ya has acertado la letra {}'.format(a))
                        else:
                            intentos += 1
                            print('...\nLo siento, la letra "{}" no esta en la palabra secreta'.format(a))
                    else:
                        print('...\nLo siento, solo se aceptan letras')
                if intentos == 6:
                    print('\n...Perdiste\nLa palabra era: {}'.format(azar))
            else:
                continue
        except KeyboardInterrupt():
            break


juego()


'''
palabras = ['hola', 'cosmos', 'azar', 'escoger', 'sentir']
azar = palabra_azar(palabras)
encrypt = palabra_encrypt(azar)
print(azar)
ck = check_position(azar, 'e')
print(ck)
new_ = encrypt_position(ck, encrypt, 'e')
print(new_)
'''