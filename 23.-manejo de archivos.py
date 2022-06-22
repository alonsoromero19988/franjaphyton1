## manejo de archivos
## with: manejador contextual.si el programa se cierra inesperadamente 
## evita que se corrompa el archivo
## como se abren los archivos de python 
def leer ():
    numeros=[]
    with open('./archivos/numeros.txt', 'r') as file:  
        for linea in file:
            numeros.append( int(linea) )
    print(numeros)

def escribir ():
     pass

def main():
    leer()
if __name__ =='__main__':
   main()    



