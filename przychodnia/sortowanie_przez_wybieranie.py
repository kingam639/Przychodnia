def indeks_najmniejszej_wartosci(lista):
    print(lista)
    min_idx = 0
    dlugosc_listy = len(lista)
    for indeks in range(1, dlugosc_listy):
        if lista[min_idx] > lista[indeks]:
            min_idx = indeks
    return min_idx

tablica = [1, 4, 0, 5, -3, 2]
n = len(tablica)

for i in range(n):
    min_idx = indeks_najmniejszej_wartosci(tablica[i:]) + i
    # print(f"{min_idx = }")
    # print(i)
    tablica[i], tablica[min_idx] = tablica[min_idx], tablica[i]
    # print(tablica)
print(tablica)



# print(indeks_najmniejszej_wartosci([2, 7, -2, 5, 4]))

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