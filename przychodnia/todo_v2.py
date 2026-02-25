def wpisz_zadanie():
    """Funkcja prosi uzytkownika o wpisanie zadania, ktore ma zostac dodane do listy."""
    zadanie = input("Podaj nazwe zadania: ")
    return zadanie

def znajdz_zadanie(lista_zadan, nazwa_zadania):
    """Funkcja sprawdza, czy zadanie jest na liscie, a jesli zadania nie ma na liscie, zwraca None."""
    for zadanie in lista_zadan:
        if zadanie["tytul"] == nazwa_zadania:
            return zadanie
    else:
         return None

def dodaj_zadanie(lista_zadan, nazwa_zadania):
    """Funkcja dodaje zadanie do listy zadan, jesli nie ma go jeszcze na liscie."""
    zadanie = znajdz_zadanie(lista_zadan, nazwa_zadania)
    if not zadanie:
        lista_zadan.append({"tytul": nazwa_zadania, "status": "do_zrobienia"})
    else:
        print("Takie zadanie jest juz na liscie.")

def wyswietl_zadania(lista_zadan):
    """Funkcja wyswietla zadania, ktore sa na liscie."""
    for zadanie in lista_zadan:
        status = zadanie["status"].replace("_", " ")
        print(f'Zadanie {zadanie["tytul"]} ma status {status}.')

def oznacz_zadanie_jako_zrobione(lista_zadan, nazwa_zadania):
    """Funkcja sprawdza, czy zadanie jest na liscie i czy ma status do_zrobienia, wowczas zmienia status na zrobione."""
    zadanie = znajdz_zadanie(lista_zadan, nazwa_zadania)
    # sprawd
    if not zadanie:
        print("Takiego zadania nie ma na liście.")
    elif zadanie["status"] == "do_zrobienia":
        zadanie["status"] = "zrobione"
        print(f'Zadanie {zadanie["tytul"]} zostało oznaczone jako zrobione.')
    else:
        print(f'Zadanie {zadanie["tytul"]} zostało już zrobione.')

def usun_zadanie(lista_zadan, nazwa_zadania):
    """Funkcja sprawdza, czy zadanie jest na liscie i wowczas je usuwa z listy."""
    zadanie = znajdz_zadanie(lista_zadan, nazwa_zadania)
    if not zadanie:
        print("Takiego zadania nie ma na liście.")
    else:
        lista_zadan.remove(zadanie)
        print(f"Zadanie {zadanie['tytul']} zostalo usuniete.")

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
# zmienna opcje to slownik, ktory do kazdego klucza ma przypisana krotke z referencja do funkcji i wartoscia True, gdy
# funkcja potrzebuje argumentu nazwa_zadania, lub False, gdy funckja tego argumentu nie potrzebuje
opcje = {
    1: (dodaj_zadanie, True),
    2: (oznacz_zadanie_jako_zrobione, True),
    3: (usun_zadanie, True),
    4: (wyswietl_zadania, False)
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
        wybor = int(input("Twoj wybor to: "))
    except ValueError:
        print("To nie jest liczba, sprobuj ponownie.")
        # jesli uzytkownik wpisal cos innego niz liczba, continue spowoduje powrot petli while do poczatku
    if wybor in opcje:
        # przypisanie krotki do dwoch zmiennych
        if funkcja, nazwa_zadania = opcje[wybor]:
                nazwa_zadania = wpisz_zadanie()
                opcje[wybor](lista_zadan, nazwa_zadania)
            elif wybor == 4:
                opcje[wybor](lista_zadan)
        elif wybor == 5:
            print("Wychodzisz z listy.")
            break
        else:
            print("Podales bledny numer zadania")

# to sa pomocnicze funkcje, wykorzystywalam je do testow zanim zrobilam menu

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


