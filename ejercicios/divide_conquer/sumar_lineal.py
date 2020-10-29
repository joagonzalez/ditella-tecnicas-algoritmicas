def sumar_aux(L, desde, hasta):
    if desde >= hasta:
        result = 0                     # caso base
    elif desde == hasta - 1:
        result = L[desde]              # caso base
    else:
        # Divide
        medio = (desde + hasta) // 2
        # Conquer
        s1 = sumar_aux(L, desde, medio) # lista inferior
        s2 = sumar_aux(L, medio, hasta) # lista superior
        # Combine
        result = s1 + s2
    return result

def sumar(L):
    return sumar_aux(L, 0, len(L))

if __name__ == '__main__':
    lista = [1,1,0,0,0,1,0,1,1,0,1,0,0,0,0,0,0,1,1]
    print(sumar(lista))

    # en este caso usamos inmersion de parametros 
    # para no hacer slice de la lista y bajar complejidad temporal