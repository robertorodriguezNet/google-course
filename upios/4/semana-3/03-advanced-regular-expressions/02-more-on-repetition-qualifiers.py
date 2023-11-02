#!/usr/bin/env python3

import re

# search devuelve la última coincidencia
print(re.search(r"[a-zA-Z]{5}","a ghost")) # match='ghost'
print(re.search(r"[a-zA-Z]{5}","a scary ghost appeared")) # match='appeared'

# finall devuelve un array con todas las apariciones
print(re.findall(r"[a-zA-Z]{5}","a scary ghost appeared")) # match=[]

# \b hace que se devuelvan la palbras completas, no las que contengan
# más caracteres de los indicados
# \b hace coincidir la búsqueda con el prinicio y final de las palabras
print(re.findall(r"\b[a-zA-Z]{5}\b","a scary ghost appeared")) # match=[]

# Rango
print(re.findall(r"\b[a-zA-Z]{5,10}\b","a scary ghost appeared")) # match=[]

# Más de la cantidad indicada
print(re.findall(r"\b[a-zA-Z]{5,}\b","a scary ghost appeared")) # match=[]