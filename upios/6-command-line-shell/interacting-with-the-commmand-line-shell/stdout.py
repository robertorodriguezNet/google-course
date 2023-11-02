#!/usr/bin/env python3

# El texto se muestra por la pantalla, que es la salida por defecto.
print("Don't mind me, just a bit of text here...")

# Modificamos la salida para que la dirija a un archivo de texto.
# Si el archivo existe, se sobre-escribe
# ./stdout.py > new_file.txt

# Anexar al contenido del archivo
# ./stdout.py >> new_file.txt

# Redirigir la entrada standard: < lee el contenido de un archivo
# y lo introduce como entrada del script que lo llama

# Redirigir el mensaje de error a un archivo
# ./streams_err.py < new_file.txt 2> error_file.txt
# "2>" es un descriptor de archivo que apunta a un recurso:
#   0 se usa para SCDIN y 1 para SCDOUT

# Rederigir un echo a un archivo
# echo "#usr/bin/env python3" > other_file.py