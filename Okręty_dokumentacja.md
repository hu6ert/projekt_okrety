Projekt z języków symbolicznych 

Dokumentacja 

HUBERT WĄTORCZYK GL.08 

Temat projektu 

Tematem projektu jest gra Okręty (ang. Battleship). Jest to gra strategiczno-planszowa dla dwóch osób. Gra jest znana w wielu krajach pod nazwą: gra w Statki lub Salvo. W polskiej literaturze można się też spotkać z nazwą: wojna morska lub bitwa morska. 

Funkcjonalność 

- Okno z dwoma planszami 10x10 pól (np. siatki przycisków) oraz przyciskiem rozpoczęcia gry przyciskiem reset. Dodatkowo został umieszczony przycisk instrukcja, wyświetlający wskazówki jak należy grać. 
- Na  początku  gracz  rozmieszcza  okręty  (1x  czteromasztowiec,  2x  trójmasztowiec,  3x dwumasztowiec, 4x jednomasztowiec). Okręty są rozmieszczane przez wybór dwóch pól między którymi ma stanąć okręt. W przypadku jednomasztowca należy dwa razy wybrać to samo pole. 
- Po rozmieszczeniu okrętów przez gracza i wciśnięciu przycisku „Bitwa” przeciwnik komputerowy losowo rozmieszcza swoje okręty. 
- Okręty nie mogą się dotykać ani bokami, ani rogami. 
- Po rozmieszczeniu okrętów przez obu graczy jeden z nich wykonuje pierwszy ruch (losowo gracz lub komputer). 
- Wybór celu przez gracza następuje przez kliknięcie pola, w razie trafienia przycisk staje się czerwony, w przeciwnym razie niebieski (nie można strzelić dwa razy w to samo pole). 
- Komputer  strzela  w  losowe,  nie  wybrane  wcześniej  pole.  Po  trafieniu  próba  znalezienia orientacji statku i zestrzelenie go do końca. 
- Gra kończy się, gdy któryś gracz straci ostatni okręt, wyświetlane jest okno z informacją o 

zwycięzcy. 

