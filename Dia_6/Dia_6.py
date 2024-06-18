#Abrir y manipular archivos
# abrir -> open()
# leer -> read(): lee el archivo completo, readline(): lee linea por linea, readlines(): devuelve todas las lineas como una lista
# escribir -> write()
# cerrar -> close()

'''
mi_archivo = open('prueba.txt')
#print(mi_archivo)
#print(mi_archivo.read())
#print(mi_archivo.readline().upper()) #funciona como string y se le aplican sus metodos
#print(mi_archivo.readline().rstrip()) #rstrip() nos ayuda a eliminar el salto de linea al final
#print(mi_archivo.readline())
#for l in mi_archivo:
#    print('Aqui dice: ' + l)
todas = mi_archivo.readlines()
print(todas)
todas = todas.pop()
print(todas)
mi_archivo.close()
'''

#Crear y escribir archivos
#open(name,op) -> op: r = solo lectura (x defecto), w = solo escritura (si existe resetea el archivo), a = el cursor se pone al final para agregar lineas
#writelines(opt) -> opt = lista de strings pero concatenado

'''
archivo = open('prueba1.txt', 'w')
archivo.write('soy el nuevo texto')
archivo.write('\n')
archivo.write('pegado')
archivo.write('''
#Hola
#Hans
#Navarrete
''')
archivo.writelines(['Hola', 'Hans', 'Navarrete'])
lista = ['Hola', 'Hans', 'Navarrete']
for p in lista:
    archivo.writelines(p + '\n')
archivo.close()
'''

'''
archivo = open('prueba1.txt', 'a')
archivo.write('Bienvenido')
archivo.close()
'''

'''
archivo = open('mi_archivo.txt', 'w')
archivo.write('Nuevo texto')
archivo.close()
archivo = open('mi_archivo.txt', 'r')
print(archivo.read())
archivo.close()
'''

'''
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
archivo = open('registro.txt', 'a')
for p in registro_ultima_sesion:
    archivo.writelines(p + '\t')
archivo.close()
archivo = open('registro.txt', 'r')
print(archivo.read())
archivo.close()
'''

#Directorios
#Windows -> las direcciones son asi: c:\users\mipc\archivo.txt, para que python lo interprete:
#c:\\users\\mipc\\archivo.txt
#Mac -> c:/users/mipc/archivo.txt
#para solucionar e identificar esto se utiliza
#Path -> para manejar las rutas
#os -> para manejar el sistema operativo


#import os

#ruta = os.getcwd() # getcwd -> get current work directory (devuelve la ruta en donde esta el codigo)
#print(ruta)

#ruta = os.chdir('C:\\Users\\hansn\\PycharmProjects\\Clase_3\\Archivos\\clase_6') # chdir -> change directory (establecer una ruta distinta)
#print(ruta)
#archivo = open('prueba.txt')
#print(archivo.read())
#archivo.close()

#ruta = os.makedirs('C:\\Users\\hansn\\PycharmProjects\\Clase_3\\otra') # makedirs -> crear directorio
#print(ruta)

'''
ruta = 'C:\\Users\\hansn\\PycharmProjects\\Clase_3\\otra\\prueba2.txt'
elemento = os.path.basename(ruta) #basename = nombre base
directorio = os.path.dirname(ruta) #dirname = nombre de ruta
tupla = os.path.split(ruta) #separar ambos en una tupla
os.rmdir('C:\\Users\\hansn\\PycharmProjects\\Clase_3\\Archivos\\clase_6') #rmdir = remove directory (tiene que estar vacio)
print(elemento)
print(directorio)
print(tupla)
'''

#archivo = open('C:\\Users\\hansn\\PycharmProjects\\Clase_3\\prueba.txt')

#con Path se puede crear una ruta para ser abierta en cualquier sistema operativo
'''
from pathlib import Path

carpeta = Path('/Users/hansn/PycharmProjects/Clase_3') / 'prueba.txt'

mi_archivo = open(carpeta)
print(mi_archivo)
'''

#pathlib
#pureWindowsPath = transforma en windows

'''
from pathlib import Path, PureWindowsPath

carpeta = Path('/Users/hansn/PycharmProjects/Clase_3/prueba.txt')
print(carpeta.read_text()) #read_text = leer contenido
print(carpeta.name) #nombre del archivo
print(carpeta.suffix) #terminacion es decir ej: txt
print(carpeta.stem) #nombre archivo sin terminacion

if not carpeta.exists():
    print('este archivo no existe')
else:
    print('existe')

print(PureWindowsPath(carpeta)) #se adapta al formato de windows
'''

