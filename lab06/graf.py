class GrafNieskierowanyWazony():
    def __init__(self, n_wierzcholkow, n_krawedzi) -> None:
        self.wierzcholki = []
        self.krawedzie = []
        self.listaSasiedztwa = [[] for i in range(n_wierzcholkow)]
        self.macierzSasiedztwa = [
            [0] * n_wierzcholkow for i in range(n_wierzcholkow)]

    def dodajWierzcholek(self, wierzcholek):
        self.wierzcholki.append(wierzcholek)

    def dodajKrawedz(self, wierzcholek1, wierzcholek2, waga):
        self.krawedzie.append((wierzcholek1, wierzcholek2, waga))
        self.listaSasiedztwa[wierzcholek1].append((wierzcholek2, waga))
        self.listaSasiedztwa[wierzcholek2].append((wierzcholek1, waga))
        self.macierzSasiedztwa[wierzcholek1][wierzcholek2] = waga
        self.macierzSasiedztwa[wierzcholek2][wierzcholek1] = waga


g = GrafNieskierowanyWazony(4, 6)
g.dodajWierzcholek(0)
g.dodajWierzcholek(1)
g.dodajWierzcholek(2)
g.dodajWierzcholek(3)

print(g.listaSasiedztwa)

g.dodajKrawedz(0, 1, 8)
g.dodajKrawedz(0, 3, 3)
g.dodajKrawedz(0, 2, 8)
g.dodajKrawedz(1, 2, 3)
g.dodajKrawedz(1, 3, 7)
g.dodajKrawedz(2, 3, 6)


for i in g.macierzSasiedztwa:
    print(i)

print()
g = GrafNieskierowanyWazony(6, 9)
g.dodajWierzcholek(0)
g.dodajWierzcholek(1)
g.dodajWierzcholek(2)
g.dodajWierzcholek(3)
g.dodajWierzcholek(4)
g.dodajWierzcholek(5)

g.dodajKrawedz(0, 1, 3)
g.dodajKrawedz(0, 5, 4)
g.dodajKrawedz(4, 3, 9)

g.dodajKrawedz(2, 3, 5)
g.dodajKrawedz(1, 2, 5)
g.dodajKrawedz(4, 5, 6)

g.dodajKrawedz(1, 5, 8)
g.dodajKrawedz(2, 5, 14)
g.dodajKrawedz(2, 4, 10)
for i in g.macierzSasiedztwa:
    print(i)
