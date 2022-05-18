# cadena de caracteres 

nombre = input("¿Cual es su nombre?  ")
# nombre = nombre.upper()     ## llevara el nombre a mayusculas siempre hay que asociarlo a una variable
# print(nombre)

# nombre = nombre.capitalize()
# print(nombre)

# nombre = nombre.strip() ## Quita los ultimos espacios que tenga mi cadena de texto
# print(nombre)
 
# nombre = nombre.lower()
# print(nombre)

nombre = nombre.replace('e', '')
print(nombre)

print( nombre[0] )

letra = nombre[2]
print(letra)

largo_cadena = len(nombre)
print(largo_cadena)

largo_texto = len("Franja")
print(largo_texto)

cadena_texto = "Franja   "
cadena_texto = cadena_texto.strip()
print(len(cadena_texto))