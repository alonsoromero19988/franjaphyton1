## modulo random
## (import random as rd ) puede ser tambi
import random
 
def main():

    numero_aleatorio = random.randint(1, 100)  ## escojer un numero entero entre 1 y 100 que es el rango que dimos
    print(numero_aleatorio)

    lista_numeros= [1, 2, 3, 4, 5, 6, 7]
    numero_aleatorio=random.choice(lista_numeros)  ## escojer un elemento de la lista de manera aleatoria
    print(numero_aleatorio)

if __name__ == '__main__':
    main()