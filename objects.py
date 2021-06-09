from operator import itemgetter
from res import *
from res import Strings as Strings
import random


class Ship:
    """
    Klasa Ship reprezentująca pojedynczy statek
    """
    def __init__(self, x1, y1, x2, y2):
        """
        konstruktor klasy
        Uzupełnia współdzędne statku, w zależności od orientacji
        :param x1: współrzędna x początku statku
        :param y1: współrzędna y początku statku
        :param x2: współrzędna x końca statku
        :param y2: współrzędna y końca statku
        """
        if x2 != x1:
            self.__ship_position = [(x, y1) for x in range(x1, x2 + 1)]
        else:
            self.__ship_position = [(x1, y) for y in range(y1, y2 + 1)]

    def set_drown_state(self, name):
        """
        Ustawia stan statku na zatopiony
        :param name: stan
        """
        if name == Strings.DROWN:
            self.__setattr__("drown", True)
        else:
            self.__setattr__("drown", False)

    def get_taken_fields(self):
        """
        Zwraca zbiór współrzędnych zajętych dla danego statku
        """
        xp = (self.__ship_position[0])[0]
        yp = (self.__ship_position[0])[1]
        if (len(self.__ship_position)) > 1:
            xk = (self.__ship_position[-1])[0]
            yk = (self.__ship_position[-1])[1]
        else:
            xk, yk = xp, yp
        taken = {(x, y) for x in range(xp - 1, xk + 2) for y in range(yp - 1, yk + 2)}
        taken = taken & {(x, y) for x in range(1, 11) for y in range(1, 11)}
        return taken

    def get_ship_position(self):
        """
        Zwraca listę określająca zajmowane pola przez statek
        :return: __ship_position :list
        """
        return self.__ship_position

    def add_ship_coordinate(self, x, y):
        """
        Dodaje współrzędne statku do listy __ship_position
        :param x: współrzędna x pola
        :param y: współrzędna y pola
        """
        self.__ship_position.append((x, y))
        if x != self.__ship_position[0][0]:
            self.__ship_position = sorted(self.__ship_position, key=itemgetter(0))
            self.__setattr__("horizontal", True)
        else:
            self.__ship_position = sorted(self.__ship_position, key=itemgetter(1))
            self.__setattr__("horizontal", False)


