#!/usr/bin/env python3

import sys

# Se toma cada línea de entrada estándar, se limpia y 
# se divide en palabras por los espacios en blanco.
# Luego se usa una lista de comprensión, se capitaliza
# cada palabra y se termina por unirlas.
for line in sys.stdin:
    words = line.strip().split()
    print(" ".join([word.capitalize() for word in words]))

# Uso del script mediante pipe.
# cat story.txt | capitalize_words.py