# 🧩 Zadanie: System rezerwacji wizyt w przychodni
# Opis ogólny
# Tworzysz prosty system do zarządzania wizytami lekarskimi.
# Dane są przechowywane w liście słowników.
# Każda akcja użytkownika wywołuje funkcję główną, która korzysta z kilku funkcji pomocniczych.

# 📦 Dane startowe

lekarze = [
    {
        "id": 1,
        "imie": "Anna",
        "specjalizacja": "internista",
        "dostepne_godziny": [9, 10, 11]
    },
    {
        "id": 2,
        "imie": "Piotr",
        "specjalizacja": "dermatolog",
        "dostepne_godziny": [12, 13, 14]
    },
{
        "id": 3,
        "imie": "Hanna",
        "specjalizacja": "internista",
        "dostepne_godziny": [9, 10, 12]
    },
]
pacjenci = [
    {
        "id": 1,
        "imie": "Jan",
        "zajete_godziny": []
    },
    {
        "id": 2,
        "imie": "Malgosia",
        "zajete_godziny": []
    },
    {
        "id": 3,
        "imie": "Stas",
        "zajete_godziny": []
    },
]
print(pacjenci[0]["imie"])
wizyty = []

# 🎯 Wymagane funkcje (KLUCZOWE)
#
# 1️⃣ czy_lekarz_istnieje(lekarze, lekarz_id)
# Sprawdza, czy lekarz o podanym id istnieje
# Zwraca True / False

def czy_lekarz_istnieje(lekarze, lekarz_id):
    for lekarz in lekarze:
        if lekarz["id"] == lekarz_id:
            return True
    return False

# print(czy_lekarz_istnieje(lekarze, 5))

# 2️⃣ czy_godzina_dostepna(lekarze, lekarz_id, godzina)
# Sprawdza, czy dana godzina jest dostępna u lekarza
# Korzysta z czy_lekarz_istnieje
# Zwraca True / False

def czy_godzina_dostepna(lekarze, lekarz_id, godzina):
    if czy_lekarz_istnieje(lekarze, lekarz_id):   # zwroci None, jesli czy_lekarz_istnieje jest False
        if godzina in lekarze[lekarz_id-1]["dostepne_godziny"]: # zakladamy, ze lekarze sa ulozenie w slowniku lekarze
            # w kolejnosci rosnacego id, a lekarze to lista slownikow, wiec ten o id=1 bedzie mial indeks listy=0
            return True # lekarz istnieje i godzina dostepna
        return False # lekarz istnieje, ale godzina niedostepna
    return None # lekarz nie istnieje
# print(czy_godzina_dostepna(lekarze, 2, 9))
# print(czy_godzina_dostepna(lekarze, 2, 13))
# print(czy_godzina_dostepna(lekarze, 1, 10))
# print(czy_godzina_dostepna(lekarze, 1, 14))

# 3️⃣ zarezerwuj_godzine(lekarze, lekarz_id, godzina)
# Usuwa godzinę z listy dostepne_godziny
# Zakładamy, że godzina jest poprawna
# Nic nie zwraca
def zarezerwuj_godzine(lekarze, lekarz_id, godzina):
    # jesli lekarz o danym id ma dostepna godzine, to wowczas mozna ja zarezerwowac, czyli usunac z listy
    # dostepnych godzin
    if czy_godzina_dostepna(lekarze, lekarz_id, godzina):
        lekarze[lekarz_id-1]["dostepne_godziny"].remove(godzina)


# print(zarezerwuj_godzine(lekarze, 1, 9))

# 4️⃣ dodaj_wizyte(wizyty, pacjent, lekarz_id, godzina)
# Dodaje słownik wizyty do listy wizyty
# {
#     "pacjent": "Jan",
#     "lekarz_id": 1,
#     "godzina": 10
# }
def dodaj_wizyte(wizyty, pacjent_id, lekarz_id, godzina):
    wizyty.append({
     "pacjent_id": pacjent_id,
     "lekarz_id": lekarz_id,
     "godzina": godzina
    })
    # tu chyba powinien tez dodac wizyte do zajete_godziny na liscie slownikow pacjenci
    pacjenci[pacjent_id-1]["zajete_godziny"].append(godzina)
# dodaj_wizyte(wizyty, pacjent="Jan", lekarz_id=1, godzina=10)
# print(wizyty)

# ⭐ Rozszerzenia (opcjonalne – świetne na kolejne zajęcia)
# funkcja wyswietl_wizyty(wizyty)
# funkcja odwolaj_wizyte(...)
# sprawdzanie, czy pacjent nie ma już wizyty o tej godzinie - baza pacjentow, dodatkowe spr,zeby pacjent nie mogl sie
# umowic do 2 lekarzy na te sama godzine
# wyszukiwanie lekarzy po specjalizacji - umow wizyte do konkretnego lekarza lub do pierwszego wolnego specjalisty
# o tej specjalizacji

