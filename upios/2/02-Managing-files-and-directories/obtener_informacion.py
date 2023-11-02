#!/usr/bin/env python3
import os
import datetime

# Obtener información sobre los archivos usando 
# la función Path

# Ruta absoluta al archivo
print(f'Ruta absoluta: {os.path.abspath("spider.txt")}')

# Tamaño de un archico
print(os.path.getsize('spider.txt'))

# Fecha de creación del documento
print(f'Fecha de creación (timestamp) : {os.path.getmtime("spider.txt")}')

timestamp = os.path.getmtime('spider.txt')
print( f'Con el método fromtimestamp: {datetime.datetime.fromtimestamp(timestamp)}')