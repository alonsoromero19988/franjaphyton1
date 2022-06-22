def main():
    edad = int(input("Ingrese su edad: "))
    if edad < 4:
        precio = 0
    elif edad <= 18:
        precio = 3500
    else:
        precio = 8000
    
    print("El precio de la entrada es: " + str(precio))
    

if __name__ == '__main__':
    main()