import random
# UWAGA! Do każdego zadania wypisz tablicę tak, aby można było sprawdzić w konsoli czy program wykonał się poprawnie.
# Np w zadaniu 1 musimy poza wynikiem wypisać też liczby które nam się wylosowały.
# Zadanie 1.
# Losowa tablica  i liczenie parzystych
# Wczytaj rozmiar tablicy n. (cin) Wypełnij tablicę n liczbami losowymi
# z przedziału ⟨1, 100⟩. Policz, ile z nich jest parzystych i ile nieparzystych.
# n = random.randint(1, 50)
# bad = True
# while bad:
#     try:
#         n1 = int(input("Wczytaj rozmiar tablicy n: "))
#         bad = False
#     except:
#         print("To nie jest liczba, sprobuj ponownie.")

# tablica1 = [random.randint(1,100) for _ in range(n)]
# # print(tablica1)
#
# tablica = []
# tablica_parzyste = []
# tablica_nieparzyste = []
# for _ in range(n1):
#     x = random.randint(1, 100)
#     tablica.append(x)
#     if x % 2:
#         tablica_nieparzyste.append(x)
#     else:
#         tablica_parzyste.append(x)
#
# print(tablica)
# print(len(tablica))
# tablica_posortowana = sorted(tablica)
# print(tablica_posortowana)
#
# print(tablica_parzyste)
# print(len(tablica_parzyste))
# parzyste_posortowane = sorted(tablica_parzyste)
# print(parzyste_posortowane)
#
# print(tablica_nieparzyste)
# print(len(tablica_nieparzyste))
# nieparzyste_posortowane = sorted(tablica_nieparzyste)
# print(nieparzyste_posortowane)

# Zadanie 2.
# Największa i najmniejsza liczba Utwórz tablicę 10 liczb. Wypełnij ją losowo z przedziału ⟨-50, 50⟩.
# Za pomocą pętli while znajdź min i max.
# tablica2 = []
# for _ in range(10):
#     tablica2.append(random.randint(-50, 50))
# print(tablica2)
#
# index = 1
# min = tablica2[0]
# max = tablica2[0]
#
# while index < len(tablica2):
#     if min > tablica2[index]:
#         min = tablica2[index]
#     if max < tablica2[index]:
#         max = tablica2[index]
#     index += 1

# print(index, min, max)

# Zadanie 3.
# Średnia i elementy większe od średniej Wczytaj n. Wypełnij tablicę losowymi liczbami z ⟨1, 20⟩.
# Oblicz średnią i wypisz elementy większe od średniej.
# n3 = random.randint(1, 10)
# tablica3 = []
# suma = 0
# for _ in range(n3):
#     x = random.randint(1, 20)
#     tablica3.append(x)
#     suma += x
# srednia = suma / n3
# print(tablica3)
# print(srednia)
# for elem in tablica3:
#     if elem > srednia:
#         print(elem)

# Zadanie 4.
# Liczby dodatnie, ujemne i zera Wczytaj n. Wypełnij tablicę danymi od użytkownika (cin). Policz ile jest:
# dodatnich, ujemnych, zer
# Zapytaj użytkownika ile liczb chce podać (to będzie n)
# W pętli poproś użytkownika n razy o wpisanie kolejnych liczb
# Dodaj te liczby do tablicy
# Potem przejdź przez tablicę i policz dodatnie/ujemne/zera
# try: # kod, który może wywołać błąd
#     n = int(input("Powiedz ile chcesz podac liczb: "))
# except ValueError:  # co zrobić gdy wystąpi błąd
#     print("To nie jest liczba, spróbuj ponownie.")
# licznik = 0
# tablica4 = []
# while licznik < n:
#     try: # kod, który może wywołać błąd
#         liczba = int(input("Podaj liczbe: "))
#     except ValueError:  # co zrobić gdy wystąpi błąd
#         print("To nie jest liczba, spróbuj ponownie.")
#     else: # Pozwala wykonac kod, gdy nie ma bledu
#         tablica4.append(liczba)
#         licznik += 1
# print(tablica4)
# licznik_dodatnich = 0
# licznik_ujemnych = 0
# licznik_zer = 0
# for liczba in tablica4:
#     if liczba > 0: # nie moge dac if liczba, bo dla Pythona tylko 0 to False, czyli < 0, tez bylyby True
#         licznik_dodatnich += 1
#     elif liczba == 0:
#         licznik_zer += 1
#     else:
#         licznik_ujemnych += 1
# print(f"Liczb dodatnich jest: {licznik_dodatnich}.")
# print(f"Zer jest:{licznik_zer}.")
# print(f"Liczb ujemnych jest:{licznik_ujemnych}")

