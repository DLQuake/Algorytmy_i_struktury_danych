#Przygotować funkcję, która przyjmie argument w postaci łańcucha znaków, a następnie zwróci wartość logiczną informującą o tym czy przekazany tekst jest palindromem.

def funkcja(napis):
    if napis==napis[::-1]:
        return True
    else:
        return False

napis1='radar'
napis2='ania'

print(funkcja(napis1))
print(funkcja(napis2))