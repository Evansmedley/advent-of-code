import unittest

from day6 import Race, RaceDocument, RaceCalculator


class TestDay6(unittest.TestCase):

    def setUp(self):
        self.race_calc = RaceCalculator()


    def test_race_document_parse(self):
        # Given
        with open("day6_input.txt", 'r') as file:
            input = file.readlines()

        expected_races = [Race(7, 9), Race(15, 40), Race(30, 200)]

        # When
        race_doc = RaceDocument(input)

        # Then
        self.assertEqual(race_doc.races, expected_races)


    def test_find_min_button_press_len_for_win(self):
        # Given
        race = Race(7, 9)
        expected_min = (2, 5)

        # When
        self.race_calc.find_min_button_press_len_for_win(race)

        # Then
        self.assertEqual(race.mins, expected_min)


    def test_find_num_ways_to_win(self):
        # Given
        test_cases = [(Race(7, 9), 4), (Race(3, 20), 0), (Race(2, 1), 1), (Race(30, 200), 9)]

        # When
        for race, expected in test_cases:
            with self.subTest(race=race, expected=expected):
                result = self.race_calc.find_num_ways_to_win(race)

                # Then
                self.assertEqual(result, expected)


    def test_compute_prod_of_ways_to_win_races(self):
        # Given
        with open("day6_input.txt", 'r') as file1:
            input1 = file1.readlines()

        with open("day6_input2.txt", 'r') as file2:
            input2 = file2.readlines()

        test_cases = [
            (RaceDocument(input1), 288),
            (RaceDocument(input2), 1731600)
        ]

        # When
        for race_doc, expected in test_cases:
            with self.subTest(race_doc=race_doc, expected=expected):
                result = self.race_calc.compute_prod_of_ways_to_win_races(race_doc)

                # Then
                self.assertEqual(result, expected)




if __name__ == '__main__':
    unittest.main()
