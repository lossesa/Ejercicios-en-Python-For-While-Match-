
# Ejercicio uno

def tablaMultiplicarWHILE(numero,numFinal):
    resultado = ''
    contador = 0
    estado = True
    while estado:
        if contador == numFinal:
            estado = False
        else:
            contador = contador + 1
            multiplicacion = numero * contador
            resultado += f'{numero} x {contador} = {multiplicacion}\n'
    return resultado



# Ejercicio dos

def cantidadVocalesWhile(cadena):
    acum_a = 0
    acum_e = 0
    acum_i = 0
    acum_o = 0
    acum_u = 0

    iterador = 0
    resultado = ''
    while iterador < len(cadena):
        match cadena[iterador]:
            case 'a':
                   acum_a+=1
            case "e":
                acum_e+=1
            case "i":
                acum_i+=1
            case "o":
                acum_o+=1
            case "u":
                acum_u+=1
        iterador += 1
    
    resultado += f' Vocal a: {acum_a} \n Vocal e: {acum_e} \n Vocal i: {acum_i} \n Vocal o: {acum_o} \n Vocal u: {acum_u}'
    return resultado



# Ejercicio tres

def piramideWHILE(altura):
    resultado = []

    estado = True
    iterador = 0
    while estado:
        resultado.append("*"*(iterador))
        iterador = iterador + 1
        if iterador > altura:
           estado = False
    
    estado = True
    iterador = 0
    while estado:
        resultado.append("*"*(altura-iterador))
        iterador = iterador + 1
        if iterador > altura:
           estado = False

    return "\n".join(resultado)



# Ejercicio cuatro

def piramideNuevoEstiloWHILE(altura):
    resultado = []

    estado = True
    iterador = 0
    while estado:
        resultado.append(" "*(iterador) + " "*(altura-iterador) + " "*(altura-iterador) + "*"*(iterador) + "*"*(iterador-1))
        iterador = iterador + 1
        if iterador > altura:
            estado = False
    
    return "\n".join(resultado)


# Ejercicio cinco

def serieFibonacciWHILE(n):
    a = 0
    b = 0

    iterador = 0
    estado = True
    while estado:
        iterador = iterador + 1
        print(a, end= " ")
        temporal = a
        a = b
        b = temporal + b
        if iterador > n:
            estado = False
    