# Zadanie 5.
# Odwracanie tablicy Wczytaj n. Wypełnij tablicę losowo. Odwróć tablicę „w miejscu” (pierwszy z ostatnim itd.)
# używając while.
# TODO: dwa wskazniki!
# Implementacja techniki dwóch wskaźników jest zazwyczaj dość prosta. Poniżej znajduje się podstawowy schemat, który można zastosować do implementacji tej techniki:
# Utwórz dwie zmienne, które będą służyły jako wskaźniki. Zazwyczaj jedna z nich zaczyna od początku tablicy lub listy, a druga od końca.
# Utwórz pętlę, która będzie kontynuowana, dopóki wskaźniki nie spotkają się w środku. W przypadku tablicy o parzystej liczbie elementów wskaźniki spotkają się na jednym elemencie. W przypadku tablicy o nieparzystej liczbie elementów wskaźniki spotkają się na dwóch środkowych elementach.
# W każdym obiegu pętli wykonaj operacje na elementach, na które wskazują wskaźniki. To, jakie operacje będą wykonywane, zależy od konkretnego problemu, który próbujesz rozwiązać.
# Po wykonaniu operacji przesuń wskaźniki. Zazwyczaj jeden wskaźnik jest przesuwany o jeden element w prawo, a drugi o jeden element w lewo.
# Powtarzaj kroki 3 i 4, dopóki wskaźniki nie spotkają się w środku.
# n5 = random.randint(1,10)
# tablica5 = []
# print(n5)
# for _ in range(n5):
#     tablica5.append(random.randint(1,100))
# print(tablica5)
# lewy = 0
# prawy = len(tablica5) - 1
# while lewy < prawy:
#     tablica5[lewy], tablica5[prawy] = tablica5[prawy], tablica5[lewy]
#     lewy += 1
#     prawy -= 1
# print(tablica5)

# Zadanie 6.
# Sprawdzanie monotoniczności Wczytaj n (ilosc el. tablicy) i elementy tablicy. Sprawdź, czy tablica jest:
# rosnąca, malejąca, ani taka, ani taka
# Monotoniczność w Pythonie (dla list/ciągów) sprawdza się, weryfikując,
# czy wszystkie elementy są uporządkowane rosnąco lub malejąco
# n6 = random.randint(1,10)
# tablica6 = []
tablica6 = [22, 24, 29, 18, 43]
# print(n6)
# for _ in range(n6):
#     tablica6.append(random.randint(1,100))
# print(tablica6)
#
# tablica_rosnaca = True # Tu ma byc tylko True albo False
# tablica_malejaca = True
#
# element = tablica6[0]
#
# for indeks in range(1, len(tablica6)):
#     if element < tablica6[indeks]:
#         tablica_rosnaca = False
#     elif element > tablica6[indeks]:
#         tablica_malejaca = False
#     element = tablica6[indeks]
#     if not tablica_rosnaca and not tablica_malejaca:
#         break


#
# print(tablica_rosnaca)
# print(tablica_malejaca)
#
# if tablica_rosnaca:
#     print("Funkcja jest rosnaca.")
# elif tablica_malejaca:
#     print("Funkcja jest malejaca.")
# else:
#     print("Funkcja nie jest ani rosnaca ani malejaca.")


# Zadanie 7.
# Szukanie liczby Wypełnij tablicę 15 losowymi liczbami ⟨1, 30⟩. Wczytaj liczbę x.
# Sprawdź, czy x występuje w tablicy i ile razy.

# tablica7 = []
# for liczba in range(15):
#     tablica7.append(random.randint(1, 30))
# print(tablica7)
# try:
#     x = int(input("Wczytaj liczbe z zakresu 1-30: "))
# except ValueError:
#     print("To nie jest liczba, sprobuj ponownie.")
# licznik7 = 0
# for element in tablica7:
#     if element == x:
#         licznik7 += 1
# print(f"Liczba {x} wystepuje {licznik7} razy.")

# TODO: Zadanie 8.
# Tablica bez duplikatów Wypełniaj tablicę losowymi liczbami ⟨1, 20⟩ tak długo, aż wszystkie elementy
# będą różne (użyj while i if).
# tablica8 = []
# rozne_liczby = False
# while not rozne_liczby:
#     nowy = random.randint(1, 20)
#     print(nowy)
#     if nowy not in tablica8:
#         tablica8.append(nowy)
#     else:
#         rozne_liczby = True
# print(tablica8)
# Zadanie 9.
# Liczby pierwsze w tablicy Wypełnij tablicę 20 liczbami losowymi ⟨2, 100⟩.
# Wypisz tylko liczby pierwsze i policz ich ilość.
# tablica9 = []
# for liczba in range(20):
#     tablica9.append(random.randint(2, 100))
# print(tablica9)
# liczby_pierwsze = []
# for element in tablica9:
#     for liczba in range(2, element):
#         if element % liczba == 0:
#             break
#     else:
#         liczby_pierwsze.append(element)
# print(liczby_pierwsze)

