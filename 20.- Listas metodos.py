## Listas metodos
from pickle import TRUE


def main():
    numeros =[1,3,5,7,8,9,0]
    print (type(numeros))
    print(numeros[0])

    objetos=['hola', 2, 4.5, True]
    print(objetos)

## agregar elementos 
    objetos.append(False)
    objetos.append(45)
    objetos.append("Hola mundo")
    print( objetos )

## Eliminar elementos
    objetos.pop(0)     ### Elimina en donde esta la posicion 0  
    objetos.pop()     ## elimina el ultimo dato
    print(objetos)

### recorrer lista

    for objeto in objetos:
        print(objeto)

## ordena lista
    
    print(objetos[::-1])

##sumar lista 
    numeros_1 = [1,2,3]
    numeros_2 = [4,5,6]
    lista_final = numeros_1 + numeros_2
    print(lista_final)

##multiplicar lista
    print(numeros_1*3)
 

if __name__== '__main__':
    main()