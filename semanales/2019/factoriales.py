# Devuelve una lista con los factoriales desde 1 hasta n.
# Complejidad cuadrática respecto de n.
def factoriales(n):
  rv = []
  i = 1
  while i <= n:
    rv.append(factorial(i))
    i = i + 1
  return rv

# Devuelve el factorial de n, es decir 1*2*3*...*n.
def factorial(n):
  rv = 1
  i = n
  while i > 0:
    rv = rv * i
    i = i - 1
  return rv

# Devuelve una lista con los factoriales desde 1 hasta n.
# Complejidad lineal respecto de n.
def factoriales_lineal(n):
  ## COMPLETAR ##

  
print(factoriales_lineal(1))  # debe imprimir [1]
print(factoriales_lineal(5))  # debe imprimir [1, 2, 6, 24, 120]
print(factoriales_lineal(10)) # debe imprimir [1, 2, 6, 24, 120, 720, 5040, 40320, 3628800]

