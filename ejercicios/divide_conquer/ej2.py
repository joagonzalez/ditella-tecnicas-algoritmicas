# Técnicas Algorítmicas - Clase 2 - Resolución de ejercicios

###############################################################
# 1. Escribir una función 'maximo' con la técnica dividir y
#    conquistar que, dada una lista no vacía de números,
#    devuelva el número máximo.
def maximo(L):
    return maux(L, 0, len(L))

def maux(L, desde, hasta):
    if desde == hasta - 1:  # caso base
        res = L[desde]
    else:                   # caso recursivo
        # dividir
        medio = (desde + hasta) // 2
        # conquistar
        m1 = maux(L, desde, medio)
        m2 = maux(L, medio, hasta)
        # combinar    
        if m1 > m2:
            res = m1
        else:
            res = m2
    return res

def maximo_pos(L):
    return maux_pos(L, 0, len(L))

def maux_pos(L, desde, hasta):
    if desde == hasta - 1:  # caso base
        res = desde
    else:                   # caso recursivo
        # dividir
        medio = (desde + hasta) // 2
        # conquistar
        m1 = maux_pos(L, desde, medio)
        m2 = maux_pos(L, medio, hasta)
        # combinar    
        if L[m1] >= L[m2]:
            res = m1
        else:
            res = m2
    return res

###############################################################
# 2. Implementar Mergesort

# Dada una lista L, la ordena en el lugar (o sea, la modifica),
# con el algoritmo recursivo d&c "merge sort", que es O(n log n).
def mergesort(L):
  return mergesort_aux(L, 0, len(L))

def mergesort_aux(L, desde, hasta):
  if desde +1 >= hasta:
    pass
  else:
    medio = (desde + hasta) // 2
    mergesort_aux(L, desde, medio)
    mergesort_aux(L, medio, hasta)
    AUX = merge(L[desde:medio], L[medio:hasta])
    for i in range(len(AUX)):
      L[desde+i] = AUX[i]

# Dadas dos listas ordenadas (en forma creciente) L1 y L2,
# devuelve una nueva lista con los elementos de ambas ordenados.
def merge(L1, L2):
  i,j = 0,0
  RES = []
  while i<len(L1) and j<len(L2):
    if L1[i] < L2[j]:
      RES.append(L1[i])
      i += 1
    else:
      RES.append(L2[j])
      j += 1
  while i<len(L1):
      RES.append(L1[i])
      i += 1
  while j<len(L2):
      RES.append(L2[j])
      j += 1
  return RES
    
##############################################################

L = [324, 2, 12432, 923, 23, 523, 7, 2, 12302, 923, 1, 12432]

print("original: ", L)
print("máximo:", maximo(L))
print("pos máxima:", maximo_pos(L))
copia = list(L)
mergesort(copia)
print("mergesort:", copia)
