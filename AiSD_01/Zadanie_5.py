#Przygotować funkcję, która przyjmie 2 argumenty, a następnie zwróci wynik ich dzielenia. Należy sprawdzić w jednej instrukcji if (bez użycia elif i else), czy obydwie liczby są dodatnie oraz czy druga liczba jest różna od 0.
def funkcja(a,b):
    if a>0 and b>0 and b!=0:
        return a/b

print(funkcja(2,3))