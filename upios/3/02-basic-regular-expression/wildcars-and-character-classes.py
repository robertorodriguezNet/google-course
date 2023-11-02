#!/usr/bin/env python3

import re

# Clases de caracteres
# [a-z], [A-Z], [a-zA-Z], [0-9]
print(re.search(r"[Pp]ython","python"))

# Busca la cadena que no contenga 
# [^a-z]

# Busca la primera cadena que no contenga una letra
print(re.search(r"[^a-zA-Z]","This is a sentence whith espaces.")) # span(4,5) match(' ')
print(re.search(r"[^a-zA-Z ]","This is a sentence whith espaces.")) # span(32,33) match('.')

# Operador OR 
print(re.search(r"cat|dog", "I like cat."))

# Encontrar todo: findall
print(re.findall(r"cat|dog", "I like cat."))