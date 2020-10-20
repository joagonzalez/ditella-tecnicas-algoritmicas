# Devuelve la cantidad de veces que 0 está en la lista L.
def cant_0_aux(L, desde):
    if desde >= len(L):
        return 0
    else:
        if L[desde] == 0:
            return 1 + cant_0_aux(L, desde+1) # se ejecuta n-veces instrucciones de O(1)
        else:
            return cant_0_aux(L, desde+1) # O(1) si no encuentra entonces avanza

def cant_0(L):
    return cant_0_aux(L, 0)

print(cant_0([3, 0, 1, 0]))     # debe imprimir 2
print(cant_0([0, 0, 0]))        # debe imprimir 3
print(cant_0([30, -4, 10, 5]))  # debe imprimir 0
print(cant_0([]))               # debe imprimir 0

# Explicación:
# cant_0_aux tiene todas instrucciones de orden O(1), no hay slicing ya que se usa inmersion de parámetros
