# Przygotować funkcję, która przyjmie w parametrach pierwszą literę imienia, oraz nazwisko, a następnie zwróci te wartości połączone kropką. Przykładowe wyjście: J. Kowalski

def funkcja(x,y):
    return x+'.'+y

imie="Dominik"
nazwisko="Lewczyński"

print(funkcja(imie[0],nazwisko))