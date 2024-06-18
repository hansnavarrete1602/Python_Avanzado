# Posibles funciones
'''
    def unpack(self, *args):
        if len(args) > 1:
            os.chdir(str(Path(args[1])))
            home = os.getcwd()
        else:
            home = os.getcwd()
        try:
            if len(args) == 1:
                shutil.unpack_archive(args[0], home, str(Path(args[0]).suffix).replace('.', ''))
            elif len(args) == 2:
                os.chdir(str(Path(args[1])))
                shutil.unpack_archive(args[0], str(Path(args[1])), str(Path(args[0]).suffix).replace('.', ''))
            else:
                shutil.copy(args[0], str(Path(args[2])))
                os.chdir(str(Path(args[2])))
                home = os.getcwd()
                shutil.unpack_archive(args[0], home, str(Path(args[0]).suffix).replace('.', ''))
                file = Path(home, args[0])
                send2trash.send2trash(file)
        except ValueError:
            return f'\n...La carpeta comprimida "{args[0]}" no se puede descompimir.'
        except shutil.ReadError:
            return f'\n...La carpeta comprimida "{args[0]}" no existe,\ntalvez se encuentre en otra direccion...'
        else:
            return f'\nLa carpeta "{args[0]}" ha sido descomprimida con exito!...'
'''