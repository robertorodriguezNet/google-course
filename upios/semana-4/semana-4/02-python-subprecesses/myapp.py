import os
import subprocess

# Copiamos el diccionario con las variables de 
# entorno del SO
my_env = os.environ.copy()

# Ahora podemos modificar el entorno sin modificar el original

# Agregamos un directorio adicional 
my_env['PATH'] = os.pathsep.join(['/opt/myapp/', my_env['PATH']])

# LLamamos al comando myapp buscando la ruta en el entorno que
# hemos creado
result = subprocess.run(['myapp'], env=my_env)