"""
ternariasyargs.py
Entrega de la tercera practica del curso Python Intermedio
Evaluaciones ternarias, args y kwargs
"""

def main():
    try:
        print(calcular_mayor())
        print(buscar_palabra("auto","rojo","mio"))
        print(es_par())
        print(calcular_promedio(3,2,5))
        print(error_de_argumento())
    except TypeError:
        print("5) Capturar error al no ingresar suficientes argumentos: \n ERROR no se envio al menos un argumento")



def calcular_mayor():
    print("1) Calcular mayor")
    try:
        numero_1 = float(input("Ingresar el primer numero:  "))
        numero_2 = float(input("Ingresar el segundo numero: "))

        resultado = "Los valores son iguales \n" if numero_1 == numero_2 else (f"El primer valor es mayor: {numero_1} \n" if numero_1 > numero_2 else f"El segundo valor es mayor: {numero_2}\n")
        return resultado
    except ValueError:
        return "ERROR: solo se pueden ingresar numeros \n"

def buscar_palabra(*args):
    print("2) Buscar palabra: ")

    palabra = input("Ingresar palabra: ")
    resultado= "Palabra encontrada.\n" if palabra in args else "Palabra no encontrada.\n"

    return resultado


def es_par():
    print("3) ¿Es par?")
    try:
        numero = float(input("Ingrese un numero: "))
        resultado = "El numero es par.\n" if numero % 2 == 0 else "El numero es impar\n "
        return resultado
    except ValueError:
        return "ERROR: solo se pueden ingresar numeros \n"


def calcular_promedio(*args):
    print("4) Calcular promedio: ")
    try:
        total=0
        for arg in args:
            total += arg
        resultado = f"El promedio es: {float(total/len(args))}\n"
        return resultado
    except ValueError:
        return "ERROR: solo se pueden evaluar numeros.\n"
    except ZeroDivisionError:
        return "ERROR: no se enviaron numeros para evaluar.\n"


def error_de_argumento(arg, *args):
    print("5) Capturar error al no ingresar suficientes argumentos:")
    resultado = f"El argumento mandatorio es {arg} y los opcionales son {args}. \n"
    return resultado


if __name__ == '__main__':
    main()
