import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

def fibonacci(i, n = 0, m = 1):
    f = [n, m]
    
    while f[-1] < i:
        n, m = m, n + m
        f.append(m)
    
    return f

i = 0
f = fibonacci(100000)
f_max = 100000
while True:
    i += 1
    
    
    if not is_prime(i):
        continue
    if i > f_max:
        f = fibonacci(i, f[-2], f[-1])
        f_max = f[-1]
    
    if i in f and is_prime(i):
        print("Fibonacci-Primzahl gefunden:" + str(i))

# What is the biggest Fibonacci-Prime number you can find?