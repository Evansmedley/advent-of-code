import re

from typing import List


class Mapping():

    def __init__(self, source: int, dest: int, range: int):
        self._source = source
        self._dest = dest
        self._range = range


    def __contains__(self, val: int) -> bool:
        return self._source <= val < self._source + self._range
    

    def map(self, val: int) -> int:
        return val - self._source + self._dest
    

    def __repr__(self) -> str:
        return str(f'({self._source}, {self._dest}, {self._range})')
    

    def __eq__(self, other):
        if not isinstance(other, Mapping):
            return NotImplemented
        return self._source == other._source and self._dest == other._dest and self._range == other._range

    


class Almanac():

    def __init__(self, input: List[str]):
        self._parse(input)


    def _parse(self, input: List[str]) -> None:
        # Split list on empty str to separate sections
        sections = ''.join(input).split('\n\n')

        # Get seeds
        self.seeds = [int(seed) for seed in sections[0].split(': ')[1].split(' ')]

        pattern = r"(\d+ \d+ \d+)"

        seed_soil_matches = [list(map(int, match.split(' '))) for match in re.findall(pattern, sections[1])]
        self.seed_soil_map = [Mapping(match[0], match[1], match[2]) for match in seed_soil_matches]

        soil_fertilizer_matches = [list(map(int, match.split(' '))) for match in re.findall(pattern, sections[2])]
        self.soil_fertilizer_map = [Mapping(match[0], match[1], match[2]) for match in soil_fertilizer_matches]
        
        fertilizer_water_matches = [list(map(int, match.split(' '))) for match in re.findall(pattern, sections[3])]
        self.fertilizer_water_map = [Mapping(match[0], match[1], match[2]) for match in fertilizer_water_matches]

        water_light_matches = [list(map(int, match.split(' '))) for match in re.findall(pattern, sections[4])]
        self.water_light_map = [Mapping(match[0], match[1], match[2]) for match in water_light_matches]

        light_temp_matches = [list(map(int, match.split(' '))) for match in re.findall(pattern, sections[5])]
        self.light_temp_map = [Mapping(match[0], match[1], match[2]) for match in light_temp_matches]

        temp_humidity_matches = [list(map(int, match.split(' '))) for match in re.findall(pattern, sections[6])]
        self.temp_humidity_map = [Mapping(match[0], match[1], match[2]) for match in temp_humidity_matches]

        humidity_location_matches = [list(map(int, match.split(' '))) for match in re.findall(pattern, sections[7])]
        self.humidity_location_map = [Mapping(match[0], match[1], match[2]) for match in humidity_location_matches]