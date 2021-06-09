import unittest
import res
from Battleships import *
import random
from tkinter import *
from res import Strings


class Tests(unittest.TestCase):
    def place_ships_properly_and_start_game(self, game):
        game.place_ship((1, 1))
        game.place_ship((4, 1))
        game.place_ship((1, 3))
        game.place_ship((3, 3))
        game.place_ship((1, 5))
        game.place_ship((3, 5))
        game.place_ship((1, 7))
        game.place_ship((2, 7))
        game.place_ship((1, 9))
        game.place_ship((2, 9))
        game.place_ship((6, 9))
        game.place_ship((7, 9))
        game.place_ship((6, 5))
        game.place_ship((6, 5))
        game.place_ship((10, 1))
        game.place_ship((10, 1))
        game.place_ship((10, 5))
        game.place_ship((10, 5))
        game.place_ship((10, 3))
        game.place_ship((10, 3))
        game.start_game()
        return game

    def test_place_ships_improperly(self):
        root = Tk()
        game = Game(root)
        game.place_ship((1, 1))
        game.place_ship((3, 1))
        game.place_ship((1, 2))
        game.place_ship((3, 2))
        self.assertTrue(Strings.WRONGLY_PLACED_SHIP in game.get_displayed_message())

    def test_place_ships_properly_and_start_game(self):
        root = Tk()
        game = Game(root)
        game = self.place_ships_properly_and_start_game(game)
        self.assertTrue((Strings.STARTING_GAME in game.get_displayed_message()) or
                        (Strings.PLAYER_TURN in game.get_displayed_message()))

    def test_empty_field_shoot(self):
        root = Tk()
        game = Game(root)
        game = self.place_ships_properly_and_start_game(game)
        taken_fields = game.get_computer_ships_coordinates()
        empty_fields = [(x, y) for x in range(1, 11) for y in range(1, 11) if (x, y) not in taken_fields]
        x, y = random.choice(empty_fields)
        game.player_shoot((x, y))
        self.assertTrue(Strings.MISS in game.get_displayed_message())

    def test_ship_hit(self):
        root = Tk()
        game = Game(root)
        game = self.place_ships_properly_and_start_game(game)
        taken_fields = game.get_computer_ships_coordinates()
        x, y = random.choice(taken_fields)
        game.player_shoot((x, y))
        self.assertTrue(Strings.HIT in game.get_displayed_message() or Strings.DROWN in game.get_displayed_message())

    def test_try_shoot_own_ship(self):
        root = Tk()
        game = Game(root)
        game = self.place_ships_properly_and_start_game(game)
        placed_ship_x = 1
        placed_ship_y = 1
        self.assertTrue(game.get_player_board()[placed_ship_x][placed_ship_y]['state'] == States.DISABLED)

    def test_double_empty_field_shoot(self):
        root = Tk()
        game = Game(root)
        game = self.place_ships_properly_and_start_game(game)
        taken_fields = game.get_computer_ships_coordinates()
        empty_fields = [(x, y) for x in range(1, 11) for y in range(1, 11) if (x, y) not in taken_fields]
        x, y = random.choice(empty_fields)
        game.player_shoot((x, y))
        self.assertTrue(game.get_computer_board()[x][y]['state'] == States.DISABLED)

    def test_double_ship_hit(self):
        root = Tk()
        game = Game(root)
        game = self.place_ships_properly_and_start_game(game)
        taken_fields = game.get_computer_ships_coordinates()
        x, y = random.choice(taken_fields)
        game.player_shoot((x, y))
        self.assertTrue(game.get_computer_board()[x][y]['state'] == States.DISABLED)

    def test_place_some_ships_and_reset(self):
        root = Tk()
        game = Game(root)
        game.place_ship((1, 1))
        game.place_ship((4, 1))
        game.place_ship((1, 3))
        game.place_ship((3, 3))
        game.reset_game()
        self.assertTrue(game.get_player_ships_to_place() == res.LIST_OF_SHIPS)

    def test_take_some_shots_then_reset_and_again_take_some_shots(self):
        try:
            root = Tk()
            game = Game(root)
            game = self.place_ships_properly_and_start_game(game)
            taken_fields = game.get_computer_ships_coordinates()
            x, y = random.choice(taken_fields)
            game.player_shoot((x, y))
            x, y = random.choice(taken_fields)
            game.player_shoot((x, y))

            root = Tk()
            game = Game(root)
            game = self.place_ships_properly_and_start_game(game)
            taken_fields = game.get_computer_ships_coordinates()
            x, y = random.choice(taken_fields)
            game.player_shoot((x, y))
            x, y = random.choice(taken_fields)
            game.player_shoot((x, y))
        except Exception:
            self.fail("Unexpected exception occured!")

    def test_win_game(self):
        root = Tk()
        game = Game(root)
        game = self.place_ships_properly_and_start_game(game)
        taken_fields = game.get_computer_ships_coordinates()
        for i in range(len(taken_fields)):
            coordinates = random.choice(taken_fields)
            game.player_shoot(coordinates)
            taken_fields.remove(coordinates)
        self.assertTrue(Strings.RESET_GAME_TO_PLAY_AGAIN in game.get_displayed_message())

    def test_lose_game(self):
        root = Tk()
        game = Game(root)
        game = self.place_ships_properly_and_start_game(game)
        taken_fields = game.get_computer_ships_coordinates()
        empty_fields = [(x, y) for x in range(1, 11) for y in range(1, 11) if (x, y) not in taken_fields]
        while len(game.get_player_ship_list()) > 0:
            coordinates = random.choice(empty_fields)
            game.player_shoot(coordinates)
            empty_fields.remove(coordinates)
        self.assertTrue(Strings.RESET_GAME_TO_PLAY_AGAIN in game.get_displayed_message())


if __name__ == '__main__':
    unittest.main(exit=False)
