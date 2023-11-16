#!/bin/bash

clear

n=1

# -le equivale a < (supongo que le es una abreviatura de less)
while [ $n -le 5 ]; do
    echo "Iteration number $n"

# El doble paréntesis permite hacer operaciones aritméticas con las variables
    ((n+=1))
done