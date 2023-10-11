#!/usr/bin/env python3

# w re-escribe el fichero. No crea el fichero.
# r solo lectura. Modo por defecto, no es necesario pasarla.
# a añade al final del archivo
with open("novel.txt", 'w') as file:
    file.write("It was a dark and strom night")

with open("novel.txt", 'a') as file:
    file.write("\nIt was a dark and strom day")