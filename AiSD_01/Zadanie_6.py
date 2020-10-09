#Przygotować skrypt, w którym użytkownik będzie podawał kolejne liczby w pętli, dopóki suma wszystkich podanych do tej pory liczb nie osiągnie wartości 100.
import sys
suma=0
while suma!=100:
    liczba=int(input())
    suma+=liczba
else:
    sys.exit(0)