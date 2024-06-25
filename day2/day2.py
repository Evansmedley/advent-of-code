from typing import List
from enum import Enum

class Cubes(Enum):
    RED = 12
    GREEN = 13
    BLUE = 14


class Handful():
    '''
    A handful consists of a number of red, blue and green cubes.
    '''
    def __init__(self, red: int, green: int, blue: int) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    def __repr__(self):
        return f'red: {self.red}, green: {self.green}, blue: {self.blue}'


class Game():
    '''
    A game consists of a number of handfuls and is identified by its game number.
    '''
    def __init__(self, number: int, handfuls: List[Handful]) -> None:
        self.number = number
        self.handfuls = handfuls

    def __repr__(self):
        return f'number: {self.number}, handfuls={[handful for handful in self.handfuls]}'


class CubeGame:

    def is_handful_possible(self, handful: Handful) -> bool:
        '''
        Given a handful, is it possible with the given number of cubes?
        '''
        return handful.red <= Cubes.RED.value and handful.green <= Cubes.GREEN.value \
            and handful.blue <= Cubes.BLUE.value

    def is_game_possible(self, game: Game) -> bool:
        '''
        Given a number of handfuls, are they all possible with the given number of cubes?
        '''
        for handful in game.handfuls:
            if not self.is_handful_possible(handful):
                return False
            
        return True

    def sum_of_possible_game_numbers(self, games: List[Game]) -> int:
        '''
        Given a number of games, what is the sum of their corresponding game numbers.
        '''
        sum_game_numbers = 0
        for game in games:
            if self.is_game_possible(game):
                sum_game_numbers += game.number

        return sum_game_numbers
