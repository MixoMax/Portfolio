# Implementation des Fakultätsalgorithmus mit Iteration

import time


def Fakultät(n):
    if n == 0:
        return 1
    else:
        f = 1
        for i in range(1, int(n+1)):
            f *= i
        return f
    
    

n = float(input("Geben Sie eine natürliche Zahl ein: "))

t1 = time.time()

print(Fakultät(n))

print("Die Berechnung dauerte", int((time.time() - t1) * 1_000_000), "ns")