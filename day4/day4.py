from typing import List
import re

class ScratchCard:

    def __init__(self, card: str):
        self._parse(card)
        

    def _parse(self, card: str):
        split_card = re.split(': | \| ', card)
        self.card_number = split_card[0].split(' ')[1]
        self.my_numbers = [int(num) for num in split_card[2].split(' ') if num]
        self.winning_numbers = [int(num) for num in split_card[1].split(' ') if num]
        


class ScratchCardEvaluator:

    POINTS = {
        True: lambda n: 2**(n-1),
        False: lambda n: 0
    }

    def count_winning_numbers(self, card) -> int:
        return len([num for num in card.my_numbers if num in card.winning_numbers])


    def evaluate_cards(self, cards: List[ScratchCard]) -> int:
        running_sum = 0
        for card in cards:
            running_sum += 2**(num_wins - 1) if (num_wins := self.count_winning_numbers(card)) else 0

        return running_sum
