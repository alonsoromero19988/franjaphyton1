## ejerciocio 1 
## Escribir un programa que pregunte el nombre por consola 
## y un numero entero a imprimir por pantalla el nombre 
##tantas veces como el numero que introdujo
numero1 = int(input("Ingrese el número de repeticiones del nombre:"))
print(numero1)
nombre1 = input("Ingrese el nombre:")
print(numero1 * nombre1)

## ejercicio 2
##Escribir un programa que muestre por pantalla el resultado
##De la siguiente operacion matematica

Valor_ecuacion = (( 3 + 2 )/( 2 * 5 ))**2 ## signo gatos es el de exponentes 
print(Valor_ecuacion)

## ejercicio 3
## Escribir un programa que lea un entero positivo n 
##introducido por el usuario y despues muestre por pantalla 
## la suma de todos los enteros desde 1 hasta n.
## la suma de los n enteros positivos puede ser calculada de la siguiente forma n*(n+1)/2

numero = int(input("ingrese un numero n entero positivo "))
if 0< numero :
    valor=str(numero*(numero+1)/2)
    print("el valor del 1 hasta n es:" + valor)  
else:
    print(" no se puede calcular")

