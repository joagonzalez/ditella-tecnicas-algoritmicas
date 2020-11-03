def factorial(n):
    rv = 1
    i = n
    while i > 0:
        rv = rv * i
        i -= 1
    return rv

def factoriales(n):
    rv = []
    i = 1
    while i <= n:
        rv.append(factorial(i))
        i += 1
    return rv

def factoriales_lineal(n):
    '''
    Se van agregando los factoriales calculados multiplicando el factorial anterior
    Esto hace que sea un algoritmo lineal O(N)
    '''
    rv = []

    for i in range(n+1):
        if i == 0:
            continue
        elif i == 1:
            rv.append(1)
        else:
            rv.append( i * rv[i-2]) # se desfasa por el continue el indice de la lista respecto de i
    return rv

if __name__ == '__main__':
    FACTORIAL = 6
    print(factoriales(FACTORIAL))
    print(factoriales_lineal(FACTORIAL))