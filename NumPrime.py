def isPrime(n):
    cont = 0
    for i in range(0, n):
        if n % (i + 1) == 0:
            cont += 1

    if cont == 2:
        return n

list_prime = [num for num in range(100) if isPrime(num)]
'''for num in range(100):
    if isPrime(num):
        print(f"{num} is prime!")'''

print(list_prime)
