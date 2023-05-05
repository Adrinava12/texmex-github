#!/usr/bin/python3



# Definir el nombre del fichero de recetas
nombre_fichero = "recetas.md"

# Comprueba si el fichero existe
try:
	# Abre el fichero y lee su contenido
	with open(nombre_fichero, "r") as fichero:
		contenido = fichero.read()
			
	# Imprime el contenido del archivo en la terminal
	print(contenido)
    
except FileNotFoundError:
	print(f"El fichero {nombre_fichero} no existe en el directorio actual.")




