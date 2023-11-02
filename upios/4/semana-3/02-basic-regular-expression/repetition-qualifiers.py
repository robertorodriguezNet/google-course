#!/usr/bin/env python3

import re

# * indica que . puede aparecer varias veces o ninguna
print(re.search(r"Py.*n", "Pygmalion")) # Pygmalion
print(re.search(r"Py.*n", "Python programning")) # Python programmin 
print(re.search(r"Py[a-z]*n", "Python programming")) # Python

# + una o más apariciones
# \? 0 o 1 aparición (la barra es de escape)
print(re.search(r"o+l+","goldfish")) # 'ol'
print(re.search(r"o+l+",'woolly')) # ooll
print(re.search(r"o+l+",'boil')) # ooll
print(re.search(r"p?each",'To each ther own')) # each