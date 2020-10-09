#Przygotować funkcję, która przyjmie 1 argument całkowitoliczbowy, a następnie zwróci nazwę dnia tygodnia odpowiadającą przekazanemu argumentowi. Nie należy w tym zadaniu używać instrukcji warunkowych! Przykładowo, wejście: 6, wyjście: sobota.

def funkcja(nr_tygodnia):
    lista=['poniedzialek','wtorek','sroda','czwartek','piatek','sobota','niedziela']
    return lista[nr_tygodnia-1]

nr_tygodnia=int(input())
print(funkcja(nr_tygodnia))