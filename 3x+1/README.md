# 3x+1 Programme in verschiedenen Sprachen

## Inhalt

* [Beschreibung](#Beschreibung)
* [Implementierung](#Implementierung)
* [Sprachen und Zeitmessung](#Sprachen-und-Zeitmessung)

## Beschreibung

Die Collatz-Folge ist eine Folge von natürlichen Zahlen, die wie folgt definiert ist:

```f(n) = n/2, wenn n gerade ist (n mod 2 = 0))```  
```f(n) = 3n+1, wenn n ungerade ist (n mod 2 = 1))```

Die Collatz-Folge für eine beliebige natürliche Zahl `n` ist definiert als:

```n, f(n), f(f(n)), f(f(f(n))), ...```

Die Collatz-Folge endet immer bei 1. Die Aufgabe ist es nun, für eine beliebige natürliche Zahl `n` die Länge der Collatz-Folge zu berechnen. Die Länge der Collatz-Folge für eine beliebige natürliche Zahl `n` ist definiert als:

```L(n) = 1 + L(f(n))```


## Implementierung

Die Implementierung ist in allen Sprachen sehr ähnlich und in 3 Schritte aufteilbar:

1. "boilerplate" Code, in dem relevante Bibliotheken importiert, grund Variablen deklariert und die Startzeit gemessen wird.

2. Die eigentliche Berechnung der Collatz-Folge in einer for-Schleife mit innerer while-Schleife. Dabei wird für jede Zahl die Anzahl der Schritte gezählt und mit der bisher höchsten Zahl verglichen und ggf. ersetzt.

3. Die Zeitmessung wird beendet und die Ergebnisse ausgegeben. 

Output:

```<Zahl mit den Meisten Schritten> <Anzahl der Schritte> <Zeit in ms>```


## Sprachen und Zeitmessung

| Sprache | Zeit[¹](#fußnoten) |
| :--- | :--- |
| [C++](./cpp/3x+1.cpp) | 936 ms |
| [Python](./py/3x+1.py) | 28515 ms[²](#fußnoten) |
| [Go](./go/3x+1.go) | 312 ms |
| [Fortran90](./fortran/3x+1.f90) | 853 ms |


## Reflexion und Lessons Learned

Dieses Projekt war für mich eine gute Möglichkeit, meine Grundlegenden Fähigkeiten zu testen und zu verbessern, da die Collatz-Folge in allen Sprachen grundsätzlches verständnis von Variablen, if-Statements und for- und while-Loops erfordert, aber auch Hardware-nähere Kentnisse, wie verschieden Lange Integer in den verschiedenen Sprachen implementiert sind.

<br>

##### Fußnoten
---
1. Die Zeitmessung wurden alle auf einem AMD Ryzen 7 2700 bei 3.9GHz mit 16GB Ram durchgeführt. Die Zeiten wurden von den jeweiligen Sprachen selbst gemessen. Zeiten sind durchschnittswerte von 5 Durchläufen.
2. Die Zeiten in Python sind aufgrunddessen soviel langsamer als alle anderen (kompilierten) Sprachen, da python keine native implementation for ```long``` bzw. ```int_fast64_t``` hat, sondern stadtdessen eine Klasse, die die Zahl als String repräsentiert namens [```Bignum```](https://peps.python.org/pep-0237/#implementation). Die Berechnung der Collatz-Folge für große Zahlen ist dadurch sehr ineffizient und nicht mit den anderen Sprachen vergleichbar. Die Python implementierung ist daher nur als "Proof of Concept" zu sehen und sollte nicht als Benchmark verwendet werden.