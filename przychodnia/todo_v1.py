# Lista zadań startowo jest pusta
lista_zadan = []

# Funkcja do dodawania zadania
def dodaj_zadanie(lista_zadan, nazwa_zadania):
    """
    Dodaje nowe zadanie do listy, jeśli jeszcze go nie ma.
    """
    # Sprawdzamy, czy zadanie już istnieje
    for zadanie in lista_zadan:
        if zadanie["tytul"] == nazwa_zadania:
            print("Takie zadanie jest już na liście.")
            break
    else:
        # Jeśli nie ma takiego zadania, dodajemy je
        lista_zadan.append({"tytul": nazwa_zadania, "status": "do_zrobienia"})

# Funkcja do wyświetlania zadań
def wyswietl_zadania(lista_zadan):
    """
    Wypisuje wszystkie zadania i ich status.
    Zamienia "_" w statusie na spację dla lepszej czytelności.
    """
    for zadanie in lista_zadan:
        status = zadanie["status"].replace("_", " ")
        print(f'Zadanie "{zadanie["tytul"]}" ma status {status}.')

# Funkcja do oznaczania zadania jako zrobione
def oznacz_zadanie_jako_zrobione(lista_zadan, nazwa_zadania):
    """
    Szuka zadania na liście. Jeśli znajdzie i status jest "do_zrobienia",
    zmienia go na "zrobione". W przeciwnym razie wypisuje odpowiedni komunikat.
    """
    for zadanie in lista_zadan:
        if zadanie["tytul"] == nazwa_zadania:
            if zadanie["status"] == "do_zrobienia":
                zadanie["status"] = "zrobione"
                print(f'Zadanie "{zadanie["tytul"]}" zostało oznaczone jako zrobione.')
            else:
                print(f'Zadanie "{zadanie["tytul"]}" było już zrobione.')
            break
    else:
        # Jeśli pętla for zakończyła się bez break, zadania nie znaleziono
        print("Takiego zadania nie ma na liście.")

# Funkcja do usuwania zadania
def usun_zadanie(lista_zadan, nazwa_zadania):
    """
    Szuka zadania na liście i usuwa je, jeśli istnieje.
    """
    for index in range(len(lista_zadan)):
        if lista_zadan[index]["tytul"] == nazwa_zadania:
            zadanie = lista_zadan.pop(index)
            print(f'Zadanie "{zadanie["tytul"]}" zostało usunięte.')
            break
    else:
        print("Takiego zadania nie ma na liście.")

# Funkcja do wyświetlenia menu
def menu():
    print("\nWybierz zadanie z listy:")
    print("1 → Dodaj zadanie")
    print("2 → Oznacz jako zrobione")
    print("3 → Usuń zadanie")
    print("4 → Wyświetl zadania")
    print("5 → Wyjdź")

# Główna pętla programu
while True:
    menu()
    try:
        wybor = int(input("Twój wybór: "))
    except ValueError:
        print("To nie jest liczba, spróbuj ponownie.")
    else:
        if wybor == 1:
            nazwa_zadania = input("Podaj nazwę zadania: ")
            dodaj_zadanie(lista_zadan, nazwa_zadania)
        elif wybor == 2:
            nazwa_zadania = input("Podaj nazwę zadania: ")
            oznacz_zadanie_jako_zrobione(lista_zadan, nazwa_zadania)
        elif wybor == 3:
            nazwa_zadania = input("Podaj nazwę zadania: ")
            usun_zadanie(lista_zadan, nazwa_zadania)
        elif wybor == 4:
            wyswietl_zadania(lista_zadan)
        elif wybor == 5:
            print("Wychodzisz z listy zadań. Do widzenia!")
            break
        else:
            print("Podałeś błędny numer zadania")


# TODO: to jest smietniczek, jakies wczesniejsze wersje, pewnie sie powielaja z ta powyzej, bo mam ja od chata,
#  nie chcialo mi sie juz polapywac w tym kodzie

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
# def dodaj_zadanie(lista_zadan, nazwa_zadania):
#     for zadanie in lista_zadan:
#         if zadanie["tytul"] == nazwa_zadania:
#             print("Takie zadanie jest juz na liscie.")
#             break
#     else:
#         lista_zadan.append({"tytul": nazwa_zadania, "status": "do_zrobienia"})

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

# def usun_zadanie(lista_zadan, nazwa_zadania):
#     for index in range(len(lista_zadan)):
#         if lista_zadan[index]["tytul"] == nazwa_zadania:
#             lista_zadan.pop(index)
#             break
#     else:
#         print("Takiego zadania nie ma na liście.")

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
# dodaj_zadanie(lista_zadan, "kup mleko")
# dodaj_zadanie(lista_zadan, "napisz raport")
# wyswietl_zadania(lista_zadan)
# # # oznacz_zadanie_jako_zrobione(lista, "kup mleko")
# oznacz_zadanie_jako_zrobione(lista_zadan, "Nauczyć się Pythona")
# oznacz_zadanie_jako_zrobione(lista_zadan, "Napisać raport")
# oznacz_zadanie_jako_zrobione(lista_zadan, "Nieistniejące zadanie")
# usun_zadanie(lista_zadan, "napisz raport")
# wyswietl_zadania(lista_zadan)