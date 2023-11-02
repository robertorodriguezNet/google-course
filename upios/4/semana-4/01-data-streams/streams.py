#!/usr/bin/env python3

data = input("This will come from STDIN: ")
print("Now we write it to STDOUT: " + data)
print("Now we generate an error to STDERR: " + data + 1)
# This will come from STDIN: cadena de texto
# Now we write it to STDOUT: cadena de texto
# Traceback (most recent call last):
#   File "/home/roberto/Documentos/google-course/upios/semana-4/streams.py", line 5, in <module>
#     print("Now we generate an error to STDERR: " + data + 1)
# TypeError: can only concatenate str (not "int") to str