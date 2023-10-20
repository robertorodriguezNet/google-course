#!/usr/bin/env python3
import re

# # ---------------------------------------------------------
# # Cada registro tiene campos: nombre, teléfono y función.
# # El teléfono debe modificarse para añadir el +1 delante.
# def transform_record(record):
#     new_record = re.sub(r",([0-9-]*),",r",+1-\1,",record)
#     return new_record

# print(transform_record('Sabrina Green,802-867--5309,System Administrator'))
# print(transform_record('Eli Jones,684-3481127,IT specialist'))
# print(transform_record('Melody Daniels,846-687-7436,Programmer'))
# print(transform_record('Charlie Rivera,698-746-7436,Web Developer'))
# # Sabrina Green,+1 802-867--5309,System Administrator
# # Eli Jones,+1 684-3481127,IT specialist
# # Melody Daniels,+1 846-687-7436,Programmer
# # Charlie Rivera,+1 698-746-7436,Web Developer   

# # ---------------------------------------------------------
# # Devuelve todas las palabras con 3 o más vocales consecutivas.
# def multi_vowel_words(text):
#     pattern = r"\b\w*[aeiou]{3,}\w*\b"
#     result = re.findall(pattern,text)
#     return result

# print(multi_vowel_words('Life is beautifull'))
# print(multi_vowel_words('Obviously, the queen is courageous and gracious'))
# print(multi_vowel_words('The rambunctions children had to sit quietly and await their delicious dinner'))
# print(multi_vowel_words('The order of a data queue is First In First Out (FIFO)'))
# print(multi_vowel_words('Hello World!'))
# # ['beautifull']
# # ['Obviously', 'queen', 'courageous', 'gracious']
# # ['quietly', 'delicious']
# # ['queue']
# # []

# # ---------------------------------------------------------
# # Buscar texto que comience con # y reemplazarlo con //.
# def transform_comments(line_of_code):
#     result = re.sub(r"#{1,}","//",line_of_code)
#     return result

# print(transform_comments('### Start of program'))
# print(transform_comments(' number = 0 ## Initialize the variable'))
# print(transform_comments(' number += 1 # Incremetn the variable'))
# print(transform_comments(' return(number)'))
# # \/\/ Start of program
# #  number = 0 // Initialize the variable
# #  number += 1 // Incremetn the variable
# #  return(number)

# ---------------------------------------------------------
# Busca teléfonos con formato xxx-xxx-xxx y los tansforma en 
# (xxx) xxx-xxxx
def convert_phone_number(phone):
    result = re.sub(r" ([0-9]{3})-([0-9]{3})-([0-9]{3,4})",r" (\1) \2-\3",phone)
    return result

print(convert_phone_number('My numberj is 212-345-9999.'))
print(convert_phone_number('Please call 888-555-1234'))
print(convert_phone_number('123-123-12345'))
print(convert_phone_number('Phone number of Buckingham Palace is +44 303 123 7300'))