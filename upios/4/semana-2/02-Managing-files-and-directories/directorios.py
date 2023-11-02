#!/usr/bin/env python3
import os

# Obtener el directorio actual
print(f'Directorio actual: {os.getcwd()}')

# Crar un directorio
# if not os.path.exists('new_dir'):
#     print(f'Crear el directorio new_dir (os.mkir(\'new_dir\')): {os.mkdir("new_dir")}')
# else:
#     print(f'Cambiar al directorio new_dir (os.chdir(\'new_dir\')): {os.chdir("new_dir")}')
#     print(f'Nueva ruta: {os.getcwd()}')

# Eliminar un directorio
# if not os.path.exists('newer_dir'):
#     os.mkdir('newer_dir')
# else:
#     os.rmdir('newer_dir')

# Operador ternario
os.mkdir('newer_dir') if not os.path.exists('newer_dir') else os.rmdir('newer_dir')