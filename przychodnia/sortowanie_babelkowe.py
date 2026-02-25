tablica = [5, 2, 8, 3]
n = len(tablica)
# print(tablica)
# # # 1. 1405-32
# for i in range(n):
#     for j in range(n-1):
#         # warunek sprawdza, czy kolejny element na liscie jest wiekszy od poprzedniego,
#         # jesli tak zamienia je miejscami
#         if tablica[j] > tablica[j+1]:
#             tablica[j], tablica[j+1] = tablica[j+1], tablica[j]
#     print(tablica)
#     # zmniejszam rozmiar tablicy za kazdym razem, gdy najwiekszy element zostaje wstawiony na ostatnie wolne miejsce
#     n -= 1
# print(tablica)

def indeks_wiekszej_wartosci(tablica, idx1, idx2):
    """Funkcja porownuje sasiedne liczby, jesli liczba o nizszym indeksie ma wieksza wartosc, zamienia je miejscami.
    Zwraca True, gdy nastapila zamiana."""
    if tablica[idx1] > tablica[idx2]:
        tablica[idx1], tablica[idx2] = tablica[idx2], tablica[idx1]
        return True
    return False

def sortowanie_jednokrotne(lista, dlugosc_tablicy, numer_przejscia):
    """Funkcja sortuje tablice za pomoca algorytmu sortowania babelkowego. Przechodzac przez tablice jednokrotnie
    wypycha najwiekszy element na koniec tablicy.
    Args:
    lista: tablica do sortowania
    dlugosc_tablicy: długość tablicy
    numer_przejscia: ile razy już przeszliśmy przez tablicę
    """
    # zmienna czy_zmiana sledzi, czy jakies liczby byly zamienione
    czy_zmiana = False
    for j in range(dlugosc_tablicy - numer_przejscia - 1):
        wynik = indeks_wiekszej_wartosci(lista, j, j + 1)
        # jesli liczby zostaly zamienione zmienna wynik bedzie miec wartosc True,co zmieni wartosc zmiennej czy_zmiana
        if wynik:
            czy_zmiana = True
        # czy_zmiana = czy_zmiana or wynik # alternatywna wersja sprawdza
    return czy_zmiana

def sortowanie_babelkowe(lista):
    """Funkcja sortuje cala tablice za pomoca algorytmu sortowania babelkowego."""
    n = len(lista)
    for i in range(n):
        # po każdym przejściu największy element "wypływa" na koniec,
        # więc nie trzeba go już sprawdzać (stąd n - i - 1)
        # zmienna czy_zmiana zwroci True, jesli podczas przejscia przez petle nastapila zamiana liczb
        czy_zmiana = sortowanie_jednokrotne(lista, n, i)
        print(czy_zmiana)
        print("A")
        print(lista)
        if not czy_zmiana:
            print(i)
            break
# wywolanie funkcji sortujacej
sortowanie_babelkowe(tablica)
print(tablica)
# print(tablica[2], tablica[3])
# indeks_wiekszej_wartosci(tablica, 2, 3)
# def sortowanie_babelkowe(lista):
#     n = len(lista)
#     for i in range(n):
#         # po kazdym przejsciu przez cala tablice zmniejsza sie jej rozmiar
#         # o elementy juz posortowane, ktore trafily na koniec tablicy
#         for j in range(n-i-1):
#             indeks_wiekszej_wartosci(lista, j, j+1)
#         print(lista)
#         # zmniejszam rozmiar tablicy za kazdym razem, gdy najwiekszy element zostaje wstawiony na ostatnie wolne miejsce
#         # n -= 1

# sortowanie_babelkowe(tablica)
# print(tablica)

