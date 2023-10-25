#!/usr/bin/env python3

import os
from pathlib import Path, PurePath

# @see https://youtu.be/80Z7ojUn3ao

# ----------------------------------------------------------------------
# Obtener la ruta
# os.getcwd() devuelve una cadena de texto
# print("Ruta actual con os.getcwd(): " + os.getcwd())

# Path.cwd() devuelve una clase de Path
# print("Ruta con pathlib.Path.cwd(): " + str(Path.cwd()))

# ----------------------------------------------------------------------
# Listar archivos o carpetas 
# print(os.listdir())

# Listar un directorio concreto
# print(os.listdir('archivos-y-directorios'))

# list() se usa para obtener el texto del objeto Path
# print(list(Path().iterdir()))
# print(list(Path('archivos-y-directorios').iterdir()))

# ----------------------------------------------------------------------
# Concatener directorios
# print(os.path.join(os.getcwd(), 'tmp'))

# print(PurePath.joinpath(Path.cwd(), 'tmp'))

# ----------------------------------------------------------------------
# CREAR DIRECTORIOS
# os.mkdir('Dataset')
# os.rmdir('Dataset')

# Subcarpeta: debemos unir los directorios con join para evitar
# los errores con los diferentes SO
# os.makedirs(os.path.join('Dataset', 'Scripts'))

# El parámetro exist_ok=True evita el error si el directorio existe
# Path('Dataset').mkdir(exist_ok=True)
# Path('Dataset').rmdir()

# parents=True permite crear subcarpetas
# PurePath.joinpath(Path.cwd(), 'Dataset','Scripts').mkdir(parents=True)

# ----------------------------------------------------------------------
# RENOMBRAR DIRECTORIOS
# os.rename('Dataset','Data')

# path_actual = Path('Data')
# path_final = Path('Dataset')
# Path.rename(path_actual,path_final)

# Renombrar los arcivos
# f'xxxx' es concatener texto
# for file in os.listdir():
#     if file.endswith('.txt'):
#         os.rename(file, f'2023_{file}')

# ----------------------------------------------------------------------
# COMPROBAR SI EXISTE UNA RUTA O UNA CARPETA

# print(os.path.exists('Dataset'))
# directorio = Path(PurePath.joinpath(Path.cwd(),'archivos-y-directorios','Dataset'))
# print(directorio.exists())

# ----------------------------------------------------------------------
# METADATA
# print(os.path.abspath('Dataset'))

file = Path('novel.txt')
print(file.resolve())
print(file.stem)
print(file.suffix)
print(f'{file.stat().st_size}kb')



