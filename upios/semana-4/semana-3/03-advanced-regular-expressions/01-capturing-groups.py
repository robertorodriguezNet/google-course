#!/usr/bin/env python3

import re

# # Los Capturing Group son partes del patrón que están entre
# # paréntesis.
# result = re.search(r"^(\w*), (\w*)$","Lovelace, Ada")
# print(result) # match='lovelace,Ada'
# print(result.groups()) # ('Lovelace','Ada')

# # groups devuelve una matriz en la que el primer elemento
# # contiene el resultado de la coincidencia.
# print(result[0])
# print(result[1])
# print(result[2])

def rearrange_name(name):
    result = re.search(r"^(\w*), (\w*)$", name)
    if result is None:
        return name
    return(f"{result[2]}, {result[1]}")

print(rearrange_name("Lovelace, Ada")) # Ada, Lovelace
print(rearrange_name("Hopper, Grace M.")) # None -> modificar ([\w .])

