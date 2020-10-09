#Przygotować funkcję, która przyjmie 3 argumenty: 2 pierwsze cyfry aktualnego roku, 2 ostatnie cyfry aktualnego roku, wiek użytkownika, a następnie zwróci jego rok urodzenia
def funkcja(rok1,rok2,wiek):
    rok=str(rok1)+str(rok2)
    wynik=int(rok)-wiek
    return wynik
rok1=20
rok2=20
wiek=20
print(funkcja(rok1,rok2,wiek))