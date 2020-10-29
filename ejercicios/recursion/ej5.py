def cantidad_ocurrencias(lista, n, desde): # O(n)
    if desde >= len(lista):
        return 0
    else:
        if lista[desde] == n:
            return 1 + cantidad_ocurrencias(lista, n, desde+1) # O(1)
        else:
            return cantidad_ocurrencias(lista, n, desde+1)

def cantidad_ocurrencias_aux(lista, n):
    return cantidad_ocurrencias(lista, n, 0)

if __name__ == '__main__':
    print(cantidad_ocurrencias_aux([0,1,1,1,2,3,4,0,7,6,2,3,1], 1))
    print(cantidad_ocurrencias_aux([0,1,1,1,2,3,4,0,7,6,2,3,1], 0))
    print(cantidad_ocurrencias_aux([0,1,1,1,2,3,4,0,7,6,2,3,1], 3))

