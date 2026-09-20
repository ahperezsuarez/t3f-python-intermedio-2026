def main():
    A={1,3,4,5,6}
    B={4,6,7,8,9}

    union=A|B
    interseccion=A&B
    conjunto_diferencia= A.symmetric_difference(B)
    subconjunto=A.issubset(B)
    cantidad_elementos_a=len(A)

    print("Union: ", *union)
    print("Interseccion: ", *interseccion)
    print("Conjunto de diferencia: ", conjunto_diferencia)
    print("Subconjunto: ", subconjunto)
    print("Cantidad de elementos en A: ", cantidad_elementos_a)

if __name__== '__main__':
    main()