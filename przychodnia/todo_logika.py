# def czy_zadanie_istnieje(lista_zadan, nazwa_zadania):
#     for zadanie in lista_zadan:
#         if zadanie["tytul"] == nazwa_zadania:
#             return True
#     else:
#         return False
#
# def czy_zadanie_zrobione(lista_zadan, nazwa_zadania):
#     # tu wstaw pętlę i warunek
#     if not czy_zadanie_istnieje(lista_zadan, nazwa_zadania):
#         pass
#         # zadania nie ma na liscie zadan
#     else:
#         for zadanie in lista_zadan:
#             if zadanie["status"] == "zrobione":
#                 return True
#         else:
#             return False
#
# def czy_zadanie_zrobione(lista_zadan, nazwa_zadania):
#     for zadanie in lista_zadan:
#         if zadanie["tytul"] == nazwa_zadania and zadanie["status"] == "zrobione":
#             return True
#     return False
#
# # Logika funkcji oznacz_zadanie_jako_zrobione
# # Rozbijamy na punkty (tylko logika, nie kod):
# # 1️⃣ Najpierw przechodzi po liście zadań i sprawdza, czy zadanie o podanym tytule istnieje
# # 2️⃣ Jeśli nie istnieje → wypisuje komunikat: "Takiego zadania nie ma na liście"
# # 3️⃣ Jeśli istnieje, sprawdza, czy status to "do_zrobienia"
# # 4️⃣ Jeśli status jest inny (czyli "zrobione") → wypisuje komunikat: "To zadanie zostało już zrobione"
# # 5️⃣ Jeśli status to "do_zrobienia" → zmienia status na "zrobione" i wypisuje: "Zadanie zostało oznaczone jako zrobione"

# def oznacz_zadanie_jako_zrobione(lista_zadan, nazwa_zadania):
#     for zadanie in lista_zadan:
#         if zadanie["tytul"] == nazwa_zadania:
#             if zadanie["status"] == "do_zrobienia":
#                 zadanie["status"] = "zrobione"
#                 print("Zadanie zostało oznaczone jako zrobione")
#             else:
#                 print("To zadanie zostało już zrobione")
#             break
#     else:
#         print("Takiego zadania nie ma na liście")
#
# # przejdź po liście
# # jeśli znajdziesz zadanie o tym tytule → usuń je z listy
# # przerwij pętlę
# # jeśli nie znajdziesz → wypisz komunikat
#
# def usun_zadanie(lista_zadan, nazwa_zadania):
#     # for zadanie in lista_zadan:
#     #     if zadanie["tytul"] == nazwa_zadania:
#     for index in range(len(lista_zadan)):
#         if lista_zadan[index]["tytul"] == nazwa_zadania:
#             lista_zadan.remove(lista_zadan[index])
#             break
#     else:
#         print("Takiego zadania nie ma na liście")

# lista_zadan = [
#     {"tytul": "Nauczyć się Pythona", "status": "do_zrobienia"},
#     {"tytul": "Napisać raport", "status": "zrobione"},
#     {"tytul": "Posprzątać pokój", "status": "do_zrobienia"},
# ]

def znajdz_zadanie(lista_zadan, nazwa_zadania):
    for zadanie in lista_zadan:
        if zadanie["tytul"] == nazwa_zadania:
            return zadanie
    else:
         return None

def dodaj_zadanie(lista_zadan, nazwa_zadania):
    zadanie = znajdz_zadanie(lista_zadan, nazwa_zadania)
    if not zadanie:
        lista_zadan.append({"tytul": nazwa_zadania, "status": "do_zrobienia"})
    else:
        print("Takie zadanie jest juz na liscie.")

# def dodaj_zadanie(lista_zadan, nazwa_zadania):
#     for zadanie in lista_zadan:
#         if zadanie["tytul"] == nazwa_zadania:
#             print("Takie zadanie jest juz na liscie.")
#             break
#     else:
#         lista_zadan.append({"tytul": nazwa_zadania, "status": "do_zrobienia"})

def wyswietl_zadania(lista_zadan):
    for zadanie in lista_zadan:
        status = zadanie["status"].replace("_", " ")
        print(f'Zadanie {zadanie["tytul"]} ma status {status}.')

# def oznacz_zadanie_jako_zrobione(lista_zadan, nazwa_zadania):
#     for zadanie in lista_zadan:
#         if zadanie["tytul"] == nazwa_zadania:
#             if zadanie["status"] == "do_zrobienia":
#                 zadanie["status"] = "zrobione"
#                 print("Zadanie zostało oznaczone jako zrobione.")
#             else:
#                 print("To zadanie zostało już zrobione.")
#             break
#     else:
#         print("Takiego zadania nie ma na liście.")

def oznacz_zadanie_jako_zrobione(lista_zadan, nazwa_zadania):
    zadanie = znajdz_zadanie(lista_zadan, nazwa_zadania)
    if not zadanie:
        print("Takiego zadania nie ma na liście.")
    else:
        if zadanie["status"] == "do_zrobienia":
            zadanie["status"] = "zrobione"
            print("Zadanie zostało oznaczone jako zrobione.")
        else:
            print("To zadanie zostało już zrobione.")

# def usun_zadanie(lista_zadan, nazwa_zadania):
#     for index in range(len(lista_zadan)):
#         if lista_zadan[index]["tytul"] == nazwa_zadania:
#             lista_zadan.pop(index)
#             break
#     else:
#         print("Takiego zadania nie ma na liście.")

