
from funciones2FOR import *

# Menu 

def menu(opcion):

    match opcion:
        case 1:
            numUsuario = int(input("Ingrese el número a multiplicar: "))
            numFinalUSuario = int(input("Ingrese hasta donde desea multiplicar: "))
            return tablaMultiplicarFOR(numUsuario, numFinalUSuario)
        
        case 2:
            cadenaUsuario = input("Ingrese una cadena de tetxo: ")
            return cantidadVocalesFOR(cadenaUsuario)
        
        case 3:
            alturaUsuario = int(input("Ingrese la altura de la piramide: "))
            return piramideFOR(alturaUsuario)
        
        case 4:
            alturaUsuario = int(input("Ingrese la altura de la piramide: "))
            return piramideNuevoEstiloFOR(alturaUsuario)
        
        case 5:
            nUsuario = int(input("Ingrese una cantidad de número para la serie: "))
            return serieFibonacciFOR(nUsuario)
        
        case 6:
          pass
        
        case 7:
            return 'Haz salido del menú.'
        

opcion = int(input('''------- MENU -------
                   1) Tabla de multiplicar.
                   2) Hallar vocales cadena. 
                   3) Piramide estilo 1.
                   $) Piramide estilo 2.
                   5) Serie de fibonacci.
                   6) Numero primos de 0 a 100.
                   7) Salir. '''))

print(menu(opcion))
