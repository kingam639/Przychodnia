# funkcja rekuryncje wypisze 3x siema
# skad drugie wypoisz siema ma wiedziec ze  jest drugie

# def wypisz_siema(i):
#     print(f"siema jestem {i}")
#     if i < 2:
#         wypisz_siema(i+1)
#         # 2ga opcja
#         # i += 1
#         # wypisz_siema(i)
#
#
# def test(i):
#     print(f"siema jestem {i}")
#
# i = 0
# while i  < 3:
#     i += 1
#     # test(i)
#
#
#
# wypisz_siema(i=0)


# silnia, oblicz silnie liczby uzywajac rekurencji

def oblicz_silnie(n, silnia=1):
    silnia *= n
    while n > 1:
        n -= 1
        oblicz_silnie(n, silnia)
    return silnia
    # if n == 1 or n == 0:
    #     return 1


#
print(oblicz_silnie(3))

# n = 3
# silnia = 1
# if n == 1 or n == 0:
#     print(silnia)
# else:
#     while n > 1:
#         silnia *= n
#         n -= 1
#
# print(silnia)



