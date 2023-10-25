#!/usr/bin/env python3

import re

# Validar un nombre de variable para Pyton
pattern = r'^[a-zA-z_][a-zA-Z0-9_]*$'

print(re.search(pattern, '_nombre_valido'))
print(re.search(pattern,'0-no_válido'))