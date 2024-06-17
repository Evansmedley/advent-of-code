import unittest
from day2 import CubeGame, Handful, Game, Cubes

class TestDay2(unittest.TestCase):

    def setUp(self):
        self.cube_game = CubeGame()


    def test_is_handful_possible(self):
        test_cases = [
            (Handful(4, 3, 0), True),
            (Handful(0, 1, 2), True),
            (Handful(6, 0, 3), True),
            (Handful(20, 6, 8), False),
            (Handful(4, 5, 13), True)
        ]

        for handful, expected in test_cases:
            with self.subTest(handful=handful, expected=expected):
                result = self.cube_game.is_handful_possible(handful)
                self.assertEqual(result, expected)


    def test_is_game_possible(self):
        test_cases = [
            (Game(1, [Handful(4, 3, 0)]), True),
            (Game(2, [Handful(0, 1, 2), Handful(4, 5, 13)]), True),
            (Game(3, [Handful(20, 6, 8), Handful(4, 5, 13)]), False),
            (Game(4, []), True)            # If there are no handfuls, the game is still possible
        ]

        for game, expected in test_cases:
            with self.subTest(game=game, expected=expected):
                result = self.cube_game.is_game_possible(game)
                self.assertEqual(result, expected)

    
    def test_sum_of_possible_game_numbers(self):
        test_case = [
            Game(1, [Handful(4, 0, 3), Handful(1, 2, 6), Handful(0, 2, 0)]),    # Possible
            Game(2, [Handful(0, 2, 1), Handful(1, 3, 4), Handful(0, 1, 1)]),    # Possible
            Game(3, [Handful(20, 8, 6), Handful(4, 13, 5), Handful(1, 5, 0)]),  # Impossible
            Game(4, [Handful(3, 1, 6), Handful(6, 3, 0), Handful(14, 3, 15)]),  # Impossible
            Game(5, [Handful(6, 3, 1), Handful(1, 2, 2)])                       # Possible
        ]

        self.assertEqual(self.cube_game.sum_of_possible_game_numbers(test_case), 1 + 2 + 5)


    def test_with_txt_input(self):
        # TODO

if __name__ == '__main__':
    unittest.main()