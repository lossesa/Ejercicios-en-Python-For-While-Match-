# Ejercicio ocho

# Forma 1. Donde se crean las funciones dentro del menu. 
# Forma 2. Donde las funciones estan por fuera y simplemente se llaman. 

def menu(opcion):
    match opcion:
        case 1:
            def calcularDescuentoTotal(valor, porcentaje):
                descuento = (valor * porcentaje) / 100
                descuentoTotal = valor - descuento
                return f'Para un valor de {valor} y un porcentaje de {porcentaje} %, el descuento total es de {descuentoTotal}'
            
            v = int(input("Ingrese el valor: ").replace(".", ""))
            p = int(input("Ingrese el procentaje: "))
            return calcularDescuentoTotal(v,p)

        case 2:
            def devolverBooleano(cadena):
                if len(cadena) % 2 == 0:
                    return True
                else:
                    return False
            
            c = input("Ingrese la cadena: ")
            return devolverBooleano(c)
        
        case 3:
            def cadenaMasGrande(cadenaUno, cadenaDos):
                if len(cadenaUno) < len(cadenaDos):
                    return True
                elif len(cadenaUno) > len(cadenaDos):
                    return False
                else:
                    return 'Las dos cadenas son iguales en longitud.'
                
            c1 = input("Ingrese la cadena uno: ")
            c2 = input("Ingrese la cadena dos: ")
            return cadenaMasGrande(c1,c2)
                
        case 4:
            def sumaNumeroDeDosDigitos(numero):
                if numero >= 10 and numero <= 99:
                    divisionEntera = numero// 10
                    modulo = numero % 10
                    suma = divisionEntera + modulo
                    return f'La suma del digito es de {suma}'
                else:
                    return f'Ingresar un numero de dos digitos'
            
            n = int(input("Ingrese un número de dos digitos: "))
            return sumaNumeroDeDosDigitos(n)
        
        case 5:
            def validaciónUsuario(nombre, contraseña):
                nombreCorrecto = "CIAF"
                contraseñaCorrecta = "ciaf123"
                if nombre == nombreCorrecto and contraseña == contraseñaCorrecta:
                    return 'Usuario y contraseña correcta.'
                else:
                    return 'Acceso denegado'
            
            nombre = input("Ingrese su nombre: ")
            contra = input("Ingrese la contraseña: ")
            return validaciónUsuario(nombre, contra)

        case 6:
            def declaracionRenta(ingresoNetoMensual, edadUsuario):
                dineroAño = ingresoNetoMensual * 12
                if edadUsuario >= 18 and dineroAño > 50000000:
                    return f'Debe declarar renta.'
                else:
                    return f'No debe declarar renta.'
            
            inm = float(input("Ingrese su ingreso neto mensual: ").replace(".", ""))
            edad = int(input("Ingrese su edad: "))
            return declaracionRenta(inm, edad)

        case 7:
            def siEsMultiplo(numUno, numDos):
                if numUno > numDos:
                    if numUno % numDos == 0:
                        return f'{numUno} es multiplo de {numDos}'
                    else:
                        return f'{numUno} no es multiplo de {numDos}'
                elif numDos > numUno:
                    if numDos % numUno == 0:
                        return f'{numDos} es multiplo de {numUno}'
                    else:
                        return f'{numDos} no es multiplo de {numUno}'
                else:
                    return f'Ambos numeros son iguales'
            
            n1 = int(input("Ingrese el primer número: "))
            n2 = int(input("Ingrese el segundo número: "))
            return siEsMultiplo(n1,n2)
        
        case 8:
            def salir():
                return f'Haz salido del menú.'
            
            return salir()
        

