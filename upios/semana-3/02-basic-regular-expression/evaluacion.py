#!/usr/bin/env python3

import re

# ---------------------------------------------------------
# The check_web_adresse function checks if the text passed
# qualifies as a top-level web address, meaning that it con-
# tains alphanumeric character, as well as periods,dashes, 
# and a plus sign, followed by a period and a character-only
# top-level domain.
# def check_web_addresse(text):
#     pattern = '^[a-zA-Z0-9.\-_]*\.[a-zA-Z]*$'
#     result = re.search(pattern,text)
#     return result != None

# print(check_web_addresse('gmail.com')) # True
# print(check_web_addresse('www@google')) # False
# print(check_web_addresse('www.Coursera.com')) # True
# print(check_web_addresse('web-address.com/homepage')) # False
# print(check_web_addresse('My_favorite-Blog.US')) # True

# ---------------------------------------------------------
# Verifica:
# El formato de la hora es de 12 horas
# La hora está entre 1 y 12, sin 0 a la izquierda.
# El separador es ":"
# Los minutos están entre 00 y 59
# am/pm es opcional y valen mayúsculas
# def check_time(text):
#     pattern = r'^[1-9][012]?:[012345][0-9][ amAMpmPM]'
#     result = re.search(pattern,text)
#     return result != None

# print(check_time('12:45pm')) # True
# print(check_time('9:59 AM')) # True
# print(check_time('6:60am')) # False
# print(check_time('five o clock')) # False

# ---------------------------------------------------------
# Verifica:
# El texto contiene 2 o más caracteres enter paréntesis.
# El primer carácter debe ser mayúscula.
# def contains_acronym(text):
#     pattern = r'.*\([A-Z0-9]\w*\).*'
#     resutl = re.search(pattern,text)
#     return resutl != None

# print(contains_acronym('Instant messaging (IM) is a set')) # True
# print(contains_acronym('American standard Code (ASCII) is a')) # True
# print(contains_acronym('Please do NOT enter!!!')) # False
# print(contains_acronym('PostScript isa fourth-generation (4GL)')) # True
# print(contains_acronym('Have fun using (Scuba)')) # True

# ---------------------------------------------------------
# Verifica:
# El texto incluye el CP de USA.
# 5 dígitos simpre seguido de (opcional) un guión y 5 dígitos.
# El código debe ir precedido de un espacion y no estar al inicio.
def check_zip_code(text):
    pattern = r'^.* [0-9]{5}(-[0-9]{4})?'
    result = re.search(pattern,text)
    return result != None

print(check_zip_code('The zip codes for NY are 10001 thru 11104.')) # True
print(check_zip_code('90210 is a TV show')) # False
print(check_zip_code('Their address is: 123 Main Street, AZ 85258')) # True
print(check_zip_code('The Parliament of Canada is on KA1A0A9')) # False