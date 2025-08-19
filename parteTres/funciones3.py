# Ejercicio uno

# def rectangulo(largo, ancho, caracter):
#     resultado = ""
#     for i in range(ancho): 
#         resultado += (f" {caracter} " *(largo)) + "\n"
#     return resultado

def rectangulo(largo, ancho, caracter):
    filas = []
    for i in range(ancho):
        fila = (f" {caracter} " * (largo))
        filas.append(fila)
    return "\n".join(filas)


# Ejercicio dos

def siEsBisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return f"El año {año} es bisiesto."
    else:
        return f"El año {año} no es bisiesto."



# Ejercicio tres

def cantidadAñoBisiesto(añoUno, añoDos):
    contador = 0
    inicio = min(añoUno, añoDos)
    fin = max(añoUno, añoDos)

    for año in range (inicio, fin):
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
            contador += 1
    return f"La cantidad de años bisiestos entre {añoUno} y {añoDos} es de {contador}"


# Ejercicio cuatro

def obtenerDescuento(valor, descuento):
    descuentoOperacion = (valor * descuento) / 100
    descuentoTotal = valor - descuentoOperacion
    return descuentoTotal

def obtenerIva(valorBase):
    return valorBase * 0.19 



# Ejercicio cinco

# def cantidadCaracteres(cadena):
#     contador = 0
#     for i in range(len(cadena)):
#         if contador % 2 == 0:
#             contador += 1
#         else:
#             contador += 1
#     return 



def cantidadCaracteres(cadena):

    cadenaSinEspacios = cadena.replace(" ", "")
    cantidad = len(cadenaSinEspacios)
    if cantidad % 2 == 0:
        paridad = "par"
    else:
        paridad = "impar"
    return f"La cadena tiene {cantidad} caracteres y es {paridad}"



# Ejercicio seis

def cantidadNumeros(cantidad):
    sumatoria = 0
    numeroAnterior = None

    for i in range(cantidad):
        if numeroAnterior is None:
            numero = int(input("Escriba un número: "))
        else:
            numero = int(input(f"Escriba un número distinto de {numeroAnterior}: "))
            while numero == numeroAnterior:
                print(f"¡{numero} no es distinto de {numeroAnterior}!")
                numero = int(input(f"Escriba un número distinto de {numeroAnterior}: "))
        
        sumatoria += numero
        numeroAnterior = numero

    print("Gracias por su colaboración.")
    return f"La sumatoria de todos los números es: {sumatoria}"



# Ejercicio siete

def determinarSiEsCorreo(cadena):
    if "@" in cadena and "." in cadena:
        return "La cadena es un correo electrónico."
    else:
        return "La cadena no es un correo electrónico."



# Ejercicio ocho

def cantidadCadenas(cantidadNumero):
    sumatoria = 0
    for i in range(cantidadNumero):
        cadena = input("Ingrese una cadena: ")
        cadenaSinEspacios = cadena.replace(" ", "")
        sumatoria += len(cadenaSinEspacios)
    return f"La suma de todas las longitudes de las cadenas es de {sumatoria}"