def wyswietl_wizyty(wizyty):
    for wizyta in wizyty:
        # pacjenci[wizyta["pacjent_id"]-1]] - tu dostaje sie do slownika pacjenta, ktory ma wizyte, tak samo, jak przy
        # lekarzach
        # TODO: czy tu nie musze tez jako argument dawac listy slownikow pacjenci?
        print(f"Pacjent {pacjenci[wizyta["pacjent_id"]-1]["imie"]} ma wizyte u lekarza o godzinie {wizyta["godzina"]}.")

def odwolaj_wizyte(wizyty, lekarz_id, godzina):
    for wizyta in wizyty:
        if wizyta["godzina"] == godzina:
            wizyty.remove(wizyta) # usuwa cala wizyte
            pacjenci[wizyta["pacjent_id"]-1]["zajete_godziny"].remove(godzina) # usuwa godzine wizyty z listy
            # zajete_godziny w slowniku pacjenta (z listy slownikow pacjenci)
            lekarze[lekarz_id-1]["dostepne_godziny"].append(godzina) # lekarzowi zwalnia sie godzina wizyty

# sprawdzanie, czy pacjent nie ma już wizyty o tej godzinie - baza pacjentow, dodatkowe spr,zeby pacjent nie mogl sie
# umowic do 2 lekarzy na te sama godzine
# wizyta = {'pacjent': 'Jan', 'lekarz_id': 1, 'godzina': 10}
def czy_jest_wizyta(wizyty, pacjent_id, godzina):
    for wizyta in wizyty:
        if wizyta["pacjent_id"] == pacjent_id and wizyta["godzina"] == godzina:
            return True
    return False

def czy_godzina_wolna_pacjent(pacjenci, pacjent_id, godzina):
    if godzina in pacjenci[pacjent_id-1]["zajete_godziny"]:
        return False
    return True

def czy_jest_specjalizacja(lekarze, specjalizacja):
    # TODO: cz ta funkcja jest potrzebna (zmienilam nazwe, to byla znajdz specjalizacje)# ?
    for lekarz in lekarze:
        if lekarz["specjalizacja"] == specjalizacja:
            return True
    return False

def znajdz_specjalizacje(lekarze, lekarz_id):
    # zwraca specjalizacje lekarza o danym id
    specjalizacja = lekarze[lekarz_id-1]["specjalizacja"]
    return specjalizacja

# print(znajdz_specjalizacje(lekarze, 1))

def wybierz_specjaliste(lekarze, lekarz_id):
    # lekarz_id to bedzie ten ktorego nie chce juz brac pod uwage....
    # przeszukuje reszte lekarzy i wtedy wybieram tego o tej specjalizacji, ktorej szukam i zwracam jego id
    for lekarz in lekarze:
        if lekarz["id"] != lekarz_id and znajdz_specjalizacje(lekarze, lekarz_id):
            return lekarz["id"]

# 5️⃣ umow_wizyte(lekarze, wizyty, pacjent, lekarz_id, godzina)
# 🔥 FUNKCJA GŁÓWNA
# Ta funkcja:
# Sprawdza, czy lekarz istnieje
# Sprawdza, czy godzina jest dostępna
# Rezerwuje godzinę
# Dodaje wizytę
# Wypisuje komunikat:
# „Wizyta umówiona”
# albo „Nie można umówić wizyty”
# 👉 MUSI wywoływać inne funkcje

def umow_wizyte(lekarze, wizyty, pacjent_id, lekarz_id, godzina):
    lekarz = czy_lekarz_istnieje(lekarze, lekarz_id)
    godzina_wizyty = czy_godzina_dostepna(lekarze, lekarz_id, godzina)
    brak_lekarza = True
    if lekarz and godzina_wizyty:
        zarezerwuj_godzine(lekarze, lekarz_id, godzina)
        dodaj_wizyte(wizyty, pacjent_id, lekarz_id, godzina)
        print("Wizyta umówiona")
    # jesli nie ma takiego lekarza, mozna wtedy znalezc innego specjaliste
    else:
        id_innego_lekarza = None
        while id_innego_lekarza != lekarz_id:
            id_innego_lekarza = wybierz_specjaliste(lekarze, lekarz_id)
            umow_wizyte(lekarze, wizyty, pacjent_id, id_innego_lekarza, godzina)
        else:
            print("Nie mozna umowic wizyty")

# 🧠 Ograniczenia (ważne dydaktycznie)
# ❌ brak input()
# ❌ brak klas
# ❌ brak break i continue
# ✔️ tylko funkcje
# ✔️ listy i słowniki
# ✔️ logika oparta o wartości zwracane z funkcji

# ▶️ Przykładowe użycie (do testów)
umow_wizyte(lekarze, wizyty, 1, 1, 10)
print(wizyty)
print(pacjenci)
# odwolaj_wizyte(wizyty,1, 10)
print(pacjenci)
umow_wizyte(lekarze, wizyty, 2, 1, 10)
print(wizyty)
# umow_wizyte(lekarze, wizyty, 3, 2, 14)
print(wizyty)
# umow_wizyte(lekarze, wizyty, 3, 1, 10)
print(wizyty)
wyswietl_wizyty(wizyty)

