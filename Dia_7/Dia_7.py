# Object Oriented Programming (OOP)
# obbjeto -> se le llama clase
# las caracterisiticas de un objeto se le llaman atributos (color, tipo de pelo, etc)
# las funcionalidades se le dicen metodos (volar, correr, etc)
# un objeto es una instancia de una clase

# principios o pilares basicos de la OOP:
# herencia
# polimorfismo
# cohesion
# abstraccion
# acoplamiento
# encapsulamiento

# Clases:

'''
class Pajaro:
    pass


mi_pajaro = Pajaro()
otro_pajaro = Pajaro()
print(mi_pajaro)
print(type(mi_pajaro))
print(otro_pajaro)
print(type(mi_pajaro))
'''

# Atributos
# atributos de clase -> pertenecen a la clase (alas = True)
# atributos de instancia -> pertencen a la instancia o al objeto (color = 'negro')

# Atributos de instancia:

'''
class Pajaro:

    # contructor de atributos iniciales
    # python siempre va a revisar esto ya que es lo que se necesita para crear un objeto
    def __init__(self, color, especie): # color es el primer atributo
        self.color = color # self representa la instancia del objeto que va a ser creado
        self.especie = especie


mi_pajaro = Pajaro('rojo', 'Tucan')
print(mi_pajaro.color) # se llama los atributos con "."
print(mi_pajaro.especie)
'''

# Atributos de clase:

'''
class Pajaro:

    alas = True # es un atributo que comparten todos los objetos 

    # contructor de atributos iniciales
    # python siempre va a revisar esto ya que es lo que se necesita para crear un objeto
    def __init__(self, color, especie): # color es el primer atributo
        self.color = color # self representa la instancia del objeto que va a ser creado
        self.especie = especie


mi_pajaro = Pajaro('rojo', 'Tucan')
print(mi_pajaro.color) # se llama los atributos con "."
print(mi_pajaro.especie)
print(mi_pajara.alas)
print(Pajaro.alas)
'''

'''
class Casa:

    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos


casa_blanca = Casa('blanco', 4)
'''

'''
class Cubo:
    caras = 6

    def __init__(self, color):
        self.color = color


cubo_rojo = Cubo('rojo')
'''

'''
class Personaje:
    real = False

    def __init__(self, especie, magico, edad):
        self.especie = especie
        self.magico = magico
        self.edad = edad


harry_potter = Personaje('Humano', True, 17)
'''

# Metodos
# metodos = funciones

'''
class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    def piar(self): # self es obligatorio y se refiere al objeto ya creado
        print('pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'He volado {metros} mts')


piolin = Pajaro('amarillo', 'canario')
piolin.piar()
piolin.volar(50)
'''

'''
class Perro:

    def __init__(self):
        pass

    def ladrar(self):
        print('Guau!')


mi_perro = Perro()
mi_perro.ladrar()
'''

'''
class Mago:

    def __init__(self):
        pass

    def lanzar_hechizo(self):
        print('¡Abracadabra!')


merlin = Mago()
merlin.lanzar_hechizo()
'''

'''
class Alarma:

    def __init__(self):
        pass

    def postergar(self, cantidad_minutos):
        print(f'La alarma ha sido pospuesta {cantidad_minutos} minutos')


mi_alarma = Alarma()
mi_alarma.postergar(10)
'''

# Tipos de metodos
# decoradores -> permiten crear distintos tipos de metodos

# metodos de instancia -> se crean como def x(self)
# acceden y modifican atributos del objeto
# acceder a otros metodos
# modificar el estado de la clase

# metodos de clase -> @classmethod
# cls -> clase
# no estan asociados a las instancias sino a la misma clase
# no pueden acceder a los atributos de instancia pero si pueden modificar los atributos de la clase
# se definen asi:
'''
@classmethod
def mi_metodo(cls):
    print('algo')
'''
#

# metodos estaticos -> @staticmethod
# no aceptan como parametro nada
# no puedo modificar el estado de la clse ni de la instancia, solo puede recibir parametros de entrada
# son funciones normales, pero van ligados a una clase concreta
# se declara asi:
'''
@staticmethod
def mi_metodo():
    print('algo')
'''