#Path
#util para crear, mover, enumerar archivos
#mi_ruta = Path('Europa','España','Barcelona','Sagrada_familia.txt)
#print(mi_ruta) -> Europa/España/Barcelona/Sagrada_familia.txt


#from pathlib import Path

'''
base = Path.home() #devuelve la ruta absoluta del directorio principal del usuario actual
guia = Path('barcelona','iglesia')
print(base)
print(guia)
guia = Path(base,'barcelona','iglesia')
print(guia)
guia = Path(base,'barcelona','iglesia', Path('Silla', 'madera'))
print(guia)
print(guia.parent) # devuelve la ruta anterior
guia2 = guia.with_name('pedrera.txt') #with_name copia el nombre
print(guia2)
'''

'''
guia = Path(Path.home(), 'Europa')
#glob() -> global, *.txt -> * todos los .txt
for txt in Path(guia).glob("*.txt"):
    print(txt)
#glob('**/*.txt) -> busca en todas las carpetas y subcarpetas del diretorio
for carpetas_subcarpetas in Path(guia).glob('**/*.txt'):
    print(carpetas_subcarpetas)
'''

'''
guia = Path('Europa', 'España', 'iglesia.txt')
en_europa = guia.relative_to(Path('Europa'))
en_espana = guia.relative_to(Path('Europa', 'España'))
print(en_europa)
print(en_espana)
'''

#Limpiar consola
#from os import system
#system(opt) -> 'cls' (windows) , 'clear' (otros os)

'''
from os import system

nombre = input('Dime tu nombre: ')
edad = input('Dime tu edad: ')

system('cls') #cls -> clear screen

print('Tu nombre es {} y tu edad es {}'.format(nombre, edad))
'''

'''
def abrir_leer(a):
    archivo = open(a)
    return archivo.read()
'''

'''
def sobrescribir(a):
    archivo = open(a, 'w')
    archivo.write("contenido eliminado")
'''

'''
def registro_error(a):
    archivo = open(a, 'a')
    archivo.write("se ha registrado un error de ejecución")
'''

'''
from pathlib import Path
ruta = Path('c:/users/usuario/desktop/curso') / 'Cuestionario' / 'pregunta'
carpeta = ruta.parents[3]
print(carpeta)
'''

#####################################################Proyecto 6 ##############################################

from pathlib import Path, PureWindowsPath
from os import system
import shutil
import time
import os

home = Path(Path.home(), 'Recetas')


def category_choice():
    while True:
        try:
            system('cls')
            lst_categorias = []
            for root, dirs, files in os.walk(home, topdown=False):
                for name in dirs:
                    lst_categorias.append(os.path.join(root,name))
            print('Selecciona una categoria, escribiendo el numero de inidice que le corresponde')
            for i in range(len(lst_categorias)):
                print(f'{i+1}. {Path(lst_categorias[i]).stem}')
            a = input('¿Que categoria ecoge?: ')
            if a.isdigit():
                return int(a)-1, lst_categorias
            else:
                system('cls')
                print('...Lo siento, sebes de escribir el "numero" del inidice')
                time.sleep(3.5)
                continue
        except KeyboardInterrupt():
            break


def file_choice(a, b):
    while True:
        try:
            system('cls')
            lst_names = []
            guia = Path(b[a])
            for txt in Path(guia).glob("*.txt"):
                lst_names.append(txt.stem)
            if len(lst_names) != 0:
                print(f'Estas son las recetas que existen dentro de la categoria {guia.stem}"')
                print('Seleccione la receta, escribiendo el numero del inidice que le corresponde')
                for i in range(len(lst_names)):
                    print(f'{i+1}. {lst_names[i]}')
                c = input('¿Que receta selecciona?: ')
                if c.isdigit():
                    return b[a], lst_names[int(c)-1]
                else:
                    system('cls')
                    print('...Lo siento, sebes de escribir el "numero" del inidice')
                    time.sleep(3.5)
                    continue
            else:
                print('La categoria esta vacia...')
                time.sleep(3.5)
                return 0, 0
        except KeyboardInterrupt:
            break


