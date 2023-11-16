#!/bin/bash

for logfile in /var/log/*log; do
    echo "Processing: $logfile"

    # cut corta cada línea por ' ' y muestra a partir del campo 5 (field 5).
    # head -5 imprime las 5 primeras líneas de cada archivo.
    cut -d' ' -f5- $logfile | sort | uniq -c | sort -nr | head -5
done