class Competitor:
    """
    Klasa Competitor reprezentująca uczestnika bitwy
    """
    def __init__(self, name):
        """
        konstruktor
        :param name: nazwa gracza
        """
        self.__competitor_name = name
        self.__ships_list = []
        self.__ships_to_place = []
        self.set_ships_to_place()
        self.__player_shots = set()
        self.__hit_ships = []

    def place_computer_ships(self):
        """
        Rozstawia losowo statki komputera
        """
        unavailable_fields = set()
        all_coordinates = {(x, y) for x in range(1, 11) for y in range(1, 11)}
        for length in LIST_OF_SHIPS:
            length -= 1
            available_fields = [zb for zb in all_coordinates - unavailable_fields]
            while True:
                x, y = random.choice(available_fields)
                x2, y2 = x + length, y
                if {(x2, y2)} & unavailable_fields:
                    x2, y2 = x, y + length
                try:
                    self.try_place_ship(x, y, x2, y2)
                except Exceptions.ShipWronglyPlacedException:
                    pass
                else:
                    unavailable_fields = unavailable_fields | self.__ships_list[-1].get_taken_fields()
                    break

    def try_place_ship(self, x1, y1, x2, y2):
        """
        Próba umieszczenia statku
        :param x1: współrzędna x początku statku
        :param y1: współrzędna y początku statku
        :param x2: współrzędna x końca statku
        :param y2: współrzędna y końca statku
        """
        all_coordinates = {(x, y) for x in range(1, 11) for y in range(1, 11)}
        if not ({(x1, y1)} & all_coordinates and {(x2, y2)} & all_coordinates):
            raise Exceptions.ShipWronglyPlacedException
        elif x2 != x1 and y2 != y1:
            raise Exceptions.ShipWronglyPlacedException
        else:
            if x2 != x1:
                length = abs(x2 - x1) + 1
                if x2 < x1:
                    x1, x2 = x2, x1
            else:
                length = abs(y2 - y1) + 1
                if y2 < y1:
                    y1, y2 = y2, y1
            if self.__ships_to_place.count(length):
                for ship in self.__ships_list:
                    if ship.get_taken_fields() & {(x1, y1)} or (length > 1 and ship.get_taken_fields() & {(x2, y2)}):
                        raise Exceptions.ShipWronglyPlacedException
                s = Ship(x1, y1, x2, y2)
                self.__ships_to_place.pop(self.__ships_to_place.index(length))
                self.__ships_list.append(s)
            else:
                raise Exceptions.ShipWronglyPlacedException

    def reset(self):
        """
        Resetuje atrybuty klasy
        """
        if hasattr(self, 'turn'):
            delattr(self, 'turn')
        if self.__ships_list:
            self.__ships_list.clear()
        if self.__hit_ships:
            self.__hit_ships.clear()
        self.__ships_to_place.clear()
        self.set_ships_to_place()
        if self.__player_shots:
            self.__player_shots.clear()

    def get_competitor_name(self):
        """
        zwraca prywatna zmienna zawierająca nazwę gracza
        :return: __owner : string
        """
        return self.__competitor_name

    def get_ships_list(self):
        """
        zwraca prywatną zmienną __list_of_ships lista zawierająca statki umieszczone na planszy gracza
        :return: __list_of_ships : list
        """
        return self.__ships_list

    def get_ships_to_place(self):
        """
        zwraca prywatną zmienną __ships_to_set informujacą o statkach do ustawienia
        :return: __ships_to_set :set
        """
        return self.__ships_to_place

    def get_my_shots(self):
        """
        zwraca prywatną zmienną __my_shots
        :return: __my_shots :set
        """
        return self.__player_shots

    def ships_to_place_info(self):
        """
        Zwraca informację o aktualnych statkach do rozstawienia
        :return: string
        """
        return Strings.SHIPS_TO_SET_MESSAGE + "\n" + str(self.__ships_to_place)

    def set_ships_to_place(self):
        """
        Przypisuje do zmiennej __ships_to_place liste okrętów do rozstawinia znajdującą się w res.py
        """
        self.__ships_to_place = LIST_OF_SHIPS.copy()

    def take_shot(self, coordinates):
        """
        dodaje do listy __player_shots parę współrzędnych
        :param coordinates: współrzędne x,y oddanego strzału
        """
        self.__player_shots.add(coordinates)

    def drown_check(self):
        """
        Sprawdza czy któryś statków z __list_of_ships nie jest jest pusty
        :return: 1 jeśli pusty, 0 jeśli nie
        """
        for i in range(len(self.__ships_list)):
            if not self.__ships_list[i].get_ship_position():
                self.__ships_list.pop(i)
                return 1
        return 0

    def hit_check(self, x, y):
        """
        Sprawdza czy statek został trafiony
        :param x : współrzędna x wybranego pola
        :param y: współrzędna y wybranego pola
        """
        for ship in self.__ships_list:
            if ship.get_ship_position().count((x, y)):
                i = ship.get_ship_position().index((x, y))
                ship.get_ship_position().pop(i)
                if self.drown_check():
                    raise Exceptions.HitException(Strings.DROWN)
                else:
                    raise Exceptions.HitException(Strings.HIT)
        else:
            raise Exceptions.MissedException

    def determine_possible_coordinates(self):
        """
        Wybiera i zwraca możliwe współrzędne do strzału
        """
        unavailable_coordinates = self.get_drown_ships_taken_fields() | self.__player_shots
        all_coordinates = {(x, y) for x in range(1, 11) for y in range(1, 11)}
        for ship in self.__hit_ships:
            if not ship.drown:
                if hasattr(ship, "horizontal"):
                    if ship.horizontal:
                        coordinates = {zb for zb in ship.get_taken_fields() if zb[1] == ship.get_ship_position()[0][1]}
                    else:
                        coordinates = {zb for zb in ship.get_taken_fields() if zb[0] == ship.get_ship_position()[0][0]}
                else:
                    coordinates = {zb for zb in ship.get_taken_fields() if zb[0] == ship.get_ship_position()[0][0]} | \
                                  {zb for zb in ship.get_taken_fields() if zb[1] == ship.get_ship_position()[0][1]}
                return coordinates - unavailable_coordinates
        return all_coordinates - unavailable_coordinates

    def get_drown_ships_taken_fields(self):
        """
        Zwraca zbiór współrzędnych zajętych przez zatopione okręty
        :return: taken_coordinates
        """
        taken_coordinates = set()
        for ship in self.__hit_ships:
            if ship.drown:
                taken_coordinates = taken_coordinates | ship.get_taken_fields()
        return taken_coordinates

    def ship_detection(self, x, y, name):
        """
        Dodaje statek do listy __hit_ships, lub gdy już się tam znajduje dodaje współrzędne
        :param x: współrzędna x strzelonego pola
        :param y: współrzędna t strzelonego pola
        :param name: stan statku
        :return:
        """
        if self.__hit_ships:
            for ship in self.__hit_ships:
                if {(x, y)} & ship.get_taken_fields():
                    ship.add_ship_coordinate(x, y)
                    ship.set_drown_state(name)
                    return
            s = Ship(x, y, x, y)
            s.set_drown_state(name)
            self.__hit_ships.append(s)
        else:
            s = Ship(x, y, x, y)
            s.set_drown_state(name)
            self.__hit_ships.append(s)


