#!/bin/bash

clear

# Iterar sobre todos los archivos que terminen en .HTM
# basename contiene "file" sin la extensión que para como 
# segundo argumento.
# $ se usa para llamar al comando.
# file está entrecomillado para que se respenten los espacios
# en blanco si los hubiera.
for file in archivos/*.HTM; do
    name=$(basename "$file" .HTM)
    mv "$file" "$name.html"
done;