'''
class Pajaro:

    alas = True

    def __init__(self, color, especie):
        self.color = color
        self.especie = especie

    #metodos de instancias porque afectan a self
    def piar(self):
        print('pio, mi color es {}'.format(self.color))

    def volar(self, metros):
        print(f'He volado {metros} mts')
        self.piar()

    def pintar_negro(self):
        self.color = 'negro'
        print(f'Ahora el pajaro es de color {self.color}')

    # metodos de clase relacionado a la clase cls
    # puede modificar los metodo de clase
    @classmethod
    def poner_huevos(cls, cantidad):
        print(f'puso {cantidad} huevos')
        cls.alas = False
        print(Pajaro.alas)

    @staticmethod
    def mirar():
        #self.color -> error
        #cls.alas -> error
        print('El pajaro mira')


"""
# metodos de instancia y propiedades
piolin = Pajaro('amarillo', 'canario')
piolin.piar()
piolin.volar(50)
piolin.pintar_negro()
piolin.alas = False
print(piolin.alas)
"""

"""
# Metodo de clase
Pajaro.poner_huevos(5) # se ejecuta sin haber declarado un objeto
#Pajaro.piar() -> error porque no se ha declarado un objeto
"""

"""
# metodo static
Pajaro.mirar()
"""
'''

'''
class Mascota:

    def __init__(self):
        pass

    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")


Mascota.respirar()
'''

'''
class Jugador:
    vivo = False

    def __init__(self):
        pass

    @classmethod
    def revivir(cls):
        cls.vivo = True
        print(cls.vivo)
'''

'''
class Personaje:

    def __init__(self, cantidad_flechas):

        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):

        self.cantidad_flechas -= 1


Hans = Personaje(30)
Hans.lanzar_flecha(
'''

# Herencia
# se manejas clases padre y clases hijas
# la clase hija hereda atribtos de la clase padre y tambien los puede modificar
# DRY -> Don't repeat yourself -> no repitas codigo -> filosofia de la herencia
'''
class Animal:
    def nacer(self):
    def morir(self):
    def respirar(self):

class Pajaro(Animal):
    [codigo]

class Mamifero(Animal):
    [codigo]

class Insecto(Animal):
    [codigo]
'''

'''
class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')


class Pajaro(Animal):
    pass


class Insecto(Animal):
    pass


print(Pajaro.__bases__) # bases me dice de quien hereda
print(Animal.__subclasses__()) # subclasses a quien hereda
piolin = Pajaro(2, 'amarillo')
piolin.nacer()
print(piolin.color)
print(piolin.edad)
abeja = Insecto(1, 'negro')
abeja.nacer()
print(abeja.color)
print(abeja.edad)
'''

'''
class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


class Alumno(Persona):
    pass
'''

'''
class Mascota:

    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas


class Perro(Mascota):
    pass
'''

'''
class Vehiculo:

    def acelerar(self):
        pass

    def frenar(self):
        pass


class Automovil(Vehiculo):
    pass
'''

# Herencia extendida
# La clase hija puede:
# tener metodos heredados de la clase padre
# tener metodos modificados de la clase padre
# tener metodos nuevos que no estan en la clase padre

'''
class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color

    def nacer(self):
        print('Este animal ha nacido')

    def hablar(self):
        print('Este animal emite un sonido')

class Pajaro(Animal):

    def __init__(self, edad, color, altura_vuelo):
        # si no se quiere volver a escribir el mismo constructor del padre
        #self.edad = edad
        #self.color = color
        # se usa supper() y este hereda ya lo atributos del padre
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print('pio')

    def volar(self, metros):
        print(f'El pajaro vuela {metros} mts')


piolin = Pajaro(3, 'amarillo', 60)
piolin.hablar() # hereda el propio
piolin.volar(50)
animal = Animal(5, 'negro')
animal.hablar()
'''

# Herencia multiple
# una clase puede heredar de muchas clases al mismo tiempo

