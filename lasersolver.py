


class pole:
    def __init__(self, sirka : int, vyska : int, data):
        self.vyska = vyska
        self.sirka = sirka
        self.data = data


    def vytiskni(self):
        for line in self.data:
            print(' '.join(map(str, line)))

    def v_tabulce(self, x, y):
        if x in range(sirka) and y in range(vyska):
            return True
        else:
            return False

    def volne_pole(self, x, y):
        volne = ['>', '<', '^', 'v', 'o']
        if self.data[x][y] in volne:
            return True
        else:
            return False









