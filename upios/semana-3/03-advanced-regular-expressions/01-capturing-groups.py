#!/usr/bin/env python3

import re

# Los Capturing Group son partes del patrón que están entre
# paréntesis.
result = re.search(r"^(\w*), (\w*)$","Lovelace, Ada")
print(result)