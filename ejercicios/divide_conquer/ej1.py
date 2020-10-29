from math import ceil
from math import floor

def pot_a(a, n):
    if n == 0:
        result = 1  # caso base
    else:
        # Divide
        aux = floor(n % 2) 
        medio = floor(n/2)

        # Conquer & Combine
        if aux == 0:
            result = pot_a(a, medio) * pot_a(a, medio) # si par => a^n = a^(n/2) * a^(n/2)
        else: 
            result = pot_a(a, medio) * pot_a(a, medio) * a # si impar => a^n = a^(n/2) * a^(n/2) * a
        
    # Combine
    return result

if __name__ == '__main__':
    calcular = [0,1,2,3,4,5]
    for i in calcular:
        print(pot_a(2, i))