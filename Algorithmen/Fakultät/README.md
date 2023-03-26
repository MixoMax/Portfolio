# Fakultät Algorithmus

## Inhalt

- [Beschreibung](#Beschreibung)
- [Implementierung](#Implementierung)

## Beschreibung

Die Fakultät ise eine mathematische Funktion, die für eine natürliche Zahl `n` definiert ist als:

```n! = n * (n-1) * (n-2) * ... * 2 * 1```

DIe Fakultät-Funktion wird oft in der Kombinatorik verwendet, um die Anzahl der Möglichkeiten zu berechnen, in denen `n` Objekte angeordnet werden können.

Die Aufgabe ist es nun, für eine beliebige natürliche Zahl `n` die Fakultät zu berechnen.

## Implementierung

Die Implementierung ist in allen Sprachen sehr ähnlich und in 3 Schritte aufteilbar:

1. "boilerplate" Code, in dem relevante Bibliotheken importiert, grundlegende Variablen deklariert und die Startzeit gemessen wird.
2. Die eigentliche Berechnung der Fakultät in einer for-Schleife. Dabei wird für jede Zahl von 1 bis n das Produkt berechnet und in einer Variable gespeichert.
3. Die Zeitmessung wird beendet und die Ergebnisse ausgegeben.

Output:

>Start Zahl

>Fakultät

>Zeit in ms

Alternativ kann die Funktion auch direkt aufgreufen, oder von einem anderen Programm importiert werden.

Die Argumente der Funktion sind:

```Fakultät(n) -> i ```

in den Kompilierten Sprachen sind die Datentypen:

```n: float oder int```

```i: float oder int```



## Sprachen

der Fakultät Algorithmus wurde in den folgenden Sprachen implementiert:

- [Python](./Py/Fakultät.py)
- [C++](./cpp/Fakultät.cpp)

in allen Sprachen wurde der Fakultätsalgorithmus iterativ implementiert, ohne eine eingebaute mathematische Funktion dafür zu verwenden.