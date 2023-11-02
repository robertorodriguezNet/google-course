#!/usr/bin/env python3

import re

print(re.search(r".com","welcome")) # lcom
print(re.search(r"\.com","welcome")) # None

# Se usa para escapar conjuntos de caracteres predefinidos
# \w cualquier caracter alfanumérico y guiones bajos
# \d dígitos
# \s espacio en blanco, tabulación o nueva línea
# \b final de palabras
print(re.search(r'\w*','This is an example')) # This
print(re.search(r'\w*', 'And_this_is_another')) # And_this_is_another