Moduł[ Battleships ](https://github.com/hu6ert/projekt_okrety/blob/main/Battleships.py)

Klasa[ Game ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/Battleships.py#L9)

Główna klasa odpowiadająca ze okno gry 

[Konstruktor ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/Battleships.py#L13)

Tworzy główne okno programu, ramki, plansze, przyciski, etykiety, dwie instancje klasy Competitor z modułu objects, wyświetla napis powitalny 

Funkcje: 

[create_buttons_board ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/Battleships.py#L78)

`        `Tworzy planszę przycisków (10x10) 

`        `:param frame: ramka na której ma zostać umieszczona siatka         :param h: wysokość przycisku 

`        `:param w: szerokość przycisku 

`        `:param fun: funkcja wywoływana przez przycisk 

`        `:return: lista przycisków tkinter [start_game ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/Battleships.py#L113)

Rozpoczyna grę. Wywoływana przez przycisk Start [reset_game ](file:///C:/Users/huber/OneDrive/Dokhttps:/github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/Battleships.py%23L133umentyLabVIEW%20Data)

Resetuje grę. Wywoływana przez przycisk Reset 

[get_player_ships_to_place ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/Battleships.py#L148)

Zwraca statki do rozstawienia dla gracza 

[display_message ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/Battleships.py#L151)

Wyświetla komunikat w górnej części okna :param message: treść komunikatu 

[get_displayed_message ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/Battleships.py#L158)

Zwraca aktualnie wyświetlony komunikat 

[get_computer_ships_coordinates ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/Battleships.py#L161)

Zwraca współrzędne staków komputera 

[get_computer_board ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/Battleships.py#L167)

Zwraca plansze przycisków komputera 

[place_ship ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/Battleships.py#L176)

Rozmieszcza statek używkownika 

:param coordinate: współrzędne x oraz y przycisku 

[computer_shoot ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/Battleships.py#L201)

Wykonuje strzał kopmutera 

[player_shoot ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/Battleships.py#L225)

Wykonuje strzał gracza 

:param coordinate: współrzędne strzału [end_game ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/Battleships.py#L259)

Kończy grę 

:param name: nazwa wygranego 

Moduł[ objects ](https://github.com/hu6ert/projekt_okrety/blob/main/objects.py)

Klasa[ Ship ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/objects.py#L7)

Klasa reprezentująca pojedynczy statek 

[Konstruktor ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/objects.py#L11)

Uzupełnia współrzędne statku 

:param x1: współrzędna x początku statku 

:param y1: współrzędna y początku statku :param x2: współrzędna x końca statku :param y2: współrzędna y końca statku 

Funkcje: 

[set_drown_state ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/objects.py#L25)

Ustawia stan statku na zatopiony :param name: stan 

[get_taken_fields ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/objects.py#L50)

Zwraca zbiór współrzędnych zajętych dla danego statku 

[add_ship_coordinate ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/objects.py#L57)

Dodaje współrzędne statku do listy ship\_position :param x: współrzędna x pola 

:param y: współrzędna y pola 

Klasa[ Competitor ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/objects.py#L72)

Klasa reprezentująca uczestnika bitwy 

[Konstruktor ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/objects.py#L76)

konstruktor 

:param name: nazwa uczestnika 

Funkcje: 

[place_computer_ships ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/objects.py#L88)

Rozstawia losowo statki komputera 

[try_place_ship ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/objects.py#L110)

Próba umieszczenia statku 

:param x1: współrzędna x początku statku 

:param y1: współrzędna y początku statku 

:param x2: współrzędna x końca statku 

:param y2: współrzędna y końca statku [reset ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/objects.py#L142)

Resetuje atrybuty, zmienne klasy 

[get_competitor_name ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/objects.py#L157)

Zwraca zmienną zawierająca nazwę uczestnika 

[get_ships_list ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/objects.py#L164)

Zwraca listę statków umieszczonych na planszy uczestnika 

[get_ships_to_place ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/objects.py#L171)

Zwraca statki do rozmieszczenia 

[get_my_shots ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/objects.py#L178)

Zwraca set strzały uczestnika 

[ships_to_place_info ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/objects.py#L185)

Zwraca informację o aktualnych statkach do rozstawienia 

[set_ships_to_place ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/objects.py#L192)

Przypisuje do zmiennej ships\_to\_place listę okrętów do rozstawienia znajdującą się w res.py 

[take_shot ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/objects.py#L198)

Dodaje do listy strzałów parę współrzędnych nowego strzału [drown_check ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/objects.py#L205)

Sprawdza czy któryś statek nie jest zatopiony 

[hit_check ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/objects.py#L216)

Sprawdza czy statek został trafiony :param x : współrzędna x wybranego pola :param y: współrzędna y wybranego pola 

[determine_possible_coordinates ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/objects.py#L233)

Wybiera i zwraca możliwe współrzędne do strzału 

[get_drown_ships_taken_fields ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/objects.py#L252)

Zwraca zbiór współrzędnych zajętych przez zatopione okręty 

[ship_detection ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/objects.py#L263)

Dodaje statek do listy \_\_hit\_ships, lub gdy już się tam znajduje dodaje współrzędne :param x: współrzędna x strzelonego pola 

:param y: współrzędna t strzelonego pola 

:param name: stan statku 

Moduł res 

Lista[ LIST_OF_SHIPS ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/res.py#L1)

Lista zawierająca statki do rozmieszczenia, może być zmieniana 

Klasa[ Strings ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/res.py#L4)

Klasa zawierająca wszystkie napisy Klasa[ States ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/res.py#L39)

Klasa zawierająca stany przycisków 

Klasa[ Exceptions ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/res.py#L44)

Klasa zawierająca zdefiniowany wyjątki 

Klasa[ Colors ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/res.py#L62)

Klasa zawierająca zdefiniowany kolory 

Moduł[ test_module ](https://github.com/hu6ert/projekt_okrety/blob/main/test_module.py)

Klasa[ Tests ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/test_module.py#L9)

Klasa zawierający wszystkie testy 

Funkcje: 

[place_ships_properly_and_start_game](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/test_module.py#L10) 

Funkcja pomocnicza, rozstawia poprawnie statki i rozpoczyna grę 

[test_place_ships_improperly ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/test_module.py#L34)

Próba niepoprawnego ustawienia okrętu (stykanie się bokamilub rogami). Oczekiwana informacja o błędzie 

[test_place_ships_properly_and_start_game](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/test_module.py#L43) 

Poprawne rozmieszczenie wszystkich okrętów przez gracza i wciśnięcie przycisku rozpoczęcia gry. 

[test_empty_field_shoot ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/test_module.py#L50)

Strzelenie w puste pole. 

[test_ship_hit ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/test_module.py#L60)

Trafienie w okręt przeciwnika. 

[test_try_shoot_own_ship ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/test_module.py#L69)

Próba zestrzelenia swojego okrętu - oczekiwane niepowodzenie. 

[test_double_empty_field_shoot ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/test_module.py#L77)

Próba ponownego strzelenia w puste pole - oczekiwane niepowodzenie. 

[test_double_ship_hit ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/test_module.py#L87)

Próba ponownego strzelenia w okręt przeciwnika - oczekiwane niepowodzenie. 

[test_place_some_ships_and_reset ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/test_module.py#L96)

Rozmieszczenie części okrętów, wciśnięcie przycisku reset - oczekiwany reset plansz. 

[test_take_some_shots_then_reset_and_again_take_some_shots](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/test_module.py#L106) 

Poprawne rozmieszczenie wszystkich okrętów, oddanie kilku strzałów, rozpoczęcie nowej gry, ponowne poprawne rozmieszczenie okrętów, oddanie strzałów w te same pola. 

[test_win_game ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/test_module.py#L128)

Wygranie gry (np. Przez pokazanie okrętów przeciwnika). Rozpoczęcie nowej gry bez ponownego uruchamiania programu. 

[test_lose_game ](https://github.com/hu6ert/projekt_okrety/blob/aaaffd2cf09639eeb3a35b12cd086d29629f7fc6/test_module.py#L128)

Przegranie gry (np. Przez aktywację super-instynktu gracza komputera). Rozpoczęcie nowej gry bez ponownego uruchamiania programu. 
