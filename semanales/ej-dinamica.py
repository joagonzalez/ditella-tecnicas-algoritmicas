# Dado un entero n mayor o igual a 0, devuelve el n-esimo
# termino de la sucesion de Padovan, definida como 
# P(0)=P(1)=P(2)=1, P(n)=P(n-2)+P(n-3).
# https://en.wikipedia.org/wiki/Padovan_sequence
# Complejidad exponencial respecto de n.
def padovan(n):
  if n==0 or n==1 or n==2:
    res = 1
  else:
    res = padovan(n-2) + padovan(n-3)
  return res

# Dado un entero n mayor o igual a 0, devuelve el n-esimo
# termino de la sucesion de Padovan, definida como 
# P(0)=P(1)=P(2)=1, P(n)=P(n-2)+P(n-3).
# https://en.wikipedia.org/wiki/Padovan_sequence
# Complejidad lineal respecto de n.
def padovan_lineal(n):
    rv = [1, 1, 1]
    i = 3
    while i <= n: 
        rv.append(rv[i-2] + rv[i-3])
        i += 1
    return rv[n]


secuencia = ''
for i in range(20):
  secuencia = secuencia + str(padovan_lineal(i)) + ' '
print(secuencia) 
# debe imprimir: 1 1 1 2 2 3 4 5 7 9 12 16 21 28 37 49 65 86 114 151
