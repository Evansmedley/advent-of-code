import unittest

from day4 import ScratchCardEvaluator, ScratchCard

class TestDay4(unittest.TestCase):

    def setUp(self):
        self.scratch_card_evaluator = ScratchCardEvaluator()


    def test_parse_scratch_card(self):
        card = ScratchCard("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")

        self.assertEqual(card.my_numbers, [83, 86, 6, 31, 17, 9, 48, 53])
        self.assertEqual(card.winning_numbers, [41, 48, 83, 86, 17])


    def test_count_winning_numbers(self):
        test_cases = [
            (ScratchCard("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"), 4),
            (ScratchCard("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83"), 1),
            (ScratchCard("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"), 0)
        ]

        for card, expected in test_cases:
            with self.subTest(card=card, expected=expected):
                result = self.scratch_card_evaluator.count_winning_numbers(card)
                self.assertEqual(result, expected)


    def test_evaluate_cards(self):
        cards = [
            ScratchCard("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53"),
            ScratchCard("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19"),
            ScratchCard("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1"),
            ScratchCard("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83"),
            ScratchCard("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36"),
            ScratchCard("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11")
        ]

        self.assertEqual(self.scratch_card_evaluator.evaluate_cards(cards), 13)


    def test_evaluate_cards_txt_input(self):
        with open("day4_input.txt", 'r') as file:
            cards = [ScratchCard(card) for card in file.readlines()]

        self.assertEqual(self.scratch_card_evaluator.evaluate_cards(cards), 23028)



if __name__ == "__main__":
    unittest.main()