'''
class Padre:
    def hablar(self):
        print('Hola')


class Madre:

    def reir(self):
        print('JaJaJa')

    def hablar(self):
        print('que tal')


class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


mi_nieto = Nieto()
mi_nieto.hablar() # primero heredo de Padre, hay un orden de busqueda
mi_nieto.reir()
print(Nieto.__mro__) # para saber el arbol de la clase ue va de izquierda a derecha
'''

'''
class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")


class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")


class Hija(Madre, Padre):
    pass
'''

'''
class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Pez, Reptil, Ave, Mamifero):
    pass
'''

'''
class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"


class Hijo(Padre):

    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"
'''

# Polimorfismo -> muchas formas, los objetos toman diferentes formas
# diferentes objetos pueden compartir diferentes metodos

'''
class Vaca:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + 'dice muuuu')

class Oveja:

    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(self.nombre + ' dice beee')


vaca1 = Vaca('Aurora')
oveja1 = Oveja('Nube')

"""
animales = [vaca1, oveja1]
for animal in animales:
    animal.hablar()
"""


def animal_habla(animal):
    animal.hablar()


animal_habla(vaca1)
animal_habla(oveja1)
'''

'''
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

lst = [palabra, lista, tupla]

for n in lst:
    print(len(n))
'''

'''
class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

x = Arquero()
y = Mago()
z = Samurai()

personajes = [x,y,z]

for n in personajes:
    n.atacar()
'''

'''
class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

def personaje_defender(personaje):
    personaje.defender()
'''

# metodos especiales -> __init__, __mro__, __bases__, etc

'''
mi_lista = [1,1,1,1,1]
print(len(mi_lista))


class Objeto:
    pass

mi_objeto = Objeto()
#print(len(mi_objeto)) # error el objeto no tiene largo
print(mi_objeto)
'''

'''
class CD:

    def __init__(self, autor, titulo, canciones):
        self.autor = autor
        self.titulo = titulo
        self.canciones = canciones

    # se puede modificar una clase de python
    def __str__(self):
        return f'Album: {self.titulo} de {self.autor}'

    def __len__(self):
        return self.canciones

    def __del__(self):
        print('Se ha eliminado el CD {}'.format(self.titulo))

mi_cd = CD('Pink Floyd', 'The Wall', 24)
print(mi_cd)
print(str(mi_cd))
print(len(mi_cd))

del mi_cd # del elimina algo
'''

'''
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'
'''

'''
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __len__(self):
        return self.cantidad_paginas
'''

'''
class Libro():
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __del__(self):
        print('Libro eliminado')
'''

#####################################################Proyecto 7 ##############################################


class Persona:

    def __init__(self, nombre, apellido):
        self.name = nombre
        self.surname = apellido


class Cliente(Persona):

    def __init__(self, nombre, apellido, numero_cuenta, balance = 0):
        super().__init__(nombre, apellido)
        self.account_number = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"""
                {'*' * 35}
                \tUser info:
                \tUser name = {self.name + '  ' + self.surname} 
                \tUser account = {self.account_number}
                \tUser balance = {self.balance}        
                {'*' * 35}
                """

    def depositar(self, monto):
        self.balance += monto
        print('Deposito aceptado')

    def retirar(self, monto):
        if self.balance >= monto:
            self.balance -= monto
            print('Retiro realizado')
        else:
            print('Fondos insuficientes')


def create_user():
    name_ = input('Input name: ')
    surname_ = input('Input surname: ')
    account_n = input('Input account number: ')
    cliente = Cliente(name_, surname_, account_n)
    return cliente


def inicio():
    user_ = create_user()
    print(user_)
    opcion = 0
    while opcion.lower() != 's':
        print('Elige: Depositar [D], Retirar [R], o Salir [S]')
        opcion = input()
        if opcion.lower() == 'd':
            monto_ = int(input('Monto a depositar: '))
            user_.depositar(monto_)
        elif opcion.lower() == 'r':
            monto_r = int(input('Monto a retirar: '))
            user_.retirar((monto_r))
        print(user_)
    print('Gracias por usar Banco Python')


inicio()
