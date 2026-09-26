"""
excepciones.py
Entrega de la segunda practica del curso Python Intermedio
Excepciones
"""

def main():
    """
    Funcion Principal
    """
    diccionario = {
        "llave":"valor"
    }

    division_x_cero(10,0)
    error_de_tipo(10,"hola")
    error_de_llave(diccionario)
    error_archivo_no_encontrado("archivo.txt")
    excepciones_zerodivisionerror_valueerror("hola",10)
    excepciones_zerodivisionerror_valueerror(10,0)

def division_x_cero(dividendo: int, divisor:int):
    try:
        resultado = dividendo/divisor
        return resultado
    except ZeroDivisionError:
        print ("1) ¡El dividendo no puede ser cero!")

def error_de_tipo(numero_1, numero_2):
    try:
        resultado = numero_1+numero_2
        return resultado
    except TypeError:
        print("2) ¡Error de tipo!")

def error_de_llave(diccionario):
    try:
        resultado = diccionario["llave_inexistente"]
        return resultado
    except KeyError:
        print("3) ¡Error de llave!")

def error_archivo_no_encontrado(archivo: str):
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            contenido=file.read()
            return contenido
    except FileNotFoundError:
        print("4) ¡No se encontro el archivo! sera creado.")
        with open(archivo, "w", encoding="utf-8") as file:
            file.write("Archivo creado")

def excepciones_zerodivisionerror_valueerror(numero_1 ,numero_2):
    try:
        resultado= int(numero_1)/int(numero_2)
        return resultado
    except ZeroDivisionError:
        print("5-1) ¡Error de division por cero!")
    except ValueError:
        print("5-2) ¡Error de valor!")
if __name__ == '__main__':
    main()
