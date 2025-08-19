
from funciones3 import *

def menu(opcion):
    match opcion:
        case 1:
            largo = int(input("Ingrese el largo: "))
            ancho = int(input("Ingrese el ancho: "))
            caracter = input("Ingrese el caracter que desea: ")
            return rectangulo(largo, ancho, caracter)
        
        case 2:
            año = int(input("Ingrese el año: "))
            return siEsBisiesto(año)
        
        case 3:
            añoUno = int(input("Ingrese el primer año: "))
            añoDos = int(input("Ingrese el segundo año: "))
            return cantidadAñoBisiesto(añoUno, añoDos)
        
        case 4:
            valor = float(input("Ingrese el valor del producto: "))
            descuento = float(input("Ingrese el valor del descuento: "))

            valor1 = obtenerDescuento(valor, descuento)
            iva1 = obtenerIva(valor1)
            valorFinal1 = valor1 + iva1

            return f"El valor total con descuento e iva es de: {valorFinal1}"
        
        case 5:
            cadena = input("Ingrese una cadena de texto: ")
            return cantidadCaracteres(cadena)
        
        case 6:
            cantidad = int(input("¿Cuantos valores va a introducir? "))
            return cantidadNumeros(cantidad)

        case 7:
            cadena = input("Ingrese una cadena de texto: ")
            return determinarSiEsCorreo(cadena)

        case 8:
            cantidadNumero = int(input("Ingrese una cantidad: "))
            return cantidadCadenas(cantidadNumero)

        case 9:
            return "Haz salido del menú."
        
opcion = int(input('''----------------MENU----------------
                   1) Crear rectangulo.
                   2) Determinar si es bisieto.
                   3) Cantidad de años bisiestos.
                   4) Valor con descuento e iva.
                   5) Cantidad caracteres, par o impar.
                   6) Cantidad numero y sumatoria.
                   7) Determinar si es correo.
                   8) Suma de longitud de cadenas.
                   9) Salir del menú.'''))

print(menu(opcion))