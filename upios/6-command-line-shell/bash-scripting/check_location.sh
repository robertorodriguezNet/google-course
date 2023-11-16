#!/bin/bash

clear

# grep imprime las líneas que coinciden con la expresión dada
if grep "127.0.0.1" /etc/hosts; then
    echo "Everything ok"
else
    echo "ERROR! 127.0.0.1 is not in /etc/hosts"

# fi finaliza el bloque
fi


# Estas dos líneas hacen lo mismo
# -n comprueba si una cadena está vacía o no: true si no lo está
if test -n "$PATH"; then echo "Your path is not empty 1"; fi
if [ -n "$PATH" ]; then echo "Your path is not empty 2"; fi