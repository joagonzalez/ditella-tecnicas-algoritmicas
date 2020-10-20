def pos_dos(n):
    if n == 0:
        return 1
    elif n > 0:
        return 2 * pos_dos(n-1)
    else:
        return -1

def pos_a(a, n):
    if n == 0:
        return 1
    elif n > 0:
        return a * pos_a(a, n-1)
    else:
        return -1

if __name__ == '__main__':
    print(pos_dos(3))
    print(pos_dos(4))
    print(pos_dos(5))
    print(pos_dos(1))
    print(pos_dos(0))
    print(pos_dos(-4))

    print(pos_a(2, 3))
    print(pos_a(2, 4))
    print(pos_a(2, 5))
    print(pos_a(2, 1))
    print(pos_a(2, 0))
    print(pos_a(2, -4))
