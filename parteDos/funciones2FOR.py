# Ejercicio uno

def tablaMultiplicarFOR(numero, numFinal):
    resultado = ''
    for i in range(1,numFinal+1):
        multiplicacion = numero * i
        resultado += f'{numero} x {i} = {multiplicacion}\n'
    return resultado


# Ejercicio dos

def cantidadVocalesFOR(cadena):
    contadorA = 0
    contadorE = 0
    contadorI = 0
    contadorO = 0
    contadorU = 0

    resultado = ''
    for iterador in cadena:
        if iterador in "aeiouAEIOU":
            if iterador == "a":
                contadorA += 1
            elif iterador == "e":
                contadorE += 1
            elif iterador == "i":
                contadorI += 1
            elif iterador == "o":
                contadorO += 1
            elif iterador == "u":
                contadorU += 1
    resultado += f' Vocal a: {contadorA}\n Vocal e: {contadorE}\n Vocal i: {contadorI}\n Vocal o: {contadorO}\n Vocal u: {contadorU}\n'
    return resultado


# Ejercicio tres

def piramideFOR(altura):
    resultado = []
    for i in range(1, altura):
        resultado.append("*" * i)
    for i in range(altura):
        resultado.append("*" * (altura - i))
    return "\n".join(resultado)



# Ejercicio cuatro

def piramideNuevoEstiloFOR(altura):
    resultado = []
    for i in range(1,altura+1):
        resultado.append(" "*(i) + " "*(altura-i) + " "*(altura-i) + "*"*(i) + "*"*(i-1))
    return "\n".join(resultado)


# Ejercicio cinco

def serieFibonacciFOR(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        temporal = a
        a = b
        b = temporal + b


# Ejercicio seis

def determinarNumPrimosFOR(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True



