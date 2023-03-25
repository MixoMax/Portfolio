# Implementationen des Fakultätsalgorithmus in Python

## Inhalt

- [Rekursion](./Fakultät_Rekursion.py)
- [Iteration](./Fakultät_Iteration.py)
- [Bogo](./Fakultät_Bogo.py)

## Rekursiver Algorithmus

Der rekursive Algorithmus ist der einfachste Algorithmus, der die Fakultät einer Zahl berechnet. Er ist sehr einfach zu implementieren, hat aber den Nachteil, dass in Python die maximale Rekursionstiefe auf 1000 beschränkt ist, weil bei deutlich höherer Stacktiefe der C Stack "overflowed". Dieser Algorithmus ist daher nur für Zahlen unter 998[¹] geeignet.

Der Algorithmus ist zwar langsamer als der iterative Algorithmus, aber nicht sehr viel:

| Zahl | Zeit in ns |
|------|------------|
|1|1.06|
|100|51.86|
|500|514.6|
|1000|1203.85|
|2500|1819.36|
|5000|5534.66|
|9999|22973.61|

Dies sind die Testergebnisse mit einer Stacktiefe von 10000. Die Ergebnisse sind der Durchschnitt von 100 Durchläufen.

---

## Iterativer Algorithmus

Diese Implementierung ist zwar deutlich langsamer als die Rekursive Implementierung, aber sie ist für alle Zahlen geeignet.

| Zahl | Zeit in ns |
|------|------------|
| 1 | 1.07 |
| 100 | 21.66 |
| 500 | 307.25 |
| 1000 | 837.98 |
| 2500 | 1986.06 |
| 5000 | 4814.23 |
| 9999 | 19694.34 | 

Zeiten sind der Durchschnitt von 100 Durchläufen.


---

## Bogo Algorithmus

Der Bogo Algorithmus ist ein Algorithmus, der die Fakultät einer Zahl berechnet, indem er Zufallszahlen generiert und guckt, ob die Wurzel der Zuwahlzahl die Zahl ist, für die die Fakultät berechnet werden soll. Dieser Algorithmus ist sehr sehr langsam und sollte nicht in einem echten Programm verwendet werden.

Zeitkomplexität:
    O(n) (best case)
    O(n*n!) (average case)
    O(infinity) (worst case)

| Zahl | Zeit in ns |
|------|------------|



## Fußnoten

### 1: Warum 998 und nicht 1000?

In Python ist die Rekursionstiefe nicht zu verwechseln mit der C Stack tiefe. die Funktion sys.setrecursionlimit(n) setzt eigentlich die Stack tiefe, nicht das Rekursionslimit. Da Die Stacktiefe aber für alle Funktionen gilt, braucht Python schon 3: 1 für `input()`, und 2 für die beiden `print()` functionen. Das bedeutet, dass die übrig gebliebene Stacktiefe nur noch 997 beträgt.

