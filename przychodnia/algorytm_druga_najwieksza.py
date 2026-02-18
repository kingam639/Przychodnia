# Oto zadanie na pętle + warunki:
# Masz tablicę liczb (mogą być dodatnie i ujemne). Napisz program, który:
#
# Znajduje drugą największą liczbę w tablicy (nie największą, ale drugą!)
# Znajduje drugą najmniejszą liczbę w tablicy
# tablica = [5, 12, -3, 8, 12, 1, -7]
tablica = [10, 10, 5, 3, 1]
# Największa: 12
# Druga największa: 8  (uwaga: nawet jeśli 12 pojawia się dwa razy!)
# Najmniejsza: -7
# Druga najmniejsza: -3
najwieksza_1 = tablica[0]
najwieksza_2 = tablica[1]
# sprawdza, czy liczba przypisana jako pierwsza_najwieksza jest rzeczywiscie wieksza niz druga_najwieksza
if najwieksza_1 < najwieksza_2:
    najwieksza_1, najwieksza_2 = najwieksza_2, najwieksza_1
if len(tablica) > 2:
    for element in tablica[2:]:
        # sprawdza, czy kolejny element jest najwiekszy
        if element > najwieksza_1:
            najwieksza_1, najwieksza_2 = element, najwieksza_1 # dotychczasowa najwieksza staje sie 2-ga najwieksza
        # sprawdza czy kolejny element jest mniejszy niz najwiekszy, a wiekszy niz 2-ga najwieksza
        elif element < najwieksza_1 and element > najwieksza_2:
            najwieksza_2 = element # element staje sie dotychczasowa 2-ga najwieksza
# printuje druga najwieksza
print(najwieksza_2)