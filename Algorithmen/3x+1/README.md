# 3x+1 Algorithmus

## Inhalt

* [Beschreibung](#Beschreibung)
* [Implementierung](#Implementierung)
* [Sprachen](#Sprachen)
* [Reflexion](#Reflexion)



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

>Start Zahl

>Anzahl an Schritten

>Zeit in ms


## Sprachen

Der 3x+1 Algorithmus wurde in den folgenden Sprachen nur mit den Standardbibliotheken implementiert:
- [Python](./Py/3x+1.py)
- [C++](./cpp/3x+1.cpp)
- [fortran](./fortran/3x+1.f90)
- [Go](./go/3x+1.go)


## Reflexion

Dieses Projekt war für mich eine gute Möglichkeit, meine Grundlegenden Fähigkeiten zu testen und zu verbessern, da die Collatz-Folge in allen Sprachen grundsätzlches verständnis von Variablen, if-Statements und for- und while-Loops erfordert, aber auch Hardware-nähere Kentnisse, wie verschieden Lange Integer in den verschiedenen Sprachen implementiert sind.