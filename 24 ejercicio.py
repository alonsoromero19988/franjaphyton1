import random

def main():
    numero_aleatorio = random.randint(1, 10)
    nombre_fichero = "./archivos/tabla-" + str(numero_aleatorio) + ".txt"
    with open(nombre_fichero, "w", encoding="utf-8") as file:
        for i in range(1, 13):
            linea = str(i) + "X" + str(numero_aleatorio) + " = " + str(numero_aleatorio * i)

            file.write(linea)
            file.write("\n")

if __name__ == '__main__':
    main()