# QTally

QTally ist ein Programm zur Erfassung von Menschenmengen. Es ist in Python mit PySide6 geschrieben und hat eine Qt GUI. QTally wird beim [Südsee Open Air 2023](https://niedersachsen.naturfreundejugend.de/termine/-/-/show/4452/suedee_open_air) eingesetzt, um die Besucherzahlen zu erfassen, um sie später auszuwerten. Obwohl QTally als Auftragsarbeit entstanden ist, ist es unter der [Apache 2.0 Lizenz](https://www.apache.org/licenses/LICENSE-2.0) veröffentlicht, sodass jeder es frei verwenden kann.

[GitHub-Repository](https://www.github.com/MixoMax/QTally)

## Was ich gelernt habe

- Error Handling in Python
- Intuitives Design (in Qt)
- Object Oriented Programming
- SQLAlchemy (SQL Datenbanken in Python)


Da das Programm für die Benutzung von Laien gemacht ist, muss es nicht nur Intuitiv sein, sondern auch so benutzerfreundlich sein, dass es nicht unabsichtlich geschlossen werden kann, ohne zu speichern. Mehrere Funktionen, wie das zurücksetzen der Datenbank, sind nur über ein Passwort in der Konsole zugänglich, um zu verhindern, dass die Datenbank ausversehen gelöscht wird.
