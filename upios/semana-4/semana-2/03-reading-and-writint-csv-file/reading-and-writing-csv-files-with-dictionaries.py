#!/usr/bin/env python3

import csv

# DictReader convierte cada fila del archivo csv en un diccionario.
# La primera fila nos los nombre de las columnas.

# with open('software.csv') as software:
#     reader = csv.DictReader(software)
#     for row in reader:
#         # print(("{} has {} users").format(row["name"],row["users"]))
#         print(f"{row['name']} has {row['users']} users")

# Crear el csv a partir de una colección de diccionarios
users = [
    {"name":"Sol Mansi","username":"solm","departament":"IT infrastructure"},
    {"name":"Lio Nelson","username":"lion","departament":"User experience research"},
    {"name":"Charly Grey","username":"greyc","departament":"Development"}]
keys = ["name","username","departament"]
with open('by_departament.csv', 'w') as by_departament:
    writer = csv.DictWriter(by_departament,fieldnames=keys)
    writer.writeheader()
    writer.writerows(users)