def usun_zadanie(lista_zadan, nazwa_zadania):
    zadanie = znajdz_zadanie(lista_zadan, nazwa_zadania)
    if not zadanie:
        print("Takiego zadania nie ma na liście.")
    else:
        lista_zadan.remove(zadanie)
        print(f"Zadanie {zadanie['tytul']} zostalo usuniete.")

def wpisz_zadanie():
    zadanie = input("Podaj nazwe zadania: ")
    return zadanie
#
# def usun_zadanie(lista_zadan, nazwa_zadania):
#     for zadanie in lista_zadan:
#         if zadanie["tytul"] == nazwa_zadania:
#             lista_zadan.remove(zadanie)
#             break
#     else:
#         print("Takiego zadania nie ma na liście.")

# dodaj_zadanie(lista_zadan, "Zmierzyc miejsce na szafe.")
# print(lista_zadan)
# wyswietl_zadania(lista_zadan)
# nazwa_zadania_1 = "Zmierzyc miejsce na szafe."
# nazwa_zadania_2 = "Zrobic obiad."
# oznacz_zadanie_jako_zrobione(lista_zadan, nazwa_zadania_1)
# oznacz_zadanie_jako_zrobione(lista_zadan, nazwa_zadania_2)
# print(lista_zadan)

lista = []

# dodaj_zadanie(lista_zadan, "kup mleko")
# dodaj_zadanie(lista_zadan, "napisz raport")
# wyswietl_zadania(lista_zadan)
# # # oznacz_zadanie_jako_zrobione(lista, "kup mleko")
# oznacz_zadanie_jako_zrobione(lista_zadan, "Nauczyć się Pythona")
# oznacz_zadanie_jako_zrobione(lista_zadan, "Napisać raport")
# oznacz_zadanie_jako_zrobione(lista_zadan, "Nieistniejące zadanie")
# usun_zadanie(lista_zadan, "napisz raport")
# wyswietl_zadania(lista_zadan)

# Zróbmy teraz mini-aplikację TODO z menu, żeby połączyć wszystkie funkcje w interaktywnym programie.
# 1️⃣ Tworzymy pustą listę zadań na start:

# 2️⃣ Robimy pętlę while True, która wyświetla menu:
# 1 → Dodaj zadanie
# 2 → Oznacz jako zrobione
# 3 → Usuń zadanie
# 4 → Wyświetl zadania
# 5 → Wyjdź
# 3️⃣ Pobieramy wybór użytkownika (input) i wywołujemy odpowiednią funkcję.
# 4️⃣ Jeśli użytkownik wybierze 5 → przerywamy pętlę (break).

lista_zadan = []
opcje = {
    1: dodaj_zadanie,
    2: oznacz_zadanie_jako_zrobione,
    3: usun_zadanie,
    4: wyswietl_zadania
}
def menu():
    print("Wybierz zadanie z listy:")
    print("1 → Dodaj zadanie")
    print("2 → Oznacz jako zrobione")
    print("3 → Usuń zadanie")
    print("4 → Wyświetl zadania")
    print("5 → Wyjdź")

while True:
    menu()
    try:
        wybor = int(input())
    except ValueError:
        print("To nie jest liczba, sprobuj ponownie.")
    else:
        if wybor in opcje:
            if wybor <= 3:
                nazwa_zadania = wpisz_zadanie()
                opcje[wybor](lista_zadan, nazwa_zadania)
            elif wybor == 4:
                opcje[wybor](lista_zadan)
            else:
                break
        else:
            print("Podales bledny numer zadania")

# 1️⃣ Dodawanie zadania które nie istnieje
dodaj_zadanie(lista_zadan, "Kupić mleko")  # powinno dodać

# 2️⃣ Dodawanie zadania które już istnieje
dodaj_zadanie(lista_zadan, "Nauczyć się Pythona")  # powinno wypisać komunikat

# 3️⃣ Oznaczenie zadania jako zrobione (status 'do_zrobienia')
oznacz_zadanie_jako_zrobione(lista_zadan, "Nauczyć się Pythona")  # zmienia status

# 4️⃣ Oznaczenie zadania, które już jest zrobione
oznacz_zadanie_jako_zrobione(lista_zadan, "Napisać raport")  # komunikat, że już zrobione

# 5️⃣ Oznaczenie nieistniejącego zadania
oznacz_zadanie_jako_zrobione(lista_zadan, "Nieistniejące zadanie")  # komunikat brak zadania

# 6️⃣ Usuwanie zadania które istnieje
usun_zadanie(lista_zadan, "Posprzątać pokój")  # powinno usunąć

# 7️⃣ Usuwanie zadania które nie istnieje
usun_zadanie(lista_zadan, "Nieistniejące zadanie")  # komunikat brak zadania

# 8️⃣ Wyświetlenie wszystkich zadań
wyswietl_zadania(lista_zadan)

# Zadanie
# 1️⃣ Przejdź pętlą for po wszystkich liczbach.
# 2️⃣ Sprawdź if – czy liczba jest podzielna przez 3.
# 3️⃣ Jeśli znajdziesz taką liczbę → wypisz "Znalazłem liczbę podzielną przez 3!" i przerwij pętlę.
# 4️⃣ Jeśli pętla przeszła całą listę i nic nie znalazła → wypisz "Nie znalazłem liczby podzielnej przez 3." używając else.

# liczby = [1, 3, 5, 7, 9]
#
# for liczba in liczby:
#     if liczba % 3 == 0:
#         print("Znalazłem liczbę podzielną przez 3!")
#         break
# else:
#     print("Nie znalazłem liczby podzielnej przez 3.")




