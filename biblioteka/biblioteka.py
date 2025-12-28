# Zadanie: Mini-system biblioteki
# Masz napisać kilka prostych funkcji i użyć ich wewnątrz innych funkcji.
# Opis:
# Tworzysz bardzo uproszczony system biblioteki. Biblioteka przechowuje listę książek (same tytuły jako stringi).
# Cel zadania:
# nauczyć się dzielić logikę na małe funkcje
# zobaczyć, że funkcje mogą wywoływać inne funkcje
# unikać powtarzania kodu

biblioteka_ksiazek = []
wypozyczane_ksiazki = ["pan tadeusz", "Pan Samochodzik"]

# TODO: 1. Napisz funkcję dodaj_ksiazke(biblioteka, tytul)
# przyjmuje listę książek i tytuł
# dodaje książkę do listy
# nic nie zwraca
def dodaj_ksiazke(biblioteka, tytul):
    biblioteka.append(tytul)

# TODO: 2. Napisz funkcję czy_jest_ksiazka(biblioteka, tytul)
#  zwraca True, jeśli książka jest w bibliotece
#  w przeciwnym razie False
def czy_jest_ksiazka(biblioteka, tytul):
    return tytul in biblioteka

# TODO: 3. Napisz funkcję usun_ksiazke(biblioteka, tytul)
# używa funkcji czy_jest_ksiazka
# jeśli książka istnieje → usuwa ją i wypisuje "Usunięto książkę"
# jeśli nie → wypisuje "Brak takiej książki"
def usun_ksiazke(biblioteka, tytul):
    if czy_jest_ksiazka(biblioteka, tytul):
        biblioteka.remove(tytul)
    #     print("Usunieto ksiazke.")
    # else:
    #     print("Brak takiej ksiazki.")

# TODO:     4. Napisz funkcję wypozycz_ksiazke(biblioteka, tytul)
# używa funkcji usun_ksiazke
# symuluje wypożyczenie książki
# komentarz testowy
def wypozycz_ksiazke(biblioteka, tytul):
    usun_ksiazke(biblioteka, tytul)

# TODO: 5. Napisz funkcję obsluz_biblioteke()
# tworzy pustą listę  ukhih
# dodaje kilka książek
# próbuje wypożyczyć jedną istniejącą i jedną nieistniejącą
def obsluz_biblioteke():
    biblioteka = []
    dodaje = True
    while dodaje:
        tytul = input("Wpisz tytul ksiazki, ktora chcesz dodac, wpisz 'nie', by zakonczyc dodawanie ksiazek: ")
        if tytul == "nie":
            dodaje = False
        else:
            dodaj_ksiazke(biblioteka, tytul)
    wypozyczam = True
    while wypozyczam:
        tytul = input("Wpisz tytul ksiazki, ktora chcesz wypozyczyc, wpisz 'nie', by zakonczyc wypozyczanie ksiazek: ")
        if tytul == "nie":
            wypozyczam = False
        elif wypozycz_ksiazke(biblioteka, tytul):
            print(f"Wypozyczyles ksiazke {tytul}")
        else:
            print("Nie ma takiej ksiazki.")

# usun_ksiazke(wypozyczane_ksiazki, "abc")
obsluz_biblioteke()