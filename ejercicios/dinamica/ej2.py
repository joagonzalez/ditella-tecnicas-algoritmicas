import time

def cant_sumas_distintas_exp(n):
    if n == 1:
        rv = 1
    # hay 1 forma de escribir 1: (1)
    elif n == 2:
        rv = 1
    # hay 1 forma de escribir 2: (1+1)
    elif n == 3:
        rv = 2
    # hay 2 formas de escribir 3: (1+1+1),(3)
    elif n == 4:
        rv = 4
    # hay 4 formas de escribir 4: (1+1+1+1),(1+3),(3+1),(4)
    else:
        rv = cant_sumas_distintas_exp(n-1) + \
             cant_sumas_distintas_exp(n-3) + \
             cant_sumas_distintas_exp(n-4)
    return rv

def cant_sumas_distintas_lineal(n, buffer):
    # guardamos resultados en un diccionario
    if n == 1:
        rv = 1
    # hay 1 forma de escribir 1: (1)
    elif n == 2:
        rv = 1
    # hay 1 forma de escribir 2: (1+1)
    elif n == 3:
        rv = 2
    # hay 2 formas de escribir 3: (1+1+1),(3)
    elif n == 4:
        rv = 4
    # hay 4 formas de escribir 4: (1+1+1+1),(1+3),(3+1),(4)
    elif n in buffer:           # si el resultado esta en el buffer, lo obtenemos de ahí
        # print('encontrado!')
        rv = buffer[n]
    else:
        rv = cant_sumas_distintas_lineal(n-1, buffer) + \
             cant_sumas_distintas_lineal(n-3, buffer) + \
             cant_sumas_distintas_lineal(n-4, buffer)
        buffer[n] = rv
    # print('imprimimos buffer: ' + str(buffer))
    return rv

if __name__ == '__main__':
    ITERS = [30, 35, 40]
    buffer = {}

    for i in ITERS:
        print("Comparamos para N = " + str(i))
        start_time = time.time()
        print('exponencial: ' + str(cant_sumas_distintas_exp(i)))
        print("--- %s seconds ---" % (time.time() - start_time))

        start_time = time.time()
        print('lineal: ' + str(cant_sumas_distintas_lineal(i, buffer)))
        print("--- %s seconds ---" % (time.time() - start_time))

    ''' A)
    Este algoritmo funciona ya que descompone al numero en casos base.
    Los casos base, a su vez, estan bien definidos y se define de cuantas maneras puede escribirse cada uno como sumas de 1, 3 y 4
    Entonces, el numero solicitado se podrá escribir de tantas formas como la suma de todos los casos base en que se pudo descomponer.

    Es exponencial, ya que tomando de ejemplo n = 5

    rv = cant_sumas_distintas_exp(n-1) +          # AQUI SE CALCULA PARA 4 = caso base
             cant_sumas_distintas_exp(n-3) +      # AQUI SE CALCULA PARA 2 = caso base
             cant_sumas_distintas_exp(n-4)        # AQUI SE CALCULA PARA 1 = caso base

    Es exponencial, ya que tomando de ejemplo n = 6

    rv = cant_sumas_distintas_exp(n-1) +          # AQUI SE CALCULA PARA 5 = se realiza lo que para 5 
             cant_sumas_distintas_exp(n-3) +      # AQUI SE CALCULA PARA 3 = caso base
             cant_sumas_distintas_exp(n-4)        # AQUI SE CALCULA PARA 2 = caso base

    Es exponencial, ya que tomando de ejemplo n = 7

    rv = cant_sumas_distintas_exp(n-1) +          # AQUI SE CALCULA PARA 6 = se realiza lo que para 6 ( + 5)
             cant_sumas_distintas_exp(n-3) +      # AQUI SE CALCULA PARA 4 = caso base
             cant_sumas_distintas_exp(n-4)        # AQUI SE CALCULA PARA 3 = caso base

    Es exponencial, ya que tomando de ejemplo n = 8

    rv = cant_sumas_distintas_exp(n-1) +          # AQUI SE CALCULA PARA 7 = se realiza lo que para 7 ( + 6 + 5)
             cant_sumas_distintas_exp(n-3) +      # AQUI SE CALCULA PARA 5 = se realiza lo que para 5
             cant_sumas_distintas_exp(n-4)        # AQUI SE CALCULA PARA 4 = caso base
    
    Se puede observar que pueden descomponerse los calculos en un arbol de manera similar a como lo haciamos con la funcion recursiva de fibonacci
    No se aprovechan los resultados ya calculados y vuelven a desarrollarse, lo que hace que crezca de manera exponencial
    '''

    ''' C)
    Estas diferencias se deben a que mientras mayor es el valor de N, mas veces se reciclarán valores
    del buffer definido y, a su vez, mayor será la profundidad del árbol para calcular el valor deseado.
    Entonces, la diferencia de tiempo entre las funciones exponencial y lineal irá creciendo junto con el valor de N
    '''