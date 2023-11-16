#!/bin/bash

# Los comandos pueden ir en una línea separador por ;


clear

line='---------------------------------------------------------------'

echo "Starting at: $(date)"

echo "Uptime"
Uptime
echo $line

echo "FREE"
free 
echo $line

echo "WHO"
who 
echo $line

echo "Finishisng at: $(date)"
echo $line
