# tablica = [5, 2, 8, 1]
# n = len(tablica)
# print(tablica)
# # 1. 1405-32
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

tablica11 = [2, -5, 4, -5, 7, -11]
dl_tablicy = len(tablica11)
print(tablica11)
index = 0
min = tablica11[index]
index1 = 0 # to jest indeks pozycji, na ktora wstawiam kolejna najmniejsza liczbe z tablicy
index2 = 0 # to jest indeks pozycji, ktora ma najmniejsza liczba na tablicy
# petla zatrzyma sie, gdy index bedzie rowny dlugosci tablicy
while index < dl_tablicy:
    # warunek sprawdza najpierw czy index jest mniejszy o 2 od dlugosci tablicy (bo jesli tablica ma dlugosc 6,
    # to dlugosc tablicy -1 = 5, to warunek bedzie spelniony do wartosci indexu 4, nastepnie sprawdza czy
    # wartosc min, ktora juz jest jest wieksza niz wartosc indexu zwiekszona o 1, bo min to cos co ma w tym momencie
    # index 0, czyli sprawdzam dla kolejnej - index+1, wowczas wartosc minimalna, to wlasnie ta kolejna liczba na
    # liscie. Poniewaz wartosc maxymalna wartosc indexu dla tablicy 6-elementowej, to 4, tablica porownuje do
    # index+1, cyli do wartosci indexu 5
    if index < dl_tablicy - 1 and min > tablica11[index+1]:
        # min jest wieksza niz tablica11[index+1], dlatego teraz to tablica11[index+1] jest min
        min = tablica11[index+1]
        # wartosc index2 przyjmuje teraz wartosc z tablicy index+1
        index2 = index + 1
    # inkrementujemy za kazdym razem wartosc indexu
    index += 1
    # jesli wartosc indexu bedzie rowna dl. tablicy, co bedzie znaczylo,
    # ze poprzedni warunek sprawdzil wszytskie elementy z listy
    if index == dl_tablicy:
        # zamieniamy pozycjami element, ktory aktualnie jest minimalny z tym,
        # ktory jest na pozycji, na ktora chcemy go umiescic
        tablica11[index2], tablica11[index1] = tablica11[index1], tablica11[index2]
        print(tablica11)
        # zwiekszamy wartosc index1, dlatego ze to kolejna pozycja,
        # na ktora chcemy wstawic kolejna minimalna wartosc z tablicy
        index1 += 1
        # teraz zaczynamy sprawdzanie od nastepnego elementu, bo ten z pozycji index1 przed inkrementacja jest juz zajety
        index = index1
        # takze index2 ma miec wyzsza wartosc, bo juz poprzednia pozycja jest zajeta
        index2 = index1
        # w tym warunku sprawdzamy, czy nie ustawilismy kolejnosci dla wszytskich elementow tablicy, bo jesli
        # index po inkrementacji dla listy szescioelementowej bedzie mial wartosc 6, wowczas warunek sie nie wykona,
        # jesli jednak wartosc indexu bedzie mniejsza, wowczas jako wartosc min ustanawiamy nowy element z listy
        if index < dl_tablicy:
            min = tablica11[index]
