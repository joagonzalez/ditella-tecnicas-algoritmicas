def es_par(n): # O(n)
    if n == 1:
        return False
    elif n == 0:
        return True
    else:
        return es_par(n-2)

if __name__ == '__main__':
    print(es_par(1))
    print(es_par(2))
    print(es_par(3))
    print(es_par(4))
    print(es_par(5))
    print(es_par(6))