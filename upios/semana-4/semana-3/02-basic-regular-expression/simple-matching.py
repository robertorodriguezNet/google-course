#!/usr/bin/env python3
import re

# re es el módulo que se usa para aplicar las RegEx en Python

# r significa es una cadena sin procesar (Rawstring) por lo tanto
# no se debería interpretar ningún carácter especial y pasar
# la cadena tal y como está.
result = re.search(r"aza","plaza")
print(result)
result = re.search(r"eme","plaza") # None
print(result)

print(re.search(r"^x","Xenon"))  # None
print(re.search(r"^x", "Xenon", re.IGNORECASE))
print(re.search(r"p.ng","penguin"))
