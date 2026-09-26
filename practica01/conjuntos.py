"""
Modulo para el la entrega del la Practica 1
"""
def main():
    """
    Funcion principal realiza operaciones con conjuntos
    """
    conjunto_a = {1, 3, 4, 5, 6}
    conjunto_b = {4, 6, 7, 8, 9}

    union = conjunto_a | conjunto_b
    interseccion = conjunto_a & conjunto_b
    conjunto_diferencia = conjunto_a.symmetric_difference(conjunto_b)
    subconjunto = conjunto_a.issubset(conjunto_b)
    cantidad_elementos_a = len(conjunto_a)

    print("Unión: ", *union)
    print("Intersección: ", *interseccion)
    print("Conjunto de diferencia: ", conjunto_diferencia)
    print("Subconjunto: ", subconjunto)
    print("Cantidad de elementos en conjunto_a: ", cantidad_elementos_a)

if __name__ == '__main__':
    main()
