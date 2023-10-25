#!/usr/bin/env python3

import re

# result = re.split(r"[.?!]","One sentence. Another one? And last one!")
# print(result) # ['One sentence', ' Another one', ' And last one', '']

# Catura los puntos de ruptura
# result = re.split(r"([.?!])","One sentence. Another one? And last one!")
# print(result) # ['One sentence', '.', ' Another one', '?', ' And last one', '!', '']

result = re.split(r"the|a", "One sentence. Another one? And last one!")
print(result)

# Sustituye la cadena buscada por la cadena pasada
# result = re.sub(r"[\w.%+-]+@[\w.-]+", "[REDACTED]", "Recivied an email for go_nuts95@my.example.com")
# print(result) # Recivied an email for [REDACTED]

# En la cadena de sustitución se usa la barra invertida para indicar el grupo
# result = re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada")
# print(result) # Ada Lovelace