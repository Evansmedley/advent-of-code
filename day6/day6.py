from typing import List, Tuple

import math

class Race:

    def __init__(self, time: int, dist: int):
        self.time = time
        self.dist = dist
        self.mins = ()           # Placeholder


    def __eq__(self, other):
        if not isinstance(other, Race):
            return NotImplemented
        return self.time == other.time and self.dist == other.dist
    

    def __repr__(self) -> str:
        return f"Race(time={self.time}, dist={self.dist})"



class RaceDocument:

    def __init__(self, input: List[str]):
        self.races = []
        self._parse(input)

    
    def _parse(self, input: List[str]) -> None:
        race_times = ([time.strip() for time in input[0].split(' ')[1:] if time])
        race_distances = ([distance.strip() for distance in input[1].split(' ')[1:] if distance])

        for time, distance in zip(race_times, race_distances):
            self.races.append(Race(int(time), int(distance)))



class RaceCalculator:

    def _compute_roots(self, race: Race) -> None:
        # 0 = -1b^2 + tb - d (t = race_length and d = distance)
        # Solve for b with quadratic equation

        a, b, c = -1, race.time, -1 * race.dist

        discriminant = b**2 - 4 * a * c

        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            race.mins = math.ceil(root1 + 0.01), math.floor(root2 - 0.01)
        elif discriminant == 0:
            race.mins = (math.ceil(-1 / (2 * a)),)

    
    def find_min_button_press_len_for_win(self, race: Race) -> None:
        self._compute_roots(race)
    

    def find_num_ways_to_win(self, race: Race) -> int:
        self.find_min_button_press_len_for_win(race)

        # Always going to be a parabola with a max so...
        if len(race.mins) == 2:
            return max(race.mins) - min(race.mins) + 1
        elif len(race.mins) == 1:
            return 1
        else:
            return 0


    def compute_prod_of_ways_to_win_races(self, race_doc: RaceDocument) -> int:
        running_prod = 1
        for race in race_doc.races:
            running_prod *= self.find_num_ways_to_win(race)

        return running_prod



