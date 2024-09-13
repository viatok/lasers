# Přehled 

Jako zápočtový program jsem vypracoval program řešící jistou logickou úlohu. Umí úlohu vyřešit, a lze s ním generovat zadání těchto úloh i s řešeními. Všechny dokumenty jsou uloženy na githubovém repozitáři. Jeho obsahem jsou tyto soubory:

- lasersolver.py dostane na stdin zadání jedné instance této úlohy, a vypíše do konzole její řešení.
- interface.py je program, se kterým uživatel primárně komunikuje a spouští ho, tento program umí generovat zadání či číst zadání ze souborů, a zavolá si na ně program lasersolver, čímž tedy nepřímo vypíše řešení.
- zbylé textové soubory jsou sady vstupů, které se dají dát programu lasersolver.py k vyřešení
- a samozřejmě tato dokumentace


# Zadání problému

Program řeší tuto úlohu: Mějme tabulku n x m, která má na svých polích tyto objekty:

- Cíle k trefení, reprezentované v textu znakem '1'
- Zdi, reprezentované znakem 'z'
- Lasery se čtyřmi orientacemi rovnoběžnými se stěnami tabulky, reprezentovanými znaky '<', '^', '>' a 'v'
- Prázdná pole, reprezentovaná '.'

Úlohou je rozmístit na pole diagonálně orientovaná zrcadla, reprezentovaná dle jejich orientace buď '\' nebo '/', a to tak, aby po vystřelení všech laserů byl každý cíl zasažen alespoň jednou. Cílem je použít co nejméně zrcadel.

Laser se chová následovně:

- Přes volná pole prochází
- Cílem prochází
- Od zdi se odrazí zpátky
- Od kraje tabulky se odrazí zpátky
- Od zrcadla se odrazí o 90 stupňů, dle jeho orientace. Pokud však by mělo jít o druhý odraz od téhož zrcadla, místo toho jím proletí.

Časem tedy nutně skončí v nekonečné smyčce, ta je programem po dostatečném čase utnuta.

# Algoritmické řešení

Program **lasersolver.py** na stdin dostane validní zadání, tedy tabulku celočíselných rozměrů, se znaky oddělenými mezerami.

Zadání si převede do své datové struktury (třída Pole). Na ni volá funkci vyhledej_k, která bude postupně zvyšovat počty zrcadel, vždy zavolá funkci splnitelne, aby zjistila, zda je úloha splnitelná s k zrcadly, načež pokud není, tak zvýší počet zrcadel.

Funkce splnitelne si získá seznam všech možných umístění zrcadel a pro každé takové umístění si vytvoří pomocnou instanci třídy pole, neboli kopii, do které daná zrcadla na daná pole umístí a otestuje, zda je to řešením úlohy (ale dělá to postupně, tedy jméno pomocného plánku zůstává stejné a paměťovou složitost to má O(1)).

Pro otestování, zda je dané rozmístění zrcadel řešením, se spustí funkce vypustlasery, která vystřelí ze všech laserů, načež se zkontroluje, zda byly zasaženy všechny cíle. Výstřel z laseru je odstartován funkcí vypustlaser, která na dané pole zavolá se správnou orientací funkci posouvejlaser. Ta se rekurzivně volá vždy o jedno pole dál a simuluje tím laser (který letí dle pravidel úlohy). Poté co se dostatečně dlouho nic nestane (laser nezmění směr), usoudí funkce, že je laser v nekonečné smyčce, a zastaví ho.


Program **interface.py** umí generovat libovolný počet zadání. Jak již bylo popsáno, uživatel si vždy vybere buď že chce generovat dál (klávesa 'g'), nebo ukončit program (klávesa 'k'). Pokud chce generovat, zadá parametry zadání. Ta jsou poté předána funkci generate, která se pokusí vygenerovat dané zadání tak, že vygeneruje pole správných rozměrů, načež na něj umístí všechny lasery, zdi a cíle. Vždy vygeneruje nějaké souřadnice, načež se podívá, zda je tam volno, a umístí na ně daný objekt (toto je naivní implementace, ale pro velikosti tabulky, které program umí vyřešit, je to postačující).

Poté co je zadání vygenerováno se na něj spustí funkce vyhledej_k, importovaná z lasersolver. Poté se zadání zapíše do generovane.txt (je možné jej znovu spustit z tohoto souboru přímo pomocí lasersolver), a může se generovat znovu.

# Low lvl dokumentace

### Třída pole

Základní objekt, se kterým program operuje, je v něm obsažena instance zadání. Musí být zadán s inicializačními parametry vyska, sirka, data.

#### Vytiskni

Základní funkce, která pěkně vykreslí tabulku do konzole.

#### v_tabulce

Vrátí ano, pokud se zadané pole nachází v tabulce.

#### volne_pole

Vrátí ano, pokud je zadaný bod prázdný

#### posouvejlaser

Simuluje vystřelený laser, rekurzivně volá sama sebe.

#### vypustlaser

Vystřelí laser z některého z polí, na kterých je zavoláno

#### splnitelne

Vrátí ano, pokud je úloha splnitelná na n zrcadel. Testuje postupným zvyšováním n.

#### Vyhledej_k

Vyhledá minimální počet zrcadel, řešení vytiskne na konzoli, optimum vrátí. Volí si funkci splnitelne.

#### Parser

Funkce, která načte vstup a vrátí výsledný objekt
# Obsluha programu

Pro generování zadání spusťte interface.py. Nyní můžete generovat kolik jen úloh chcete. Zadejte 'g' jako generovat, následně zadejte na jeden řádek pět přirozených čísel, oddělených mezerou. V tomto pořadí čísla reprezentují: Výšku tabulky, šířku tabulky, počet cílů, počet laserů, počet zdí v tabulce. Zřejmě je potřeba, aby součet umisťovaných objektů nepřevyšoval počet polí v tabulce. Bude vygenerováno rovnoměrně náhodné zadání s požadovanými počty objektů.

Vygenerované zadání se vytiskne, vyřeší, a uloží do souboru generovane.txt. Pokud si přejete zadání uschovat, můžete ho přejmenovat, jinak bude při příštím generování přepsán.

Druhou možností je předat hotové zadání programu lasersolver.py, který ho jen vyřeší. Program ho přijímá na **stdin**, pokud chcete číst ze souborů, je nutné program zavolat rovnou s daným souborem jako vstupem (z konzole).

## Změny vůči původnímu zadání

Některé aspekty jsem vůči původnímu zadání pozměnil a to konkrétně:

- Lasery mohou být umístěny i uprostřed tabulky. Umožňuje to zajímavější zadání
- Program nezkouší umístění zrcadel v žádném konkrétním pořadí (Vždy stejně musí projít všechna umístění daného počtu zrcadel, aby si byl jistý, že to na dané k splnit nelze, než se posune na větší k)



