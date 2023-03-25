# Implementation des Fakultätsalgorithmus mit Rekursion

import sys
import time

def Fakultät(n):
    try:
        if n == 0:
            return 1
        else:
            return n * Fakultät(n-1)
    except RecursionError:
        print("Die Rekursion ist zu tief!")
        sys.exit()



n = float(input("Geben Sie eine natürliche Zahl ein: "))

if n > sys.getrecursionlimit()-10:
    sys.setrecursionlimit(int(n)+10)

t1 = time.time()

print(Fakultät(n))

print("Die Berechnung dauerte", int((time.time() - t1) * 1_000_000), "ns")