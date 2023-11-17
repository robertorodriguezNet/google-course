#!/bin/bash

clear

# Crear el archivo olFiles.txt en el que 
# guardar los archivos con jane.
> oldFiles.txt

# Buscamos el data/list.txt las lineas que
# contengan jane y guardamos los nombres 
# de los archivos en una variable "files"


grep " jane " ../data/list.txt | cut -d ' ' -f 3 

