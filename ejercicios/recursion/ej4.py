def productoria(lista, desde): # O(n)
    if desde >= len(lista):
        result = 1
    else:
        result = lista[desde] * productoria(lista, desde+1) # O(1)
    return result

def productoria_aux(lista):
    return productoria(lista, 0)

if __name__ == '__main__':
    print(productoria_aux([0]))
    print(productoria_aux([2, 3, 4]))
    print(productoria_aux([1, 2, 3]))