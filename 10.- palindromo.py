## palindromo 
# Escribir un programa que  identifique 
# si una palabra es palindromo o no
# Luz azul 
# Ana
# Anita lava la tina 
# yo hago yoga hoy 

def palindromo(palabra):
    palabra = palabra.replace(' ', '')
    palabra = palabra.lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else :
        return False    

## funcion principal main/run
def main():
    palabra = input("ingrese una frase: ")
    es_palindromo = palindromo(palabra)
    if es_palindromo:
        print(" Es palindromo ")
    else:
        print(" No es palindromo")    

## punto de entrada 
## buena practica 
if __name__ == "__main__":
    main()

