import time
import math

def to_int(x):
    try:
        return int(x)
    except ValueError:
        for char in x:
            if char not in "0123456789.":
                x = x.replace(char, "")
            if x.count(".") > 1:
                x = x.replace(".", "")
            
            return int(x)
        
s = to_int(input("Ab welcher Zahl sollen Primzahlen berechnet werden? "))
k = to_int(input("Bis zu welcher Zahl sollen Primzahlen berechnet werden? "))

if s > k:
    s, k = k, s

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0:
            return False
    return True

t1 = time.time()

primzahlen = [p for p in range(s, k+1) if is_prime(p)]

t2 = time.time()

print(f"ℙ ∈ [ {s}, {k} ]:")

print(", ".join(str(p) for p in primzahlen))

print(f"Es wurden {len(primzahlen)} Primzahlen gefunden. (" + str(int(len(primzahlen) / (k-s+1) * 100)) + " %)") 

print(f"Die Berechnung dauerte {int((t2 - t1)*1000)} ms.")