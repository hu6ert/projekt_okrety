from tkinter import messagebox
from objects import *
import random
from tkinter import *
from res import Strings
from res import Colors


class Game:
    """
    Główna klasa odpowiadająca ze okno gry
    """
    def __init__(self, master):
        """
        Tworzy główne okno programu, ramki, plansze, przyciski, etykiety, dwie instancje klasy Competitor z modułu
        objects, wyświetla napis powitalny
        """
        self.__canvas = Canvas(master, height=700, width=1000)
        self.__canvas.pack()
        self.__main_frame = Frame(master, bg=Colors.MAP_COLOR)
        self.__main_frame.place(relwidth=1, relheight=1)
        self.__message_frame = Frame(self.__main_frame)
        self.__message_frame.place(x=90, y=60, width=820, height=110)
        self.__message_label = Label(self.__message_frame, fg=Colors.BOARD_LABEL, bg=Colors.MAP_COLOR)
        self.__message_label.pack(expand=True, fill=BOTH)
        self.__player_board_frame = Frame(self.__main_frame, bg=Colors.MAP_COLOR)
        self.__player_board_frame.place(x=50, y=200, width=390, height=450)
        self.__computer_board_frame = Frame(self.__main_frame, bg=Colors.MAP_COLOR)
        self.__computer_board_frame.place(x=540, y=200, width=390, height=450)
        self.__player_board = self.create_buttons_board(self.__player_board_frame, 1, 3, self.place_ship)
        self.__computer_board = self.create_buttons_board(self.__computer_board_frame, 1, 3, self.player_shoot)
        self.__player_label = Label(self.__player_board_frame,
                                    height=2,
                                    width=43,
                                    fg=Colors.BOARD_LABEL,
                                    bg=Colors.MAP_COLOR,
                                    text=Strings.PLAYER_BOARD_LABEL)
        self.__player_label.grid(column=0, row=11, columnspan=10, rowspan=2)
        self.__computer_label = Label(self.__computer_board_frame,
                                      height=2,
                                      width=43,
                                      fg=Colors.BOARD_LABEL,
                                      bg=Colors.MAP_COLOR,
                                      text=Strings.COMPUTER_BOARD_LABEL)
        self.__computer_label.grid(column=0, row=11, columnspan=10, rowspan=2)
        self.__reset_button_frame = Frame(self.__main_frame)
        self.__reset_button_frame.place(x=450, y=350, width=80, height=30)
        self.__reset_button = Button(self.__reset_button_frame,
                                     command=lambda: self.reset_game(),
                                     fg=Colors.BOARD_LABEL,
                                     bg=Colors.MAP_COLOR,
                                     justify=CENTER,
                                     text=Strings.RESET_BUTTON)
        self.__reset_button.pack(expand=True, fill=BOTH)
        self.__instruction_button_frame = Frame(self.__main_frame)
        self.__instruction_button_frame.place(x=450, y=400, width=80, height=30)
        self.__instruction_button = Button(self.__instruction_button_frame,
                                           command=lambda: messagebox.showinfo(title=None, message=Strings.INSTRUCTION),
                                           fg=Colors.BOARD_LABEL,
                                           bg=Colors.MAP_COLOR,
                                           justify=CENTER,
                                           text=Strings.INSTRUCTION_BUTTON)
        self.__instruction_button.pack(expand=True, fill=BOTH)
        self.__start_button_frame = Frame(self.__main_frame)
        self.__start_button_frame.place(x=450, y=300, width=80, height=30)
        self.__start_button = Button(self.__start_button_frame,
                                     command=lambda: self.start_game(),
                                     fg=Colors.BOARD_LABEL,
                                     bg=Colors.MAP_COLOR,
                                     justify=CENTER,
                                     text=Strings.START_BUTTON)
        self.__start_button.pack(expand=True, fill=BOTH)
        self.__selected_coordinates = []
        self.__player = Competitor(Strings.PLAYER_NAME)
        self.__computer = Competitor(Strings.COMPUTER_NAME)
        self.display_message(Strings.GREETING + "\n" + self.__player.ships_to_place_info())

    def create_buttons_board(self, frame, h, w, fun):
        """
        Tworzy planszę przycisków (10x10)
        :param frame: ramka na której ma zostać umieszczona siatka
        :param h: wysokość przycisku
        :param w: szerokość przycisku
        :param fun: funkcja wywoływana przez przycisk
        :return: lista przycisków tkinter
        """
        buttons = [None]
        letter_coordinates = "ABCDEFGHIJ"
        for y in range(1, 11):
            Label(frame,
                  text=str(y),
                  fg=Colors.BOARD_LABEL,
                  bg=Colors.MAP_COLOR).grid(row=y, column=0)
            Label(frame,
                  text=letter_coordinates[y - 1],
                  fg=Colors.BOARD_LABEL,
                  bg=Colors.MAP_COLOR).grid(row=0, column=y)

            column_buttons = [None]
            for x in range(1, 11):
                bt = Button(frame,
                            text="",
                            width=w,
                            height=h,
                            bg=Colors.BUTTON,
                            anchor="sw",
                            command=lambda coord_x=y, coord_y=x: fun((coord_x, coord_y)))
                bt.grid(row=x, column=y)
                column_buttons.append(bt)
            buttons.append(column_buttons)
        return buttons

    def start_game(self):
        """
        Rozpoczyna grę. Wywoływana przez przycisk Start
        """
        if self.__player.get_ships_to_place():
            self.display_message(Strings.SHIPS_NOT_PLACED)
            raise Exceptions.CannotStartException
        elif self.__computer.get_ships_list():
            self.display_message(Strings.ALREADY_IN_GAME)
            raise Exceptions.CannotStartException
        self.__computer.place_computer_ships()
        if random.randint(0, 1):
            self.__player.__setattr__("turn", False)
            self.computer_shoot()
            self.display_message(Strings.STARTING_GAME)

        else:
            self.__player.__setattr__("turn", True)
            self.display_message(Strings.STARTING_GAME + "\n" + Strings.PLAYER_TURN)

    def reset_game(self):
        """
        Resetuje gre. Wywoływane przez przycisk Reset
        """
        self.__computer.reset()
        self.__player.reset()
        self.__selected_coordinates.clear()
        for i in range(1, 11):
            for j in range(1, 11):
                self.__player_board[j][i]['bg'] = Colors.BUTTON
                self.__player_board[i][j]['state'] = States.NORMAL
                self.__computer_board[i][j]['bg'] = Colors.BUTTON
                self.__computer_board[i][j]['state'] = States.NORMAL
        self.display_message(Strings.RESET_MESSAGE + "\n" + self.__player.ships_to_place_info())

    def get_player_ships_to_place(self):
        """
        Zwraca statki do rozstawienia dla gracza
        """
        return self.__player.get_ships_to_place()

    def display_message(self, message):
        """
        Wyświetla komunikat w górnej części okna
        :param message: treść komunikatu
        """
        self.__message_label["text"] = message

    def get_displayed_message(self):
        """
        Zwraca aktualnie wyświetlony komunikat
        """
        return self.__message_label["text"]

    def get_computer_ships_coordinates(self):
        """
        Zwraca współrzędne staków komputera
        """
        ships_fields = []
        for ship in self.__computer.get_ships_list():
            ships_fields += ship.get_ship_position()
        return ships_fields

    def get_computer_board(self):
        """
        Zwraca plansze przycisków komputera
        """
        return self.__computer_board

    def get_player_board(self):
        """
        Zwraca plansze przycisków gracza
        """
        return self.__player_board

    def get_player_ship_list(self):
        """
        Zwraca listę statków gracza
        """
        return self.__player.get_ships_list()

    def place_ship(self, coordinate):
        """
        Rozmieszcza statek gracza
        :param coordinate: współrzędne x oraz y przycisku
        """
        if self.__player.get_ships_to_place():
            self.__selected_coordinates.append(coordinate)
            self.display_message(Strings.NOW_CHOSE_END)
            if len(self.__selected_coordinates) == 2:
                x1, y1 = self.__selected_coordinates[0]
                x2, y2 = self.__selected_coordinates[1]
                try:
                    self.__player.try_place_ship(x1, y1, x2, y2)
                except Exceptions.ShipWronglyPlacedException:
                    self.display_message(
                        Strings.WRONGLY_PLACED_SHIP + "\n" + self.__player.ships_to_place_info())
                else:
                    for coordinate in self.__player.get_ships_list()[-1].get_ship_position():
                        self.__player_board[coordinate[0]][coordinate[1]]['bg'] = Colors.SHIP
                        self.__player_board[coordinate[0]][coordinate[1]]['state'] = States.DISABLED
                        self.display_message(Strings.SHIP_PLACED_SUCCES + "\n" + self.__player.ships_to_place_info())
                self.__selected_coordinates.clear()
        else:
            self.display_message(Strings.ALL_SHIPS_SET)

    def computer_shoot(self):
        """
        Wykonuje strzał kopmutera
        """
        possible_shoots = [zb for zb in self.__computer.determine_possible_coordinates()]
        x, y = random.choice(possible_shoots)
        self.__computer.take_shot((x, y))
        try:
            self.__player.hit_check(x, y)
        except Exceptions.MissedException:
            self.__player_board[x][y]['bg'] = Colors.MISS
            self.__player_board[x][y]['state'] = States.DISABLED
            self.__player.__setattr__("turn", True)
            return
        except Exceptions.ShootingShipException as ex:
            self.__player_board[x][y]['bg'] = Colors.HIT
            self.__player_board[x][y]['state'] = States.DISABLED
            self.__computer.ship_detection(x, y, ex.name)
            if len(self.__player.get_ships_list()) != 0:
                self.computer_shoot()
            else:
                self.__player.__setattr__("turn", False)
                self.end_game(self.__computer.get_competitor_name())

    def player_shoot(self, coordinate):
        """
        Wykonuje strzał gracza
        :param coordinate: współrzędne strzału
        """
        if self.__computer.get_ships_to_place() and not hasattr(self.__player, "turn"):
            self.display_message(Strings.BATTLE_NOT_STARTED)
        elif not self.__player.turn:
            self.display_message(Strings.NOT_PLAYER_TURN)
        else:
            x, y = coordinate
            if self.__player.get_my_shots() & {(x, y)}:
                self.display_message(Strings.ALREADY_SHOOT)
                return
            else:
                self.__player.take_shot((x, y))
                try:
                    self.__computer.hit_check(x, y)
                except Exceptions.MissedException:
                    self.__computer_board[x][y]['bg'] = Colors.MISS
                    self.__computer_board[x][y]['state'] = States.DISABLED
                    self.display_message(Strings.MISS)
                    self.__player.__setattr__("turn", False)
                    self.computer_shoot()
                except Exceptions.HitException as e:
                    self.__computer_board[x][y]['bg'] = Colors.HIT
                    self.__computer_board[x][y]['state'] = States.DISABLED
                    self.display_message(str(e.name))
                    if len(self.__computer.get_ships_list()) != 0:
                        pass
                    else:
                        self.__player.__setattr__("turn", False)
                        self.end_game(self.__player.get_competitor_name())

    def end_game(self, name):
        """
        Kończy grę
        :param name: nazwa wygranego
        """
        if name == Strings.COMPUTER_NAME:
            messagebox.showinfo(title=None, message=Strings.LOSE)
            self.display_message(Strings.RESET_GAME_TO_PLAY_AGAIN)
            for ship in self.__computer.get_ships_list():
                for coordinate in ship.get_ship_position():
                    self.__computer_board[coordinate[0]][coordinate[1]]['bg'] = Colors.HIT
                    self.__computer_board[coordinate[0]][coordinate[1]]['state'] = States.DISABLED
        else:
            messagebox.showinfo(title=None, message=Strings.WIN)
            self.display_message(Strings.RESET_GAME_TO_PLAY_AGAIN)
        return


if __name__ == '__main__':
    root = Tk()
    game = Game(root)
    root.mainloop()
