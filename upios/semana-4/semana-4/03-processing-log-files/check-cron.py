#!/usr/bin/env python3

import sys
import re

# Script que lee las líneas de un archivo de texto
# recibido como parámetro por consola.

pattern = r'USER \((\w+)\)$'
usernames = {}

logfile = sys.argv[1]
with open(logfile) as file:
    for line in file:
        if 'CRON' not in line:
            continue
        result = re.search(pattern,line)
        if result is None:
            continue
        usernames[result[1]] = usernames.get(result[1], 0) +1

print(usernames) # {'good_user': 1, 'naughty_user': 3}
        