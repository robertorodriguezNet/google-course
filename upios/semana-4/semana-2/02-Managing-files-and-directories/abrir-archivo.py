#!/usr/bin/env puthon3

# Abrir y leer archivos

# El bloque 'with' encierra las operaciones con open()
# y cierra automáticamente el archivo.
# Usar libremente el File Descriptor permite usar el archivo
# en cualquier lugar.
with open('spider.txt') as file:
    for line in file:
        # strip() elimina también los saltos de línea
        print(line.strip().upper()) 

# Si el archivo no existe, lanza error, no se crea
# file en un File Descriptor, un token generado por el SO
file = open('spider.txt')

# Acciones sobre el file Descriptor
# El puntero queda en la línea siguiente
# print(file.readline())

# Escribe todas las líneas en una sola, sin los saltos 
# print(file.readlines())

# Escribe todas las líneas
# Si se ejecuta readlines previamente, el puntero ha quedado
# al final del archivo y no se mostrará nada
# print(file.read())

lines = file.readlines()

file.close()

# Ordenar las líneas
lines.sort()
print(lines)