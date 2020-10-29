def fibonacci(n): # O(2n)
    if n == 0 or n == 1:
        return 1
    elif n > 1:
        return fibonacci(n-1) + fibonacci(n-2) # O(2)
    else: 
        return -1

if __name__ == '__main__':
    for i in range(15):
        print(fibonacci(i))