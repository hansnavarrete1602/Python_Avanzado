from pathlib import Path
import send2trash
import datetime
import zipfile
import shutil
import os


class Pypack:

    def __init__(self):
        pass

    def unpack(self, **kwargs):
        today = datetime.date.today()
        name = f'Uncompress_Folder_{today.day}_{today.month}_{today.year}'
        home = os.getcwd()
        f = Path(home, name)
        try:
            if 'folder' in kwargs and 'origin' in kwargs and 'destination' in kwargs:
                shutil.copy(Path(kwargs.get('origin'),kwargs.get('folder')), str(Path(kwargs.get('destination'))))
                os.chdir(str(Path(kwargs.get('destination'))))
                home = os.getcwd()
                shutil.unpack_archive(kwargs.get('folder'), f,
                                      str(Path(kwargs.get('folder')).suffix).replace('.', ''))
                file = Path(home, kwargs.get('folder'))
                send2trash.send2trash(file)
            elif 'folder' in kwargs and 'origin' in kwargs:
                os.chdir(str(Path(kwargs.get('origin'))))
                home = os.getcwd()
                f = Path(home, name)
                shutil.unpack_archive(kwargs.get('folder'), f,
                                      str(Path(kwargs.get('folder')).suffix).replace('.', ''))
            elif 'folder' in kwargs and 'destination' in kwargs:
                shutil.copy(kwargs.get('folder'), str(Path(kwargs.get('destination'))))
                os.chdir(str(Path(kwargs.get('destination'))))
                home = os.getcwd()
                f = Path(home, name)
                shutil.unpack_archive(kwargs.get('folder'), f,
                                      str(Path(kwargs.get('folder')).suffix).replace('.', ''))
                file = Path(home, kwargs.get('folder'))
                send2trash.send2trash(file)
            elif 'folder' in kwargs:
                shutil.unpack_archive(kwargs.get('folder'), f,
                                      str(Path(kwargs.get('folder')).suffix).replace('.', ''))
            else:
                return '\n...Debes de ingresar almenos una constante correcta'
        except ValueError:
            return f"\n...La carpeta comprimida '{kwargs.get('folder')}' no se puede descompimir."
        except shutil.ReadError:
            return f"\n...La carpeta comprimida '{kwargs.get('folder')}' no existe,\ntalvez se encuentre en otra direccion..."
        except FileNotFoundError:
            return f"\n...Revisa bien los datos ingresados"
        else:
            return f'\nUncompress in the folder "{name}"'

    def pack(self, **kwargs):
        today = datetime.date.today()
        name = f'Compress_Folder_{today.day}_{today.month}_{today.year}.zip'
        try:
            if 'files' in kwargs and 'origin' in kwargs and 'destination' in kwargs:
                Zip = zipfile.ZipFile(Path(kwargs.get('destination'), name), 'w')
                if type(kwargs.get('files')) == list or type(kwargs.get('files')) == tuple:
                    for i in range(len(kwargs.get('files'))):
                        Zip.write(Path(kwargs.get('origin'), f"{kwargs.get('files')[i]}"))
                else:
                    Zip.write(Path(kwargs.get('origin'), f"{kwargs.get('files')}"))
                Zip.close()
            elif 'files' in kwargs and 'origin' in kwargs:
                Zip = zipfile.ZipFile(name, 'w')
                if type(kwargs.get('files')) == list or type(kwargs.get('files')) == tuple:
                    for i in range(len(kwargs.get('files'))):
                        Zip.write(Path(kwargs.get('origin'),f"{kwargs.get('files')[i]}"))
                else:
                    Zip.write(Path(kwargs.get('origin'),f"{kwargs.get('files')}"))
                Zip.close()
            elif 'files' in kwargs and 'destination' in kwargs:
                Zip = zipfile.ZipFile(Path(kwargs.get('destination'), name), 'w')
                if type(kwargs.get('files')) == list or type(kwargs.get('files')) == tuple:
                    for i in range(len(kwargs.get('files'))):
                        Zip.write(kwargs.get('files')[i])
                else:
                    Zip.write(kwargs.get('files'))
                Zip.close()
            elif 'files' in kwargs:
                Zip = zipfile.ZipFile(name, 'w')
                if type(kwargs.get('files')) == list or type(kwargs.get('files')) == tuple:
                    for i in range(len(kwargs.get('files'))):
                        Zip.write(kwargs.get('files')[i])
                else:
                    Zip.write(kwargs.get('files'))
                Zip.close()
            else:
                return '\n...Debes de ingresar almenos una constante correcta'
        except FileNotFoundError:
            return f"\n...Revisa bien el nombre de los datos suministrados"
        else:
            return f'\nCompress with name "{name}"'



carpeta = 'Europa.zip'
carpeta2 = 'mi_web.zip'
carpeta3 = 'archivo_comprimido.zip'
direccion = "C:\\Users\\hansn\\OneDrive\\Escritorio"
direccion2 = 'C:\\Users\\hansn\\Downloads'
direccion3 = 'C:\\Users\\hansn\\PycharmProjects\\Curso_Python_Avanzado\\Dia_9'

z = Pypack() # Se crea la instancia de la clase

# print(z.unpack(folder=carpeta3)) # Si la funcion "unpack" recibe solo un argumento, esta descomprime la carpeta dentro del directorio de trabajo
# print(z.unpack(folder=carpeta2, origin=direccion2))
# print(z.unpack(folder=carpeta3, destination=direccion2))
# print(z.unpack(folder=carpeta, origin=direccion, destination=direccion2))

#print(z.pack(files='Dia_9.py'))
#print(z.pack(files=['Dia_9.py','prueba.txt','prueba1.txt']))
#print(z.pack(files='Dia_9.py', destination="C:\\Users\\hansn\\OneDrive\\Escritorio"))
#print(z.pack(files=['Dia_9.py','prueba.txt','prueba1.txt'], destination="C:\\Users\\hansn\\OneDrive\\Escritorio"))
#print(z.pack(files=['Sin título.png','Sin título2.png','Sin título3.png'], origin="C:\\Users\\hansn\\OneDrive\\Escritorio"))
#print(z.pack(files='Sin título3.png', origin="C:\\Users\\hansn\\OneDrive\\Escritorio"))
#print(z.pack(files=['Sin título.png','Sin título2.png','Sin título3.png'], origin="C:\\Users\\hansn\\OneDrive\\Escritorio", destination='C:\\Users\\hansn\\Downloads'))
#print(z.pack(files='Sin título3.png', origin="C:\\Users\\hansn\\OneDrive\\Escritorio", destination='C:\\Users\\hansn\\Downloads'))
