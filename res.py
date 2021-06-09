LIST_OF_SHIPS = [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]


class Strings:
    RESET_GAME_TO_PLAY_AGAIN = "By zagrać ponownie naciśnij Reset"
    COMPUTER_TURN = "Ruch komputera"
    NOW_CHOSE_END = "Teraz wybierz drugi punkt"
    SHIPS_TO_SET_MESSAGE = "Statki do rozmieszczenia:"
    DROWN = "Trafiony zatopiony!"
    HIT = "Trafiony!"
    INSTRUCTION_BUTTON = "Instrukcja"
    WIN = "Gratulacje! Wygrana!"
    LOSE = "Tym razem komputer okazał się lepszy. Następnym razem będzie lepiej!"
    COMPUTER_NAME = "Komputer"
    PLAYER_NAME = "Gracz"
    WINNER_IS = "Wygral: "
    END = "Koniec gry"
    MISS = "Pudło"
    ALREADY_SHOOT = "W to miejsce już strzelałeś"
    NOT_PLAYER_TURN = "Ruch komputera"
    BATTLE_NOT_STARTED = "Aby rozpocząć bitwę naciśnij przycisk Bitwa"
    PLAYER_TURN = "Ruch gracza"
    STARTING_GAME = "Rozpoczynanie gry"
    ALREADY_IN_GAME = "Bitwa jest już rozpoczęta!"
    SHIPS_NOT_PLACED = "Nie rozmieściłeś jeszcze wszystkich statków"
    ALL_SHIPS_SET = "Wszystkie staki rozmieszczone!"
    SHIP_PLACED_SUCCES = "Okręt na pozycji!"
    WRONGLY_PLACED_SHIP = "Nie można rozmieścić okrętu w ten sposób"
    PLAYER_BOARD_LABEL = "Plansza gracza"
    COMPUTER_BOARD_LABEL = "Plansza komputera"
    START_BUTTON = "Bitwa!"
    RESET_BUTTON = "Reset"
    GREETING = "Witaj! Zacznij od rozmieszczenia swoich okrętów."
    INSTRUCTION = "Aby rozmieścić okręt wybierz dwa punkty pomiędzy którymi ma stanąć twój statek. \nOkręty nie mogą " \
                  "się dotykać ani rogami ani bokami. "
    RESET_MESSAGE = "Gra została zresetowana"


class States:
    NORMAL = "normal"
    DISABLED = "disabled"


class Exceptions:
    class CannotStartException(Exception):
        pass

    class ShipWronglyPlacedException(Exception):
        pass

    class ShootingShipException(Exception):
        pass

    class MissedException(ShootingShipException):
        pass

    class HitException(ShootingShipException):
        def __init__(self, name):
            self.name = name


class Colors:
    MAP_COLOR = "#003399"
    SHIP = "black"
    BOARD_LABEL = 'yellow'
    RESET_BUTTON = "yellow"
    BUTTON = "#003399"
    START_BUTTON = "yellow"
    MISS = "#6699ff"
    HIT = 'red'
