#Przygotować funkcję, która przyjmie 3 parametry: imię, nazwisko i funkcję przetwarzającą te dane, a następnie zwróci wynik działania funkcji przyjętej w 3. parametrze. Przykładwo, wejście: (jan, kowalski, funkcja_z_zadania_2), wyjście: J. Kowalski.
import Zadanie_2

def funkcja(imie,nazwisko,funkcja_z_zadania_2):
    return funkcja_z_zadania_2

imie="dominik"
nazwisko="lewczyński"
funkcja_z_zadania_2=Zadanie_2.funkcja(imie,nazwisko)
funkcja(imie,nazwisko,funkcja_z_zadania_2)