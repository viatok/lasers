import copy
import itertools
import sys


class pole:
    # Základní datová struktura uchovávající zadání problému, její třídy jsou nástroje na jeho řešení
    def __init__(self, sirka: int, vyska: int, data):
        self.posunybezzrcadla = 0
        self.vyska = vyska
        self.sirka = sirka
        self.data = data
        self.cile = {}
        self.prustrelycilu = {}
        self.pouzitazrcadla = {(i, j): 0 for i in range(sirka) for j in range(vyska)}
        self.prazdna_pole = [(i, j) for i in range(sirka) for j in range(vyska) if self.data[i][j] == 'x']

    def vytiskni(self):
        # pomocná funkce, vizuálně vykreslí zadání
        for line in self.data:
            print(' '.join(map(str, line)))

    def v_tabulce(self, x, y):
        # Vrátí ano, pokud je zadaný bod v tabulce
        if x in range(self.sirka) and y in range(self.vyska):
            return True
        else:
            return False

    def volne_pole(self, x, y):
        # Vrátí ano, pokud je zadaný bod prázdný (není na něm zeď)
        volne = ['>', '<', '^', 'v', 'o', 'x', '/', '\\']
        if self.data[x][y] in volne or self.data[x][y].isnumeric():
            return True
        else:
            return False

    def posouvejlaser(self, x, y, smer):
        # Simuluje vystřelený laser, rekurzivně se zavolá na to pole a směr, kam se laser posune
        self.posunybezzrcadla += 1
        if self.posunybezzrcadla > self.vyska * self.sirka:
            return 1  # Pokud se laser do nekonečna hýbe mezi dvěma zdmi, tímto je zastaven
        aktualni_pole = [x, y]
        cilove_pole = [x + smer[0], y + smer[1]]
        if self.data[x][y].isnumeric():  # zda jsme zasáhli cíl
            self.prustrelycilu[(x, y)] += 1
        if self.data[aktualni_pole[0]][aktualni_pole[1]] == '/' and self.pouzitazrcadla[
            (aktualni_pole[0], aktualni_pole[1])] == 0:
            self.posunybezzrcadla = 0
            self.pouzitazrcadla[(aktualni_pole[0], aktualni_pole[1])] += 1
            novysmer = [-smer[1], -smer[0]]
            self.posouvejlaser(aktualni_pole[0], aktualni_pole[1], novysmer)
        elif self.data[aktualni_pole[0]][aktualni_pole[1]] == '\\' and self.pouzitazrcadla[
            (aktualni_pole[0], aktualni_pole[1])] == 0:
            self.posunybezzrcadla = 0
            self.pouzitazrcadla[(aktualni_pole[0], aktualni_pole[1])] += 1
            novysmer = [smer[1], smer[0]]
            self.posouvejlaser(aktualni_pole[0], aktualni_pole[1], novysmer)

        elif not self.v_tabulce(cilove_pole[0], cilove_pole[1]):
            self.posouvejlaser(x, y, [-smer[i] for i in range(2)])
        elif self.volne_pole(cilove_pole[0], cilove_pole[1]):
            self.posouvejlaser(cilove_pole[0], cilove_pole[1], smer)
        else:
            raise Exception('nevalidni pole')  # Vždy by měla nastat jedna z předchozích možností.

    def vypustlaser(self, x, y):
        # Vystřelí laser z některého z polí, na kterých se v zadání laser nachází
        self.pouzitazrcadla = {(i, j): 0 for i in range(self.sirka) for j in range(self.vyska)}
        self.posunybezzrcadla = 0
        if self.data[x][y] == '^':
            self.posouvejlaser(x, y, [-1, 0])
        elif self.data[x][y] == '>':
            self.posouvejlaser(x, y, [0, 1])
        elif self.data[x][y] == 'v':
            self.posouvejlaser(x, y, [1, 0])
        elif self.data[x][y] == '<':
            self.posouvejlaser(x, y, [0, -1])
        else:
            raise Exception('zde nelze vypustit laser')

    def inicializujcile(self):  # Nastaví počítadla průstřelů cílů na 0 (předchozí pokusy s nimi mohly pracovat)
        for i in range(self.sirka):
            for j in range(self.vyska):
                if self.data[i][j].isnumeric():
                    self.prustrelycilu[(i, j)] = 0

    def vypustlasery(self):
        # Vystřelí laser z každého pole k tomu určenému
        for i in range(self.sirka):
            for j in range(self.vyska):
                if self.data[i][j] in ['^', '>', 'v', '<']:
                    self.vypustlaser(i, j)

    def splnitelne(self, n):
        # Testuje, zda je úloha splnitelná na n zrcadel
        for kombinace in itertools.combinations(self.prazdna_pole, n):
            planeksezrcadly = copy.deepcopy(self)
            planeksezrcadly.data = copy.deepcopy(planeksezrcadly.data)
            for vyber in vsechnyvybery(kombinace):
                for zrcadlo in kombinace:
                    if zrcadlo in vyber:
                        planeksezrcadly.data[zrcadlo[0]][zrcadlo[1]] = '/'
                    else:
                        planeksezrcadly.data[zrcadlo[0]][zrcadlo[1]] = '\\'
                planeksezrcadly.inicializujcile()
                planeksezrcadly.vypustlasery()

                if min(planeksezrcadly.prustrelycilu.values()) > 0:
                    print('Řešení tohoto plánku je:')
                    planeksezrcadly.vytiskni()
                    return 1
                planeksezrcadly.data = copy.deepcopy(self.data)
        return 0




zadani = []
for line in sys.stdin:  # Přečte zadání úlohy stdin (tabulku m krát n)
    docasna = line.strip().split()
    zadani.append(docasna)
zadany_objekt = pole(len(zadani), len(zadani[0]), zadani)
zadany_objekt.vytiskni()  # Ukáže zadání pro přehlednost


def vsechnyvybery(seznam):
    # Pomocná funkce, která vrátí všech 2^n kombinací ze seznamu o n prvcích
    vysledek = []
    for i in range(len(seznam) + 1):
        for kombinace in itertools.combinations(seznam, i):
            vysledek.append(kombinace)
    return vysledek


def vyhledej_k(planek):
    # Hlavní funkce, vyhledá minimální počet zrcadel postupným zkoušením
    n = 0
    while n < planek.sirka * planek.vyska:
        n += 1
        if planek.splnitelne(n):
            return n
    raise Exception('nepovedlo se na 100000000')



#samotný program
print(vyhledej_k(zadany_objekt))