# Zadanie 10.
# Menu operacji na tablicy Utwórz tablicę 10 liczb. Wyświetl menu w pętli while:
# 1 – wypełnij losowo
# 2 – wypisz tablicę
# 3 – oblicz sumę
# 4 – znajdź max
# 0 – wyjście.
# Program działa dopóki użytkownik nie wybierze 0.
# Tutaj nie losujesz z gotowej listy, tylko każda liczba jest generowana losowo w podanym zakresie.
# def menu():
#     print("Wybierz operacje do wykonania: ")
#     print("1 – wypełnij losowo")
#     print("2 – wypisz tablice")
#     print("3 – oblicz sumę")
#     print("4 – znajdź max")
#     print("0 – wyjście.")
#     wybor = int(input("Wybor to: "))
#     return wybor

# liczba = menu()
# lista10 = []
# while liczba != 0:
#     if liczba == 1:
#         lista10 = [random.randint(1, 50) for _ in range(10)]
#     elif liczba == 2:
#         print(lista10)
#     elif liczba == 3:
#         suma = sum(lista10)
#         print(suma)
#     elif liczba == 4:
#         print(max(lista10))
#     liczba = menu()

# sortowanie przez wstawianie - znajdujemy najmniejsza liczbe w tablicy i wstawiamy na 1sze mce, nastepnie znajdujemy druga najmniejsza
# i wstawiamy na 2gie mce itd az do konca
# tablica11 = [2, 5, 4, -3, 7, 1]
# min = tablica11[0]
# szybki = 0
# wolny = 0
# while wolny <= len(tablica11) - 1:
#     min = tablica11[0]
#     # print(min)
#     while szybki <= len(tablica11) - 1:
#         if szybki + 1 == len(tablica11):
#             break
#         if min > tablica11[szybki+1]:
#             min = tablica11[szybki+1]
#             # print(min)
#         szybki += 1
#         # print(min)
#     tablica11.append(min)
#     tablica11.remove(min)
#     wolny += 1
#     # print(wolny)
#     szybki = wolny
#     # print(szybki)
#
# print(tablica11)


# tablica11 = [2, 5, 4, -3, 7, 1]
# dl_tablicy = len(tablica11)
# print(tablica11)
# while dl_tablicy > 0:
#     min = tablica11[0]
#     for elem in range(1, dl_tablicy):
#         # print(elem)
#         if min > tablica11[elem]:
#             min = tablica11[elem]
#     tablica11.append(min)
#     # print(tablica11)
#     tablica11.remove(min)
#     print(tablica11)
#     dl_tablicy -= 1

tablica11 = [2, -5, 4, -5, 7, -11]
dl_tablicy = len(tablica11)
print(tablica11)
index = 0
min = tablica11[index] # aktualny najmniejszy element w tablicy
index1 = 0 # indeks pozycji, na ktora wstawiam kolejna najmniejszy element z tablicy
index2 = 0 # indeks pozycji aktualnego najmniejszego elementu
# petla wykonuje sie, dopoki tablica nie zostanie posortowana
while index < dl_tablicy:
   # warunek sprawdza, czy kolejny element jest mniejszy od aktualnie najmniejszego, jesli tak aktualizuje najmniejszy
    if index < dl_tablicy - 1 and min > tablica11[index+1]:
        # min jest wieksza niz tablica11[index+1], dlatego teraz to tablica11[index+1] jest min
        min = tablica11[index+1]
        # index2 przyjmuje pozycje najmniejszego elementu
        index2 = index + 1
    # inkrementujemy za kazdym razem wartosc indexu, czyli sprawdzamy kolejne elementy
    index += 1
    # gdy sprawdzimy wszystkie elementy na liscie zamieniamy element, ktory jest aktualnie minimalny
   # z elementem o najmniejszym indeksie w czesci tablicy, ktora jest nieposortowana
    if index == dl_tablicy:
        # zamieniamy pozycjami element, ktory aktualnie jest minimalny z tym,
        # ktory jest na pozycji, na ktora chcemy go umiescic
        tablica11[index2], tablica11[index1] = tablica11[index1], tablica11[index2]
        print(tablica11)
        # przechodzimy do nastepnej pozycji na liscie
        index1 += 1
        index = index1
        index2 = index1
        # ustawiamy nowe poczatkowe minimum dla kolejnej iteracji
        if index < dl_tablicy:
            min = tablica11[index]