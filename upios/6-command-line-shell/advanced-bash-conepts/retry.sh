#!/bin/bash

# Comando que debemos ejecutar: ./retry.sh ./random-exit.py

clear

n=0

# $1 es el primer argumento de la línea de comando
# En python se obtiene usando sys.argv[1]
command=$1
while ! $command && [ $n -le 5 ]; do
    sleep $n
    ((n=n+1))
    echo "Retry #$n"
done;