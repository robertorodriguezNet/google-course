#!/usr/bin/env python3

# Este script provoca la salida con un código entre 0 y 3,
# lo que simulará que es una aplicación que falla (o no).

# Comando que debemos ejecutar: ./retry.sh ./random-exit.py

import sys
import random

value=random.randint(0,3)
print("Returning: " + str(value))
sys.exit(value)