def sumar(L):
    if len(L) == 0:
        result = 0
    elif len(L) == 1:
        result = L[0]
    else:
        # Divide
        medio = len(L) // 2
        # Conquer
        s1 = sumar(L[:medio]) # lista inferior
        s2 = sumar(L[medio:]) # lista superior
        # Combine
        result = s1 + s2
    return result

if __name__ == '__main__':
    lista = [1,1,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,1,1]
    print(sumar(lista))

    # Como operación de slice tiene orden O(k) y la operación se repite len(L) = N
    # Entonces este algoritmo divide&conquer tiene orden temporal O(N^2)