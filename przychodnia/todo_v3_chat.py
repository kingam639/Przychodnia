# =========================
#        TODO APP v2
# =========================

# Lista zadań startowo jest pusta
lista_zadan = []


def wpisz_zadanie():
    """Pobiera od użytkownika nazwę zadania."""
    return input("Podaj nazwę zadania: ")


def znajdz_zadanie(lista_zadan, nazwa_zadania):
    """Zwraca słownik zadania, jeśli istnieje. W przeciwnym razie None."""
    for zadanie in lista_zadan:
        if zadanie["tytul"] == nazwa_zadania:
            return zadanie
    return None


def dodaj_zadanie(lista_zadan, nazwa_zadania):
    """Dodaje zadanie, jeśli nie istnieje na liście."""
    if znajdz_zadanie(lista_zadan, nazwa_zadania):
        print("Takie zadanie jest już na liście.")
    else:
        lista_zadan.append({"tytul": nazwa_zadania, "status": "do_zrobienia"})
        print("Zadanie zostało dodane.")


def wyswietl_zadania(lista_zadan):
    """Wypisuje wszystkie zadania i ich status. Zamienia "_" w statusie na spację dla lepszej czytelności."""
    # nie mialam tego pierwszego warunku, ale wlasnie to jest potrzebne, bo bez sensu byloby, gdyby ktos chcial, zeby
    # wyswietlilo zadania, wywolal te funkcje i nic sie nie dzialo, ten if zabezpiecza przed tym
    if not lista_zadan:
        print("Lista zadań jest pusta.")
        return

    for index, zadanie in enumerate(lista_zadan, start=1):
        status = zadanie["status"].replace("_", " ")
        print(f"{index}. {zadanie['tytul']} → {status}")


def oznacz_zadanie_jako_zrobione(lista_zadan, nazwa_zadania):
    """Oznacza zadanie jako zrobione, jeśli istnieje."""
    zadanie = znajdz_zadanie(lista_zadan, nazwa_zadania)
    # ja mialam ifa zagniezdzonego w elsie, czyli dopiero jak zadanie bylo na liscie, to sprawdzalo, jaki ma status
    # tu jest bardziej plasko, wiec jest lepsza czytelnosc
    if not zadanie:
        print("Takiego zadania nie ma na liście.")
    elif zadanie["status"] == "do_zrobienia":
        zadanie["status"] = "zrobione"
        print("Zadanie zostało oznaczone jako zrobione.")
    else:
        print("To zadanie było już zrobione.")


def usun_zadanie(lista_zadan, nazwa_zadania):
    """Usuwa zadanie z listy, jeśli istnieje."""
    zadanie = znajdz_zadanie(lista_zadan, nazwa_zadania)

    if not zadanie:
        print("Takiego zadania nie ma na liście.")
    else:
        lista_zadan.remove(zadanie)
        print("Zadanie zostało usunięte.")

def zapisz_do_pliku(lista_zadan):
    """Zapisuje zadania do pliku txt."""
    # "w"(write): tworzy / nadpisuje plik
    with open("zadania.txt", "w") as plik:
        for zadanie in lista_zadan:
            plik.write(f"{zadanie['tytul']} | {zadanie['status']}\n")


lista = [
    {"tytul": "Nauczyć się Pythona", "status": "do_zrobienia"},
    {"tytul": "Napisać raport", "status": "zrobione"},
    {"tytul": "Posprzątać pokój", "status": "do_zrobienia"},
    ]

zapisz_do_pliku(lista)

# def menu():
#     print("\n=== MENU ===")
#     print("1 → Dodaj zadanie")
#     print("2 → Oznacz jako zrobione")
#     print("3 → Usuń zadanie")
#     print("4 → Wyświetl zadania")
#     print("5 → Wyjdź")
#
#
# # Słownik opcji:
# # klucz = numer z menu
# # wartość = (funkcja, czy_wymaga_nazwy_zadania)
# opcje = {
#     1: (dodaj_zadanie, True),
#     2: (oznacz_zadanie_jako_zrobione, True),
#     3: (usun_zadanie, True),
#     4: (wyswietl_zadania, False),
# }
#
#
# # Główna pętla programu
# uzywam_listy_zadan = True
#
# while uzywam_listy_zadan:
#     menu()
#
#     try:
#         wybor = int(input("Twój wybór: "))
#     except ValueError:
#         print("To nie jest liczba, spróbuj ponownie.")
#         # nie podano liczby, continue powoduje ze python wraca na poczatek petli while
#         continue
#
#     if wybor == 5:
#         print("Do zobaczenia!")
#         # uzytkownik podal 5, flaga uzywam_listy_zadan zmieni wartosc na False, co konczy dzialanie petli while
#         uzywam_listy_zadan = False
#
#     elif wybor in opcje:
#         # rozpakowywanie krotki
#         funkcja, wymaga_nazwy = opcje[wybor]
#         # jesli wymaga nazwy ma wartosc True if wywoluje funkcje wpisz_zadanie
#         if wymaga_nazwy:
#             nazwa = wpisz_zadanie()
#             funkcja(lista_zadan, nazwa)
#         else:
#             funkcja(lista_zadan)
#     # podano liczbe poza zakresem z menu
#     else:
#         print("Podałeś błędny numer.")
#
#
# if not zadanie:
#     print("Takiego zadania nie ma na liscie.")
# else:
#     if zadanie["status"] == "do_zrobienia":
#         zadanie["status"] = "zrobione"
#         print("Zadanie zostało oznaczone jako zrobione.")
#     else:
#         print("To zadanie  jest juz zrobione")