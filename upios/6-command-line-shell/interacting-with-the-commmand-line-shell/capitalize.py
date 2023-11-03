#!/usr/bin/env python3 
import sys

# Recorrer la entrada que recibamos del sistema.
# strip() limpia el carcter de nueva línea del final.
for line in sys.stdin:
    print(line.strip().capitalize())

# Para capitalizar el texto del archivo haiku.txt: 
# pipe: cat haiky.txt | ./capitalize.py
# redirección: ./capitalize.py < haiku.txt