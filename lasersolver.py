import copy
import itertools



class pole:
    def __init__(self, sirka : int, vyska : int, data):
        self.posunybezzrcadla = 0
        self.vyska = vyska
        self.sirka = sirka
        self.data = data
        self.cile = {}
        self.prustrelycilu = {}
        self.pouzitazrcadla = {(i,j) : 0 for i in range(sirka) for j in range(vyska)}
        print(self.pouzitazrcadla)
        self.prazdna_pole = [(i, j) for i in range(sirka) for j in range(vyska) if self.data[i][j] == 'x']
    def vytiskni(self):
        for line in self.data:
            print(' '.join(map(str, line)))

    def v_tabulce(self, x, y):
        if x in range(self.sirka) and y in range(self.vyska):
            return True
        else:
            return False

    def volne_pole(self, x, y):
        volne = ['>', '<', '^', 'v', 'o', 'x', '/', '\\']
        if self.data[x][y] in volne or self.data[x][y].isnumeric():
            return True
        else:
            return False


    def posouvejlaser(self, x, y, smer):
        self.posunybezzrcadla += 1
        if self.posunybezzrcadla > self.vyska * self.sirka:
            return 1
        aktualni_pole = [x, y]
        cilove_pole = [x + smer[0], y + smer[1]]
        if self.data[x][y].isnumeric():
            self.prustrelycilu[(x, y)] += 1
        if self.data[aktualni_pole[0]][aktualni_pole[1]] == '/' and self.pouzitazrcadla[(aktualni_pole[0], aktualni_pole[1])] == 0:
            self.posunybezzrcadla = 0
            self.pouzitazrcadla[(aktualni_pole[0], aktualni_pole[1])] += 1
            novysmer = [-smer[1], -smer[0]]
            self.posouvejlaser(aktualni_pole[0], aktualni_pole[1], novysmer)
        elif self.data[aktualni_pole[0]][aktualni_pole[1]] == '\\' and self.pouzitazrcadla[(aktualni_pole[0], aktualni_pole[1])] == 0:
            self.posunybezzrcadla = 0
            self.pouzitazrcadla[(aktualni_pole[0], aktualni_pole[1])] += 1
            novysmer = [smer[1], smer[0]]
            self.posouvejlaser(aktualni_pole[0] , aktualni_pole[1], novysmer)

        elif not self.v_tabulce( cilove_pole[0], cilove_pole[1]):
            self.posouvejlaser( x,y, [-smer[i] for i in range(2)])
        elif self.volne_pole(cilove_pole[0], cilove_pole[1]):
            self.posouvejlaser( cilove_pole[0], cilove_pole[1], smer)
        else:
            raise Exception('nevalidni pole')


    def vypustlaser(self, x, y):
        self.pouzitazrcadla = {(i,j) : 0 for i in range(self.sirka) for j in range(self.vyska)}
        self.posunybezzrcadla = 0
        if self.data[x][y] == '^':
            self.posouvejlaser(x, y, [-1, 0])
        elif self.data[x][y] == '>':
            self.posouvejlaser( x, y, [0,1])
        elif self.data[x][y] == 'v':
            self.posouvejlaser( x, y, [1,0])
        elif self.data[x][y] == '<':
            self.posouvejlaser( x, y, [0,-1])
        else:
            raise  Exception('zde nelze vypustit laser')

    def inicializujcile(self):
        for i in range(self.sirka):
            for j in range(self.vyska):
                if self.data[i][j].isnumeric():
                    #self.cile[(i, j)] = self.data[i][j]
                    self.prustrelycilu[(i, j)] = 0

    def vypustlasery(self):
        for i in range(self.sirka):
            for j in range(self.vyska):
                if self.data[i][j] in ['^', '>', 'v', '<']:
                    self.vypustlaser(i, j)

    def splnitelne(self, n):
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
                    planeksezrcadly.vytiskni()
                    return 1
                planeksezrcadly.data = copy.deepcopy(self.data)
        return 0

with open("vstup.txt", 'r') as vstupy:
    radky = vstupy.readlines()
    zadani = []
    for line in radky:
        docasna = line.strip().split()
        zadani.append(docasna)
    vstupy.close()

zadany_objekt = pole(len(zadani), len(zadani[0]), zadani)
zadany_objekt.vytiskni()

def vsechnyvybery(seznam):
    vysledek = []
    for i in range(len(seznam) + 1):
        for kombinace in itertools.combinations(seznam, i):
            vysledek.append(kombinace)
    return vysledek
def vyhledej_k(planek):
    n = 0
    while n < 10000000:
        n += 1
        if planek.splnitelne(n):
            return n
    raise Exception('nepovedlo se na 100000000')
print(vsechnyvybery([1,2,6]))
print(vyhledej_k(zadany_objekt))