def file_open(a, b):
    if a and b != 0:
        b = b + '.txt'
        categoria = Path(a)
        ruta = Path(a, b)
        system('cls')
        print(f'Carpeta raiz: {PureWindowsPath(home)}')
        print(f'Categoria: {categoria.stem}')
        print(f'Receta: {b.replace(".txt", "")}')
        print('\n')
        print(ruta.read_text())
        input()
    else:
        pass


def crear_archivo():
    system('cls')
    name = input('Escribe el nombre de la receta: ')
    system('cls')
    print('Empieza a escribir tu receta en la parte de abajo')
    print('Para terminar con tu escrito, escribe un renglon con solo un simbolo "#"')
    print('de esta manera el software entenderá que tu escrito de la receta ha culminado.')
    print('\n')
    lines = []
    while True:
        receta = input()
        if receta == '#':
            system('cls')
            break
        else:
            lines.append(receta + '\n')
    print('\n...Ahora debes de seleccionar la categoria en la que guardaras tu receta')
    time.sleep(3.5)
    a, b = category_choice()
    print(f'Categoria: {b[a]}')
    print(f'Nombre receta: {name}')
    print(''.join(lines))
    ch = input('\n¿Deseas almacenar la receta? [S/N]: ')
    if ch.lower() == 's':
        n = name + '.txt'
        f = Path(home, b[a], n)
        arch = open(f, 'w')
        arch.writelines(lines)
        arch.close()
        system('cls')
        print(f'receta almacenada en "{b[a]}" con el nombre "{name}"')
        time.sleep(3.5)
        pass
    elif ch.lower() == 'n':
        pass


def eliminar_archivo():
    system('cls')
    print('Ahora debes de seleccionar la categoria donde se encuentra la receta: ')
    a, b = category_choice()
    a, b = file_choice(a, b)
    b = b + '.txt'
    ruta = Path(home, a, b)
    os.remove(ruta)
    system('cls')
    print('Receta eliminada')
    time.sleep(3.5)


def crear_categoria():
    system('cls')
    name = input('Escribe el nombre de la categoria: ')
    ruta = Path(home, name)
    while True:
        if not os.path.exists(ruta):
            system('cls')
            os.mkdir(ruta)
            print(f'...La categoria {name} fue creada!')
            time.sleep(3.5)
            break
        else:
            system('cls')
            print(f'La categoria {name} ya existe...')
            print('...Debes de asignarle otro nombre')
            time.sleep(3.5)
            continue


def eliminar_categoria():
    a, b = category_choice()
    x = b[a]
    system('cls')
    ch = input(f'¿Seguro que quiere eliminar la categoria? [S/N]: ')
    if ch.lower() == 's':
        system('cls')
        shutil.rmtree(x)
        print(f'...categoria eliminada')
        time.sleep(3.5)
        pass
    else:
        system('cls')
        print('Esta bien, volviendo al menu...')
        time.sleep(3.5)
        pass


def menu():
    while True:
        try:
            system('cls')
            print('Carpeta del recetario:')
            print(home)
            print('\n')
            print('...Bienvenido a tu recetario')
            print('Menu:')
            print('1. Leer receta')
            print('2. Crear receta')
            print('3. Crear categoria')
            print('4. Eliminar Receta')
            print('5. Eliminar categoria')
            print('6. Salir del recetario')
            a = input('Seleccione una opcion, escribiendo el numero del indice: ')
            if a.isdigit():
                return int(a)
            else:
                system('cls')
                print('Lo siento, debes de escribir el "numero" del indice')
                time.sleep(3.5)
                continue
        except KeyboardInterrupt():
            break


def recetario():
    while True:
        try:
            c = menu()
            if c == 1:
                print('Ahora debes de seleccionar la categoria que deseas explorar: ')
                a, b = category_choice()
                c, d = file_choice(a, b)
                file_open(c, d)
                continue
            elif c == 2:
                crear_archivo()
                continue
            elif c == 3:
                crear_categoria()
                continue
            elif c == 4:
                eliminar_archivo()
                continue
            elif c == 5:
                eliminar_categoria()
                continue
            elif c == 6:
                system('cls')
                break
            else:
                system('cls')
                print(f'Lo siento "{c}", no es una opcion valida')
                print('selecciona una opcion dentro del menu')
                time.sleep(3.5)
                continue
        except KeyboardInterrupt:
            break


recetario()


#solucion profesor

