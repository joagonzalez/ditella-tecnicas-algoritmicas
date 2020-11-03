
def cant_pos_con_suma_ant(l):               # O(len(l)^2)
    res, i = 0, 0
    while i < len(l):                       # O(len(l))
        suma_ant, j = 0, 0                  # O(1)
        while j < i:                        # O(len(l)-1) acotando superiormente en el ultimo caso
            suma_ant = suma_ant + l[j]      # O(1)
            j = j + 1                       # O(1)
        if suma_ant == l[i]:                # O(1)
            res = res + 1                   # O(1)
        i = i + 1                           # O(1)
    return res

def cant_pos_con_suma_ant_lineal(l):         # O(len(l))            
    res, i = 0, 0
    buffer = [0]                             # guarda suma de valores de l[0] hasta l[i-1] en la posicion i

    while i < len(l):                        # O(len(l)), lo de adentro, todo O() constante
        suma_ant, j = 0, 0  
        if i != 0:    
            buffer.append(l[i-1] + buffer[i-1])                    
        if buffer[i] == l[i]:                
            res = res + 1                   
        i = i + 1                           
    return res

if __name__ == '__main__':
    lista = [1,1,2,3,7,0,14,28]
    res = cant_pos_con_suma_ant(lista)
    print('cuadratica: ' + str(res))

    res = cant_pos_con_suma_ant_lineal(lista)
    print('lineal: ' + str(res))
