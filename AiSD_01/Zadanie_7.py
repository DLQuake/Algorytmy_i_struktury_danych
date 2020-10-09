#Przygotować funkcję, która przyjmie 1 argument w postaci listy, a następnie zwróci te elementy w postaci krotki.
def funkcja(lista):
    krotka=tuple(lista)
    return krotka
lista=[1,2,3,4,5,6,7,8,9,10]
print(funkcja(lista))