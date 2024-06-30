import re

from typing import List


class Mapping():

    def __init__(self, dest: int, source: int, range: int):
        self._source = source
        self._dest = dest
        self._range = range


    def __contains__(self, val: int) -> bool:
        return self._source <= val < self._source + self._range
    

    def __repr__(self) -> str:
        return str(f'({self._source}, {self._dest}, {self._range})')
    

    def __eq__(self, other):
        if not isinstance(other, Mapping):
            return NotImplemented
        return self._source == other._source and self._dest == other._dest and self._range == other._range


    def map(self, val: int) -> int:
        if val in self:
            return val - self._source + self._dest
        else:
            return None



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


    def _map(self, mappings: List[Mapping], val: int) -> int:
        for mapping in mappings:
            if (mapped_val := mapping.map(val)) is not None:
                return mapped_val
            
        return val


    def map_seed_to_location(self, seed: int) -> int:

        # Seed -> soil
        soil = self._map(self.seed_soil_map, seed)

        # Soil -> fertilizer
        fertilizer = self._map(self.soil_fertilizer_map, soil)

        # Fertilizer -> water
        water = self._map(self.fertilizer_water_map, fertilizer)

        # Water -> light
        light = self._map(self.water_light_map, water)

        # Light -> temp
        temp = self._map(self.light_temp_map, light)

        # Temp -> humidity
        humidity = self._map(self.temp_humidity_map, temp)

        # Humidity -> location
        return self._map(self.humidity_location_map, humidity)


    def map_to_locations(self) -> List[int]:
        return [self.map_seed_to_location(seed) for seed in self.seeds]


    def lowest_location(self) -> int:
        return min(self.map_to_locations())
    
