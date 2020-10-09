# Przygotować funkcję, która przyjmie w parametrach imię i nazwisko, oraz zwróci pierwszą literę imienia i nazwisko połączone kropką. Funkcja powinna również dbać o poprawność wielkich liter. Przykładowo, wejście: (jan, kowalski), wyjście: J. Kowalski.
def funkcja(x,y):
    return x[0].capitalize()+'.'+y.capitalize()

imie="dominik"
nazwisko="lewczyński"

print(funkcja(imie,nazwisko))