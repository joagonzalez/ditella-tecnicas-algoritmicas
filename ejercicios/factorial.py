def factorial(n):               # O(n)
    res = 1
    for i in range(n):
        i = i+1
        res = res * i
    return res

def factorial_recursivo(n):
    if n > 0:
        return n * factorial_recursivo(n-1)
    elif n == 0:
        return 1
    else:
        return -1 # invalid parameter

def sumatoria_recursivo(n):
    if n > 0:
        return n + sumatoria_recursivo(n-1)
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return -1

def suma_lista_recursiva(lista):
    if len(lista) != 0:
        return lista[0] + suma_lista_recursiva(lista[1:])
    else:
        return 0

def maximo(lista):
    if len(lista) > 1:
        if lista[0] > maximo(lista[1:]):
            return lista[0]
        else:
            return maximo(lista[1:])
    elif len(lista) == 1:
        return lista[0]
    else:
        return 0

if __name__ == '__main__':
    print(factorial(5))
    print(factorial(3))
    print(factorial(0))
    print('recursivo')
    print(factorial_recursivo(5))
    print(factorial_recursivo(3))
    print(factorial_recursivo(0))
    print('sumatoria positivos recursiva')
    print(sumatoria_recursivo(5))
    print(sumatoria_recursivo(3))
    print(sumatoria_recursivo(0))
    print('sumatoria lista recursiva')
    print(suma_lista_recursiva([1,2,3]))
    print(suma_lista_recursiva([145,2,3]))
    print(suma_lista_recursiva([1,2,6]))
    print('maximo recursivo')
    print(maximo([100, 1, 2, 6, 8]))