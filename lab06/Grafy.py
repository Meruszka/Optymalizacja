class GrafNieskierowany:
    def __init__(self) -> None:
        self.lista_sasiedztwa = {}
        self.lista_krawedzi = []
        self.lista_wierzcholkow = []
    def dodaj_wierzcholek(self, wierzcholek):
        self.lista_wierzcholkow.append(wierzcholek)
        self.lista_sasiedztwa[wierzcholek] = []
    def dodaj_krawedz(self, wierzcholek1, wierzcholek2):
        self.lista_krawedzi.append((wierzcholek1, wierzcholek2))
        self.lista_sasiedztwa[wierzcholek1].append(wierzcholek2)
        self.lista_sasiedztwa[wierzcholek2].append(wierzcholek1)
    def usun_wierzcholek(self, wierzcholek):
        self.lista_wierzcholkow.remove(wierzcholek)
        self.lista_sasiedztwa.pop(wierzcholek)
        for wierzcholek in self.lista_wierzcholkow:
            if wierzcholek in self.lista_sasiedztwa[wierzcholek]:
                self.lista_sasiedztwa[wierzcholek].remove(wierzcholek)
    def usun_krawedz(self, wierzcholek1, wierzcholek2):
        self.lista_krawedzi.remove((wierzcholek1, wierzcholek2))
        self.lista_sasiedztwa[wierzcholek1].remove(wierzcholek2)
        self.lista_sasiedztwa[wierzcholek2].remove(wierzcholek1)
    def wypisz(self):
        print("Wierzcholki: ", self.lista_wierzcholkow)
        print("Krawedzie: ", self.lista_krawedzi)
        print("Lista sasiedztwa: ", self.lista_sasiedztwa)
        self.wypisz_macierz_sasiedztwa()
    def wypisz_wierzcholki(self):
        print(self.lista_wierzcholkow)
    def wypisz_macierz_sasiedztwa(self):
        macierz = []
        for wierzcholek1 in self.lista_wierzcholkow:
            wiersz = []
            for wierzcholek2 in self.lista_wierzcholkow:
                if wierzcholek2 in self.lista_sasiedztwa[wierzcholek1]:
                    wiersz.append(1)
                else:
                    wiersz.append(0)
            macierz.append(wiersz)
        return macierz

class GrafSkierowany:
    def __init__(self) -> None:
        self.lista_sasiedztwa = {}
        self.lista_krawedzi = []
        self.lista_wierzcholkow = []
    def dodaj_wierzcholek(self, wierzcholek):
        self.lista_wierzcholkow.append(wierzcholek)
        self.lista_sasiedztwa[wierzcholek] = []
    def dodaj_krawedz(self, wierzcholek1, wierzcholek2):
        self.lista_krawedzi.append((wierzcholek1, wierzcholek2))
        self.lista_sasiedztwa[wierzcholek1].append(wierzcholek2)
    def usun_wierzcholek(self, wierzcholek):
        self.lista_wierzcholkow.remove(wierzcholek)
        self.lista_sasiedztwa.pop(wierzcholek)
        for wierzcholek in self.lista_wierzcholkow:
            if wierzcholek in self.lista_sasiedztwa[wierzcholek]:
                self.lista_sasiedztwa[wierzcholek].remove(wierzcholek)
    def usun_krawedz(self, wierzcholek1, wierzcholek2):
        self.lista_krawedzi.remove((wierzcholek1, wierzcholek2))
        self.lista_sasiedztwa[wierzcholek1].remove(wierzcholek2)
    def wypisz(self):
        print("Wierzcholki: ", self.lista_wierzcholkow)
        print("Krawedzie: ", self.lista_krawedzi)
        print("Lista sasiedztwa: ", self.lista_sasiedztwa)
        self.wypisz_macierz_sasiedztwa()    
    def wypisz_wierzcholki(self):
        print(self.lista_wierzcholkow)
    def wypisz_macierz_sasiedztwa(self):
        print("Macierz sasiendztwa:")
        macierz = []
        for wierzcholek in self.lista_wierzcholkow:
            wiersz = []
            for wierzcholek2 in self.lista_wierzcholkow:
                if wierzcholek2 in self.lista_sasiedztwa[wierzcholek]:
                    wiersz.append(1)
                else:
                    wiersz.append(0)
            macierz.append(wiersz)
        print(macierz)

class GrafNieskierowanyWazony(GrafNieskierowany):
    def __init__(self, n):
        super().__init__()
        self.wagi = [[0 for _ in range(n)] for _ in range(n)]

    def dodaj_krawedz(self, a, b, waga):
        super().dodaj_krawedz(a, b)
        self.wagi[a][b] = waga
        self.wagi[b][a] = waga

    def waga(self, a, b):
        return self.wagi[a][b]

    def __str__(self):
        s = super().__str__()
        s += "Wagi krawędzi"