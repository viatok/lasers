# Přehled 

Jako zápočtový program jsem vypracoval program řešící jistou logickou úlohu. Umí úlohu vyřešit, a lze s ním generovat zadání těchto úloh i s řešeními. Všechny dokumenty jsou uloženy na githubovém repozitáři. Jeho obsahem jsou tyto soubory:

- lasersolver.py dostane na stdin zadání jedné instance této úlohy, a vypíše do konzole její řešení.
- interface.py je program, se kterým uživatel primárně komunikuje a spouští ho, tento program umí generovat zadání či číst zadání ze souborů, a zavolá si na ně program solver, čímž tedy nepřímo vypíše řešení.
- zbylé textové soubory jsou sady vstupů, které se dají spustit programem interface.py
- a samozřejmě tato dokumentace


# Zadání problému

Program řeší tuto úlohu: Mějme tabulku n x m, která má na svých polích tyto objekty:

- Cíle k trefení, reprezentované v textu znakem '1'
- Zdi, reprezentované znakem 'z'
- Lasery se čtyřmi orientacemi rovnoběžnými se stěnami tabulky, reprezentovanými znaky '<', '^', '>' a 'v'
- Prázdná pole, reprezentovaná 'x'

Úlohou je rozmístit na pole zrcadla, reprezentovaná dle jejich orientace buď '\' nebo '/', a to tak, aby po vystřelení všech laserů byl každý cíl zasažen alespoň jednou. Cílem je použít co nejméně zrcadel.

Laser se chová následovně:

- Přes volná pole prochází
- Cílem prochází
- Od zdi se odrazí zpátky
- Od kraje tabulky se odrazí zpátky
- Od zrcadla se odrazí o 90 stupňů, dle jeho orientace. Pokud však by mělo jít o druhý odraz od téhož zrcadla, místo toho jím proletí.

Časem tedy nutně skončí v nekonečné smyčce, ta je programem po dostatečném čase utnuta.

# Algoritmické řešení

Program lasersolver.py na stdin dostane validní zadání, tedy tabulku celočíselných rozměrů, se znaky oddělenými mezerami.

Zadání si převede do své datové struktury (třída Pole). Na ni volá funkci vyhledej_k, která bude postupně zvyšovat počty zrcadel, vždy zavolá funkci splnitelne, aby zjistila, zda je úloha splnitelná s k zrcadly, načež pokud není, tak zvýší počet zrcadel.

Funkce splnitelne si získá seznam všech možných umístění zrcadel a pro každé takové umístění si vytvoří pomocnou instanci třídy pole, neboli kopii, do které daná zrcadla na daná pole umístí a otestuje, zda je to řešením úlohy (ale dělá to postupně, tedy jméno pomocného plánku zůstává stejné a paměťovou složitost to má O(1)).

Pro otestování, zda je dané rozmístění zrcadel řešením, se spustí funkce vypustlasery, která vystřelí ze všech laserů, načež se zkontroluje, zda byly zasaženy všechny cíle.

