#!/usr/bin/env python3
import os
import datetime

# La función create_python_script crea un nuevo script de Python en el directorio actual, le agrega la línea de comentarios y devuelve el tamaño.
# def create_python_script(filename):
#     comments = "# Start of a new Python program"
#     with open(filename, 'w') as file:
#         file.write(comments)

#     filesize = os.path.getsize(filename)
#     return(filesize)

# print(create_python_script('program.py'))

# -----------------------------------------------------------------------------
# La función new_directory crea un nuevo directorio dentro del directorio de 
# trabajo actual, luego crea un nuevo archivo vacío dentro del nuevo directorio
# y devuelve la lista de archivos en ese directorio.
# def new_directory(directory, filename):

#     if os.path.isdir(directory) == False:
#         os.mkdir(directory)

#     os.chdir(directory)
#     with open(filename, 'w') as file:
#         pass

#     return os.listdir(os.getcwd())

# print( new_directory('PythonPrograms','script.py'))

# -----------------------------------------------------------------------------
# La función file_date crea un nuevo archivo en el didrectorio actual,
# verifica la fecha en que se modificó el archivo y devuelve solo la 
# parte de la fecha de la marca de tiempo en el formato aaaa-mm-dd.
def file_date(filename):

    if not os.path.exists(filename):
        with open(filename, 'w'):
            pass
        
    timestamp = os.path.getmtime(filename)
    fecha= datetime.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")

    return (f"{fecha}")


print(file_date('newfile.txt'))

# -----------------------------------------------------------------------------
# La función parent_directory duvuelve el nombre del directorio que se 
# encuentra justo encima del directorio actual.
# def parent_directory():

#     relative_parent = os.path.join(os.getcwd(),'..')
#     os.chdir(relative_parent)

#     return os.getcwd()

# print(parent_directory())