import random
import lasersolver


konverzace = True
def umistuj(objekt, pocet, tabulka): #umístí do dané tabulky daný počet daných objektů
    umisteno = 0
    while umisteno < pocet:
        x = random.randint(0, len(tabulka)-1)
        y = random.randint(0, len(tabulka[0])-1)
        if tabulka[x][y] == '.':
            tabulka[x][y] = objekt
            umisteno += 1
    return tabulka
def generate(sirka, vyska, cile, lasery, zdi): #Vytvoří zadání o daných parametrech
    tabulka = [['.' for i in range(sirka)] for j in range(vyska)]
    tabulka = umistuj('1', cile, tabulka)
    tabulka = umistuj('l', lasery, tabulka)
    tabulka = umistuj('z', zdi, tabulka)
    for x in range(len(tabulka)):
        for y in range(len(tabulka[0])):
            if tabulka[x][y] == 'l':
                orientace = ['^', '>', 'v', '<']
                zvolenaorientace = random.randint(0, 3)
                tabulka[x][y] = orientace[zvolenaorientace]
    return tabulka
while konverzace: # Hlavní program, přijímá zadání dokud to lze
    pozadavek = input('Přejete si generovat zadání? Zadejte g pro generování, k pro konec programu.')
    if pozadavek == 'g':
        parametry = list(map(int, input('Zadejte jako čísla oddělená mezerami: Šířku, výšku, počet cílů, počet laserů, počet zdí').split()))
        if parametry[2] == 0:
            raise Exception('Počet cílů musí být kladný')
        if parametry[0]*parametry[1] < parametry[2] + parametry[3] + parametry[4]:
            raise Exception('Nelze vygenerovat tabulku o daných parametrech')
        vygenerovane = generate(parametry[0], parametry[1], parametry[2], parametry[3], parametry[4])
        if not type(vygenerovane) == int:
            generovanyobjekt = lasersolver.pole(parametry[1], parametry[0], vygenerovane)
            lasersolver.vyhledej_k(generovanyobjekt)
            with open('generovane.txt', 'w') as f: #zapíše vygenerované zadání pro budoucí použití
                f.truncate(0)
                for line in vygenerovane:
                    f.write(' '.join(line) + '\n')
                f.close()
    if pozadavek == 'k': #k jako konec
        konverzace = False
