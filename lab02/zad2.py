from Grafy import *

graf = GrafNieskierowany()
graf.dodaj_wierzcholek(1)
graf.dodaj_wierzcholek(2)
graf.dodaj_wierzcholek(3)
graf.dodaj_wierzcholek(4)
graf.dodaj_wierzcholek(5)
graf.dodaj_krawedz(1, 2)
graf.dodaj_krawedz(2, 3)
graf.dodaj_krawedz(3, 4)
graf.dodaj_krawedz(4, 5)
graf.dodaj_krawedz(5, 1)
graf.dodaj_krawedz(1, 4)

g = [
    [0, 1, 0, 1, 1],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1],
    [1, 0, 0, 1, 0]]


def znajdz_cykl_c3_macierz(g):
    for w1 in range(len(g)):
        for w2 in range(len(g)):
            if w1 == w2:
                continue
            for w3 in range(len(g)):
                if w3 == w1 or w3 == w2:
                    continue
                if g[w1][w2] > 0 and g[w2][w3] > 0 and g[w3][w1] > 0:
                    cykl = [w1, w2, w3]
                    for w in range(len(cykl)):
                        cykl[w] += 1
                    return True, cykl
    return False


print(znajdz_cykl_c3_macierz(g))


def podniesc_macierz_do_potegi(g, n):
    if n == 0:
        return g
    if n == 1:
        return g
    return pomnoz_macierz(g, podniesc_macierz_do_potegi(g, n-1))


def pomnoz_macierz(m1, m2):
    wynik = [[0 for _ in range(len(m1))] for _ in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            for k in range(len(m1)):
                wynik[i][j] += m1[i][k] * m2[k][j]
    return wynik


def znajdz_cykl_c3_macierz_potegi(g):
    potega = podniesc_macierz_do_potegi(g, 3)
    for wiersz in potega:
        print(wiersz)
    tmp = 0
    for i in range(len(potega)):
        tmp += potega[i][i]
    return tmp/6 > 0


print(znajdz_cykl_c3_macierz_potegi(g))
