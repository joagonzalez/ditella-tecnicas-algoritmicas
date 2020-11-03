# Devuelve el n-ésimo número de Fibonacci. Complejidad exponencial.
def fib_rec(n):
  if n==0:
    res = 0
  elif n==1:
    res = 1
  else:
    res = fib_rec(n-1) + fib_rec(n-2)
  return res
  
# Devuelve el n-ésimo número de Fibonacci. Complejidad lineal.
def fib_iter(n):
  f = [0, 1]
  i = 2
  while i <= n:
    f.append(f[i-1] + f[i-2])
    i += 1
  return f[n]

if __name__ == '__main__':
    hasta = 100
    for i in range(hasta+1):
        print('algoritmo iterativo', i, fib_iter(i))
    for i in range(hasta+1):
        print('algoritmo recursivo', i, fib_rec(i))


# time complexity analysis: https://stackoverflow.com/questions/360748/computational-complexity-of-fibonacci-sequence