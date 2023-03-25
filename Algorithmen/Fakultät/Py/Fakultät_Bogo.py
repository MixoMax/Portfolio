# bogo Implementation des Fakultätsalgorithmus

import random
import time

def Fakultät(n):
    # Definiere eine Liste von Ganzzahlen von 1 bis n
    lst = list(range(1, n+1))
    
    # Mische die Liste solange, bis sie sortiert ist
    while lst != sorted(lst):
        random.shuffle(lst)
    
    # Multipliziere alle Elemente der Liste um die Fakultät zu berechnen
    result = 1
    for num in lst:
        result *= num
    
    return result

for n in [1,100,500,1000,2500,5000,9999]:
    times = []
    for i in range(100):
        t1 = time.time()
        f = Fakultät(n)
        times.append(int((time.time() - t1) * 1_000_000))
    print(n, sum(times)/len(times))