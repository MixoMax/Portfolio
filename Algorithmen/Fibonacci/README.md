# Fibonacci Algorithmus

## Inhalt

- [Beschreibung](#Beschreibung)
- [Implementierung](#Implementierung)
- [Sprachen](#Sprachen)
- [Reflexion](#Reflexion)

## Beschreibung

Die Fibonacci-Folge ist eine unendliche Folge natührlicher Zahlen, die wie folgt definiert ist:

```f(n) = f(n-1) + f(n-2)```  
```f(0) = 0```  
```f(1) = 1```

Die Fibonacci-Folge kann zwei Beliebige natürliche Zahlen `n` und `m` als Startwerte haben. Die Aufgabe ist es nun, die Fibonacci-Folge für die Zahlen `n` und `m` zu berechnen.

## Implementierung

//implemetierung goes here

## Sprachen

Die Fibonacci-Folge wurde in den folgenden Sprachen nur mit den Standardbibliotheken implementiert:

- [Python](./py/Fibonacci.py)
- [C++](./cpp/Fibonacci.cpp)
- [fortran](./fortran/Fibonacci.f90)

In Python lässt sich die Fibonacci Folge zusätzlich noch mit matplotlib visualisieren:

<img src="./Py/Figure_1.png" alt="Fibonacci Plot" width="75%"/>

## Reflexion

Da die Fibonacci-Folge sehr schnell zu großen Zahlen konvergiert, ist es für das programmieren in lower-level Sprachen (wie c++ und fortran) wichtig, den Hardware Hintergrund (von z.B. Integern und pointern) zu verstehen, um die Berechnung zu optimieren.