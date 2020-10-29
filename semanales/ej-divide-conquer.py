# Devuelve la suma de los elementos pares en la lista L de enteros.
def es_par(n):
  if n % 2 == 0:
    return True
  else:
    return False

def sumar_aux(L, desde, hasta):
    if desde >= hasta:
        result = 0                     # caso base O(1)
    elif desde == hasta - 1:
        if es_par(L[desde]):
          result = L[desde]            # caso base O(1)
        else:
          result = 0                   # O(1)
    else:
        # Divide
        medio = (desde + hasta) // 2   # O(1)
        # Conquer
        s1 = sumar_aux(L, desde, medio) # lista inferior: T(n/2)
        s2 = sumar_aux(L, medio, hasta) # lista superior: T(n/2)
        # Combine
        result = s1 + s2                # O(1)
    return result

def suma_pares(L):
  return sumar_aux(L, 0, len(L))


if __name__ == '__main__':
  print(suma_pares([1,2,4,5]))      # debe imprimir 6
  print(suma_pares([-1,2,-4,-5]))   # debe imprimir -2
  print(suma_pares([-1,-2,-4,-5]))  # debe imprimir -6
  print(suma_pares([]))             # debe imprimir 0

  '''
  Con el uso de inmersión de parametros evitamos la operación de slice L[i:j]
  Sea T(n) la cantidad de operaciones básicas que se ejecutan en función de una
  lista de entrada de tamaño n.
  T(n) = 2T(n/2) + O(1)
  ... = 4T(n/4) + O(1) + O(1)     esto se puede hacer log2(n) veces
  ... = 2^k*T(n/2^k)              se desprecian terminos constantes
  ... = n*T(1) => O(n) lineal
  '''