'''
import os
from pathlib import Path
from os import system

mi_ruta = Path(Path.home(), "Recetas")


def contar_recetas(ruta):
    contador = 0
    for file in Path(ruta).glob("**/*.txt"):
        contador +=1
    return contador


def inicio():
    system('cls')
    print('*' * 50)
    print('*' * 5 + 'Bienvenido al administrador de recetas' + '*' * 5)
    print('*' * 50)
    print('\n')
    print(f'las recetas estan en: {mi_ruta}')
    print(f'total recetas: {contar_recetas(mi_ruta)}')
    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print('Elige una opcion: ')
        print("""
        [1] - leer recetas
        [2] - crear receta nueva
        [3] - crear categoria nueva
        [4] - eliminar receta
        [5] - eliminar categoria
        [6] - salir del programa""")
        eleccion_menu = input()
    return int(eleccion_menu)


def mostrar_categorias(ruta):
    print('Categorias:')
    ruta_categorias = Path(ruta)
    lista_categorias = []
    contador = 1
    for carpeta in ruta_categorias.iterdir():
        carpeta_str = str(carpeta.name)
        print(f'[{contador}] - {carpeta_str}')
        lista_categorias.append(carpeta)
        contador += 1
    return lista_categorias


def elegir_categoria(lista):
    eleccion_correcta = 'x'
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1,len(lista) + 1):
        eleccion_correcta = input('\nElige una categoria: ')
    return lista[int(eleccion_correcta) - 1]


def mostrar_recetas(ruta):
    print('Recetas:')
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1
    for receta in ruta_recetas.glob('*.txt'):
        receta_str = str(receta.name)
        print(f'[{contador}] - {receta_str}')
        lista_recetas.append(receta)
        contador += 1
    return lista_recetas


def elegir_receta(lista):
    eleccion_correcta = 'x'
    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1, len(lista) + 1):
        eleccion_correcta = input('\nElige una receta: ')
    return lista[int(eleccion_correcta) - 1]


def leer_receta(receta):
    print(Path.read_text(receta))


def crear_receta(ruta):
    existe = False
    while not existe:
        print('Escribe el nombre de tu receta: ')
        nombre_receta = input() + '.txt'
        print('Escribe tu nueva receta: ')
        contenido_receta = input()
        ruta_nueva = Path(ruta, nombre_receta)
        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f'Tu receta {nombre_receta} ha sido creada')
            existe = True
        else:
            print('Lo siento, esa receta ya existe')


def crear_categoria(ruta):
    existe = False
    while not existe:
        print('Escribe el nombre de la nueva categoria: ')
        nombre_categoria = input()
        ruta_nueva = Path(ruta, nombre_categoria)
        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f'Tu nueva categoria {nombre_categoria} ha sido creada')
            existe = True
        else:
            print('Lo siento, esa categoria ya existe')

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f'La receta {receta.name} ha sido eliminada')


def eliminar_categoria(categoria):
    Path(categoria).rmdir()
    print(f'La categoria {categoria.name} ha sido eliminada')


def volver_inicio():
    eleccion_regresar = 'x'
    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input('\nPresione "v" para volver al menu: ')


finalizar_programa = False
#Estructura del menu
#inicio()
while not finalizar_programa:
    menu = inicio()
    if menu == 1:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print('No hay recetas en esta categoria')
        else:
            mi_receta = elegir_receta(mis_recetas)
            leer_receta(mi_receta)
        volver_inicio()
        #mostrar categroias
        #elegir categoria
        #mostrar recetas
        #elegir recetas
        #leer receta
        #volver al inicio
    elif menu == 2:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        crear_receta(mi_categoria)
        volver_inicio()
        # mostrar categroias
        # elegir categoria
        #crear receta nueva
        #volver al inicio
    elif menu == 3:
        crear_categoria(mi_ruta)
        volver_inicio()
        #crear categoria
        #volver al inicio
    elif menu == 4:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(mi_categoria)
        if len(mis_recetas) < 1:
            print('No hay recetas en esta categoria')
        else:
            mi_receta = elegir_receta(mis_recetas)
            eliminar_receta(mi_receta)
        volver_inicio()
        # mostrar categroias
        # elegir categoria
        # mostrar recetas
        # elegir recetas
        # eliminar receta
        # volver al inicio
    elif menu == 5:
        mis_categorias = mostrar_categorias(mi_ruta)
        mi_categoria = elegir_categoria(mis_categorias)
        eliminar_categoria(mi_categoria)
        volver_inicio()
        # mostrar categroias
        # elegir categoria
        #eliminar categoria
        #volver al inicio
    elif menu == 6:
        finalizar_programa = True
        #finalizar programa
'''