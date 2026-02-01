# 🧩 Zadanie: Wypożyczalnia książek
# Opis:
# Jest lista książek
# Każda książka może być dostępna albo wypożyczona
# Użytkownik chce wypożyczyć konkretną książkę
# Program ma:
# wypożyczyć książkę jeśli jest dostępna
# albo wypisać komunikat, że nie można wypożyczyć
from os import remove


# Po tej poprawce logika wygląda tak:
# 1️⃣ Program ma listę książek
# 2️⃣ Program dostaje tytuł książki do wypożyczenia
# 3️⃣ Sprawdza, czy taka książka istnieje
# 4️⃣ Jeśli istnieje i jest dostępna → wypożycza
# 5️⃣ W przeciwnym razie → wypisuje komunikat
#
# def wypozycz_ksiazke(lista_ksiazek, tytul):
#     if not czy_ksiazka_istnieje(lista_ksiazek, tytul):
#         print("Ksiazka nie istnieje")
#     elif not czy_ksiazka_dostepna(lista_ksiazek, tytul):
#             print("ksiazka jest wypozyczona")
#     else:
#         for ksiazka in lista_ksiazek:
#             if ksiazka["tytul"] == tytul:
#                 ksiazka["status"] = "wypozyczona"
#
# def oddaj_ksiazke(lista_ksiazek, tytul):
#     if not czy_ksiazka_istnieje(lista_ksiazek, tytul):
#         print("Ksiazka nie istnieje")
#     elif czy_ksiazka_dostepna(lista_ksiazek, tytul):
#         print("Taka ksiazka nie zostala wypozyczona")
#     else:
#         for ksiazka in lista_ksiazek:
#             if ksiazka["tytul"] == tytul and ksiazka["status"] == "wypozyczona":
#                 ksiazka["status"] = "dostepna"
#                 print("Oddales ksiazke")
#
#
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

def dodaj_zadanie(lista_zadan, nazwa_zadania):
    for zadanie in lista_zadan:
        if zadanie["tytul"] == nazwa_zadania:
            print("Takie zadanie jest juz na liscie.")
            break
    else:
        lista_zadan.append({"tytul": nazwa_zadania, "status": "do_zrobienia"})

def wyswietl_zadania(lista_zadan):
    for zadanie in lista_zadan:
        status = zadanie["status"].replace("_", " ")
        print(f'Zadanie {zadanie["tytul"]} ma status {status}.')

def oznacz_zadanie_jako_zrobione(lista_zadan, nazwa_zadania):
    for zadanie in lista_zadan:
        if zadanie["tytul"] == nazwa_zadania:
            if zadanie["status"] == "do_zrobienia":
                zadanie["status"] = "zrobione"
                print("Zadanie zostało oznaczone jako zrobione.")
            else:
                print("To zadanie zostało już zrobione.")
            break
        # break
    else:
        print("Takiego zadania nie ma na liście.")

def znajdz_zadanie(lista_zadan, nazwa_zadania):
    for zadanie in lista_zadan:
        if zadanie["tytul"] == nazwa_zadania:
            return zadanie
    else:
         return None

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


def usun_zadanie(lista_zadan, nazwa_zadania):
    for index in range(len(lista_zadan)):
        if lista_zadan[index]["tytul"] == nazwa_zadania:
            lista_zadan.pop(index)
            break
    else:
        print("Takiego zadania nie ma na liście.")

def usun_zadanie(lista_zadan, nazwa_zadania):
    zadanie = znajdz_zadanie(lista_zadan, nazwa_zadania)
    if not zadanie:
        print("Takiego zadania nie ma na liście.")
    else:
        lista_zadan.remove(zadanie)
        print(f"Zadanie {zadanie["tytul"]} zostalo usuniete.")
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

dodaj_zadanie(lista, "kup mleko")
dodaj_zadanie(lista, "napisz raport")
wyswietl_zadania(lista)
oznacz_zadanie_jako_zrobione(lista, "kup mleko")
usun_zadanie(lista, "napisz raport")
wyswietl_zadania(lista)
