# TODO: Sortowanie przez wybieranie - moja wersja pierwsza

# tablica11 = [2, -5, 4, -5, 7, -11]
# dl_tablicy = len(tablica11)
# print(tablica11)
# index = 0
# min = tablica11[index]
# index1 = 0 # to jest indeks pozycji, na ktora wstawiam kolejna najmniejsza liczbe z tablicy
# index2 = 0 # to jest indeks pozycji, ktora ma najmniejsza liczba na tablicy
# # petla zatrzyma sie, gdy index bedzie rowny dlugosci tablicy
# while index < dl_tablicy:
#     # warunek sprawdza najpierw czy index jest mniejszy o 2 od dlugosci tablicy (bo jesli tablica ma dlugosc 6,
#     # to dlugosc tablicy -1 = 5, to warunek bedzie spelniony do wartosci indexu 4, nastepnie sprawdza czy
#     # wartosc min, ktora juz jest jest wieksza niz wartosc indexu zwiekszona o 1, bo min to cos co ma w tym momencie
#     # index 0, czyli sprawdzam dla kolejnej - index+1, wowczas wartosc minimalna, to wlasnie ta kolejna liczba na
#     # liscie. Poniewaz wartosc maxymalna wartosc indexu dla tablicy 6-elementowej, to 4, tablica porownuje do
#     # index+1, cyli do wartosci indexu 5
#     if index < dl_tablicy - 1 and min > tablica11[index+1]:
#         # min jest wieksza niz tablica11[index+1], dlatego teraz to tablica11[index+1] jest min
#         min = tablica11[index+1]
#         # wartosc index2 przyjmuje teraz wartosc z tablicy index+1
#         index2 = index + 1
#     # inkrementujemy za kazdym razem wartosc indexu
#     index += 1
#     # jesli wartosc indexu bedzie rowna dl. tablicy, co bedzie znaczylo,
#     # ze poprzedni warunek sprawdzil wszytskie elementy z listy
#     if index == dl_tablicy:
#         # zamieniamy pozycjami element, ktory aktualnie jest minimalny z tym,
#         # ktory jest na pozycji, na ktora chcemy go umiescic
#         tablica11[index2], tablica11[index1] = tablica11[index1], tablica11[index2]
#         print(tablica11)
#         # zwiekszamy wartosc index1, dlatego ze to kolejna pozycja,
#         # na ktora chcemy wstawic kolejna minimalna wartosc z tablicy
#         index1 += 1
#         # teraz zaczynamy sprawdzanie od nastepnego elementu, bo ten z pozycji index1 przed inkrementacja jest juz zajety
#         index = index1
#         # takze index2 ma miec wyzsza wartosc, bo juz poprzednia pozycja jest zajeta
#         index2 = index1
#         # w tym warunku sprawdzamy, czy nie ustawilismy kolejnosci dla wszytskich elementow tablicy, bo jesli
#         # index po inkrementacji dla listy szescioelementowej bedzie mial wartosc 6, wowczas warunek sie nie wykona,
#         # jesli jednak wartosc indexu bedzie mniejsza, wowczas jako wartosc min ustanawiamy nowy element z listy
#         if index < dl_tablicy:
#             min = tablica11[index]

# TODO: Sortowanie przez wybieranie - rozwiazanie algorytmu znalezione w internecie

# for i in range(n):
#     # print(f"i: {i}")
#     min_idx = i # najmniejszy wolny index w nieposortowanej tablicy
#     for j in range(i+1, n):
#         # print(f"j: {j}")
#         # sprawdza, czy kolejny element jest mniejszy
#         if tablica[min_idx] > tablica[j]:
#             min_idx = j
#     # gdy znajduje kolejny najmniejszy element wstawia go na pozycje
#     # o najmniejszym indeksie w nieposortowanej czesci tablicy
#     tablica[i], tablica[min_idx] = tablica[min_idx], tablica[i]
# # print(tablica)


# TODO: Sortowanie przez wybieranie - rozwiazanie na podstawie rozw. algorytmu z internetu z dodaniem funkcji
# TODO: indeks_najmniejszej_wartosci(lista) i sortowanie_przez_wybieranie(lista)

def indeks_najmniejszej_wartosci(lista):
    """Znajduje indeks liczby o najmniejszej wartosci."""

    # indeks najmniejszej wartosci ustawiony domyslnie na najnizszy indeks listy
    min_idx = 0
    dlugosc_listy = len(lista)

    # zakres petli for zaczyna sie na indeksie 1, bo indeks 0 to min_idx
    for indeks in range(1, dlugosc_listy):
        # sprawdza, czy wartosc liczby pod indeksem jest mniejsza niz liczby pod indeksem min_ind
        if lista[min_idx] > lista[indeks]:
            min_idx = indeks
    # zwraca indeks liczby o najmniejszej wartosci
    return min_idx


def sortowanie_przez_wybieranie(lista):

    n = len(lista)

    for i in range(n):
        # funkcja dostaje wycinek (lista[i:]), zwraca indeks w wycinku,
        # więc dodajemy i żeby dostać indeks w oryginalnej tablicy
        min_idx = indeks_najmniejszej_wartosci(lista[i:]) + i
        # print(f"{min_idx = }") # "f-string debug syntax"
        # zamiana pierwszego wolnego indeksu z nieposortowanej czesci tablicy z najmniejsza wartoscia tej czesci tablicy
        lista[i], lista[min_idx] = lista[min_idx], lista[i]
    return lista # TODO: zostawic czy usunac?


tablica = [1, 4, 0, 5, -3, 2]
print(tablica)
print(id(tablica))

# wywolanie funkcji sortujacej
sortowanie_przez_wybieranie(tablica)
print(tablica)

