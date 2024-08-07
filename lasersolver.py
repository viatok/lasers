


class pole:
    def __init__(self, sirka : int, vyska : int, data):
        self.vyska = vyska
        self.sirka = sirka
        self.data = data


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
        if self.data[x][y] in volne:
            return True
        else:
            return False
    def posouvejlaser(self, x, y, smer):
        print(x, y)
        print(smer)
        aktualni_pole = [x, y]
        cilove_pole = [x + smer[0], y + smer[1]]

        if self.data[aktualni_pole[0]][aktualni_pole[1]] == '/':
            novysmer = [-smer[1], -smer[0]]
            self.posouvejlaser(aktualni_pole[0] + novysmer[0], aktualni_pole[1] + novysmer[1], novysmer)
        elif self.data[aktualni_pole[0]][aktualni_pole[1]] == '\\':
            novysmer = [smer[1], smer[0]]
            self.posouvejlaser(aktualni_pole[0] + novysmer[0], aktualni_pole[1] + novysmer[1], novysmer)

        elif not self.v_tabulce( cilove_pole[0], cilove_pole[1]):
            self.posouvejlaser( x,y, [-smer[i] for i in range(2)])
        elif self.volne_pole(cilove_pole[0], cilove_pole[1]):
            self.posouvejlaser( cilove_pole[0], cilove_pole[1], smer)
        else:
            pass

    def vypustlaser(self, x, y):
        if self.data[x][y] == '^':
            posouvejlaser(x, y, [-1, 0])
        elif self.data[x][y] == '>':
            posouvejlaser( x, y, [0,1])
        elif self.data[x][y] == 'v':
            posouvejlaser( x, y, [1,0])
        elif self.data[x][y] == '<':
            posouvejlaser( x, y, [0,-1])
        else:
            raise  Exception('zde nelze vypustit laser')

with open("vstup.txt", 'r') as vstupy:
    radky = vstupy.readlines()
    zadani = []
    for line in radky:
        docasna = line.strip().split()
        zadani.append(docasna)

    vstupy.close()
zadany_objekt = pole(len(zadani), len(zadani[0]), zadani)
zadany_objekt.posouvejlaser(1, 1, [0, 1])
zadany_objekt.vytiskni()




