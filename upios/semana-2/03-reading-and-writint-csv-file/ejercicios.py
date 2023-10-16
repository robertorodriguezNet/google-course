#!/usr/bin/env python3

import os
import csv

# # 1.- -------------------------------------------------------------------------
# # Estamos trabajando con una lista de flores y algo de información sobre cada
# # una de ellas. La función create_file escribe esta información en un CSV.
# # La función content_of_file lee este archivo en registros y devuelve la infor-
# # mación en un bloque bien formateado.

# # Create a file with data in it
# def create_file(filename):
#     with open(filename, "w") as file:
#         file.write("name,color,type\n")
#         file.write("carnation,pink,annual\n")
#         file.write("daffodil,yellow,perennial\n")
#         file.write("iris,blue,perennial\n")
#         file.write("poinsettia,red,perennial\n")
#         file.write("sunflower,yellow,annual\n")

# # Read the file contents and format the information about each row
# def contents_of_file(filename):
#     return_string = ""

#     # Call the function to create the file
#     create_file(filename)

#     # Open the file
#     with open(filename) as filename_read:
#         # Read the rows of the file into a dictionary
#         reader = csv.DictReader(filename_read)

#         # Precess each rows of the dictionary
#         for row in reader:
#             return_string += f"a {row['color']} {row['name']} is {row['type']}\n"

#         return return_string
    
# #Call the funcion
# print(contents_of_file('flowers.csv'))

# 2.- -------------------------------------------------------------------------
# Usando el archivo csv de flores, completar para procesar los datos sin con-
# vertirlos en un diccionario.

# Create a file with data in it
def create_file(filename):
    with open(filename, "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")

# Read the file contents and format the information about each row
def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open de file
    f = open(filename)
    csv_f = csv.reader(f)

    for row in csv_f:
        name,color,type = row
        return_string += f"a {name} {color} is {type}\n"
    return return_string

# Call the funtion
print(contents_of_file('flowers.csv'))