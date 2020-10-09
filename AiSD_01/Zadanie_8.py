#Przygotować skrypt, w którym użytkownik będzie wprowadzał do listy wartości używając pętli, a następnie wartości z tej zostanią zrzutowane do krotki.
lista=[]
for i in range(5):
    liczba=int(input())
    lista.append(liczba)

print(lista)
print(tuple(lista))