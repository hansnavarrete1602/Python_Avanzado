# modulos y paquetes de python
# Pypi -> repositorio de modulos y paquetes
# Modulo -> cualquier codigo python guardado en un archivo .py
# Paquetes -> colecciones de modulos (carpeta con varios modulos) siempre deben de llevar dentro de la carpeta un modulo especial llamado __init__.py ademas de los otros modulos

# Manejo de errores
# intentar -> try -> intenta esto...
# excepcion -> except -> si sale mal, has esto
# else -> codigo adicional que se ejecuta si no hay una excepcion
# finalmente -> finaly -> pase lo que pase, haz esto


'''def suma():
    n1 = int(input('n1: '))
    n2 = int(input('n2: '))
    print(n1 + n2)
    print('Gracias')'''

'''try:
    # codigo que se quiere probar
    suma()
except:
    # codigo a ejecutar si hay un error
    print('Algo no ha salido bien')
else:
    # codigo que se ejecute si no hay un error, codigo adicional a try
    print('Hiciste todo bien')
finally:
    # codigo que se va a ejecutar de todos modos
    print('Eso fue todo')'''

'''def pedir_numero():
    while True:
        try:
            numero = int(input('Escribe un numero: '))
        except:
            print('Ese no es un numero')
        else:
            print(f'Ingresaste el numero {numero}')
            break
    print('Gracias')


pedir_numero()'''

'''def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")'''

# Pruebas de codigo!!!!
# pylint -> biblioteca que analiza el codigo e informa de problemas
# estilos -> pep(8) -> python

# pylint (script.py) -r y -> desde consola -> -r y se usa para genera un reporte


# unittest -> incorporada en python y permite ejecutar codigos para probarlos

'''
import unittest
import ModuloVacio


class ProbarCambiaTexto(unittest.TestCase):

    def test_mayusculas(self):
        palabra = 'Hello Hans'
        resultado = ModuloVacio.todo_mayusculas(palabra)
        self.assertEqual(resultado, 'HELLO HANS')


if __name__ == '__main__':
    unittest.main()
'''

# decoradores
# funciones que modifican el comportamiento de otras funciones

'''
def mayuscula(texto):
    # o evitar hacer esto
    #print('Hola')
    print(texto.upper())
    #print('Adios')


def minuscula(texto):
    print(texto.lower())
'''
# Para evitar hacer esto
'''
print('Hola')
mayuscula('Hello Hans')
print('Adios')
'''

# Se hace esto:

'''
def mayuscula(texto):
    print(texto.upper())


def minuscula(texto):
    print(texto.lower())


def una_funcion(funcion):
    return funcion


# mi_funcion = mayuscula
# mi_funcion('Python')

#una_funcion(mayuscula('Hello'))'''

'''
def cambiar_letras(tipo):

    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == 'may':
        return mayuscula

    elif tipo == 'min':
        return minuscula()


operacion = cambiar_letras('may')
operacion('Hello Hans')
'''

# uso de decoradores, lo malo es que siempre se van a usar
'''def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('Adios')
    return otra_funcion


@decorar_saludo
def mayuscula(texto):
    print(texto.upper())


@decorar_saludo
def minuscula(texto):
    print(texto.lower())


mayuscula('Hello Hans')
minuscula('Hello Hans')'''

# asi es como se hace para elegir usar o no los decoradores
'''
def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print('Hola')
        funcion(palabra)
        print('Adios')
    return otra_funcion


def mayuscula(texto):
    print(texto.upper())


def minuscula(texto):
    print(texto.lower())


mayuscula('Hello Hans')
mayuscula_decorada = decorar_saludo(mayuscula)
mayuscula_decorada('Hello Hans')
'''

# Genereadores

'''
def mi_funcion():
    return 4


def mi_generador():
    yield 4


print(mi_funcion())
print(mi_generador())
g = mi_generador()
print(next(g))
'''

'''
def mi_funcion():
    lista = []
    for x in range(1, 5):
        lista.append(x * 10)
    return lista


def mi_generador():
    for x in range(1, 5):
        yield x * 10


print(mi_funcion())
print(mi_generador())
a = mi_generador()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
'''

'''
def mi_generador():
    x = 1
    yield x
    x += 1
    yield x
    x += 1
    yield x


g = mi_generador()
print(next(g))
print(next(g))
print(next(g))
'''

'''
def numeros_infinitos():
    x = 0
    while True:
        x += 1
        yield x


generador = numeros_infinitos()
'''

'''
def mi_generador():
    x = 7
    while True:
        yield x
        x += 7


generador = mi_generador()
'''

'''
def mi_generador():
    vidas = 3
    if vidas == 3:
        yield f"Te quedan {vidas} vidas"
    while True:
        vidas -= 1
        if vidas == 2:
            yield f"Te quedan {vidas} vidas"
        elif vidas == 1:
            yield f"Te queda {vidas} vida"
        elif vidas == 0:
            yield "Game Over"
            break


perder_vida = mi_generador()
'''

#####################################################Proyecto 8 ##############################################


import numeros


def preguntar():
    print('Bienvenido a Farmacia Python')
    while True:
        print("""
        [P] - Perfumeria
        [F] - Farmacia
        [C] - Cosmetica
        """)
        try:
            mi_rubro = input('Elige una opcion: ').upper()
            ['P', 'F', 'C'].index(mi_rubro) # verifica si lo que llego por el input pertenece a la lista, si no genera un error
        except ValueError:
            print('...Esa no es una opcion valida')
        else:
            break
    numeros.decorador(mi_rubro)


def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input('Quieres sacar otro turno? [S/N]: ').upper()
            ['S', 'N'].index(otro_turno)
        except ValueError:
            print('Esa no es una opcion valida')
        else:
            if otro_turno == 'N':
                print('Gracias por su visita')
                break


inicio()
