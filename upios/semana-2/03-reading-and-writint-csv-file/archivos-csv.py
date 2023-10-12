#!/usr/bin/env python3

import csv

# Colección de coches
coches = []

# Abrir y leer el archivo csv
f = open('documento.csv')
csv_f = csv.reader(f)

# Iterar sobre el archivo
for row in csv_f:
    marca, modelo, color, matricula, combustuble = row
    # print(f"Marca: {marca}, modelo: {modelo}, color: {color}, matrícula: {matricula}, combustible: {combustuble}")
    coches.append([marca, modelo, color, matricula, combustuble])

f.close()

# Guardar los coches en un nuevo csv
# coches.csv está abierto para escribir
with open('coches.csv', 'w') as coches_csv:
    writer = csv.writer(coches_csv)
    writer.writerows(coches)