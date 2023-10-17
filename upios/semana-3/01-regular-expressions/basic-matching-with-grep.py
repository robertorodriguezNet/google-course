#!/usr/bin/env python3

# grep se usa para aplicar expresiones regulares en línea de comandos.
# grep imprime cualquier línea que coincida con la
# consulta pasada.

# Buscar las palabras que contengan 'tal' en el archivo word.txt.
# Para no case: grep -i
# grep tal words.txt
# grep -i tal words.txt

# Comodín: el punto . es el comodín
# grep -i t.l words.txt

# ^ comienzo de la línea: no debe haber nada antes.
# $ final de la línea: no debe haber nada después.

# grep ^t.l words.txt
# grep t.l$ words.txt



