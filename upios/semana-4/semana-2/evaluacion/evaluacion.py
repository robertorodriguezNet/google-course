#!/usr/bin/env python3

import os
import csv

# ---------------------------------------------------------
# El departamento de RR.HH. de una empresa quiere conocer
# cuántas personas hay en cada departamento.
# Hay que generar un informe con esta información en un 
# archivo de texto sin formato.
# La lista de empleado se encuentra en un archivo CSV.

filename = "employees.csv"
report_file = 'report.txt'

# Convertir los datos en un diccionario -------------------

# Devuelve un listado con llos empleados
def read_employees(csv_file_location):

    # Un dialecto configura algunos parámetros para parsear
    # el archivo csv
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

    # Si se omiten los nombre de los campos, se toma la 
    # primera fila como claves.
    employee_file = csv.DictReader(open(csv_file_location), dialect= 'empDialect')

    # En employee_file tenemos los empleados.
    # Iteramos sobre los registros para generar el diccionario.
    employee_list = []
    for data in employee_file:
        employee_list.append(data)

    return employee_list

# Devuelve un diccionario departamento:cantidad
def process_data(employees_list):

    # Se recorre la lista de empleados y se guardan únicamente 
    # los nombres, repetidos, de los departamentos.
    departament_list = []
    for employee_data in employee_list:
        departament_list.append(employee_data['departament'])

    # Ahora recorremos la lista repetida y creamos un conjunto
    # con los datos departamento:cantidad
    departament_data = {}
    for departament_name in set(departament_list):
        departament_data[departament_name] = departament_list.count(departament_name)

    return departament_data

# Generar el informe
# Escribir la lista departamento:cantidad en un archivo txt
def write_report(dictionay, report_file):

    with open(report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k) + ':' + str(dictionary[k])+ '\n')
        f.close

# ---------------------------------------------------------
# Obtener un listado de empleados a partir del csv
employee_list = read_employees(filename)

# Obtener los departamentos con el número de empleados
dictionary = process_data(employee_list)

# Escribir el informe
write_report(dictionary,report_file)



