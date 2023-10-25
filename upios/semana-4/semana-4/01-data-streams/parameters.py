#!/usr/bin/env python3

import sys

# Imprime el programa que ha sido llamad con sus argumentos
print(sys.argv) 

# roberto@ubuntu-vb:~/Documentos/google-course/upios/semana-4$ ./parameters.py
# ['./parameters.py']
# roberto@ubuntu-vb:~/Documentos/google-course/upios/semana-4$ ./parameters.py one two
# ['./parameters.py', 'one', 'two']
# roberto@ubuntu-vb:~/Documentos/google-course/upios/semana-4$ 

# Estados de salida
# 0: sin error

# El comando wc lee el número de líneas, palabras y caracteres de un archivo
# La variable $? devuelve el estado de la salida de la última ejecución
# roberto@ubuntu-vb:~/Documentos/google-course/upios/semana-4$ wc variables.py
#   6  16 169 variables.py
# roberto@ubuntu-vb:~/Documentos/google-course/upios/semana-4$ echo $?
# 0