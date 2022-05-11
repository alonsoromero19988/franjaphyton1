def suma(a,  b):
    resultado = a + b 
    return resultado ## sirve para cuando quiero que me devuelva un resultado

def resta(a, b):
    resultado = a - b 
    return resultado 

def division(a, b):
    resultado = a / b 
    return resultado 

def multiplicacion(a, b):
    resultado = a * b 
    return resultado 

print("""1 para suma
2 para restar
3 para division 
4 para multiplicacion""")
opcion = int(input("seleccione una opcion"))
numero_1=int(input("ingrese numero 1: "))
numero_2=int(input("ingrese numero 2: "))

if opcion == 1:
    res=suma(numero_1, numero_2)
    print("la suma es: "+ str(res))

elif opcion ==2:
    res= resta(numero_1, numero_2)
    print("La resta es: " + str(res))
elif opcion == 3:
    res= division(numero_1, numero_2)
    print("La division es: " + str(res))

    
elif opcion == 4:
    res= multiplicacion(numero_1, numero_2)
    print("La multiplicacion es: " + str(res))
else:
    print("opcion no valida")
