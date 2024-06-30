import unittest

from day5 import Almanac, Mapping

class TestDay5(unittest.TestCase):

    def setUp(self):
        pass

    def test_parse(self):
        with open("day5_input2.txt", 'r') as file:
            input = file.readlines()

        almanac = Almanac(input)

        self.assertEqual(almanac.seeds, [79, 14, 55, 13])
        self.assertEqual(almanac.seed_soil_map, 
                         [Mapping(50, 98, 2), Mapping(52, 50, 48)])
        self.assertEqual(almanac.soil_fertilizer_map, 
                         [Mapping(0, 15, 37), Mapping(37, 52, 2), Mapping(39, 0, 15)])
        self.assertEqual(almanac.fertilizer_water_map, 
                         [Mapping(49, 53, 8), Mapping(0, 11, 42), Mapping(42, 0, 7), Mapping(57, 7, 4)])
        self.assertEqual(almanac.water_light_map, 
                         [Mapping(88, 18, 7), Mapping(18, 25, 70)])
        self.assertEqual(almanac.light_temp_map, 
                         [Mapping(45, 77, 23), Mapping(81, 45, 19), Mapping(68, 64, 13)])
        self.assertEqual(almanac.temp_humidity_map,
                         [Mapping(0, 69, 1), Mapping(1, 0, 69)])
        self.assertEqual(almanac.humidity_location_map,
                         [Mapping(60, 56, 37), Mapping(56, 93, 4)])


    def test_map_to_locations(self):
        # Given
        with open("day5_input2.txt", 'r') as file:
            input = file.readlines()
        almanac = Almanac(input)
        expected = [82, 43, 86, 35]

        # When
        locations = almanac.map_to_locations()

        # Then
        self.assertEqual(locations, expected)

    
    def test_lowest_location(self):
        # Given
        with open("day5_input2.txt", 'r') as file:
            input = file.readlines()
        almanac = Almanac(input)
        
        # When
        location = almanac.lowest_location()

        # Then
        self.assertEqual(location, 35)


    def test_lowest_location_from_full_input(self):
        # Given
        with open("day5_input.txt", 'r') as file:
            input = file.readlines()
        almanac = Almanac(input)
        
        # When
        location = almanac.lowest_location()

        # Then
        self.assertEqual(location, 51580674)


if __name__ == "__main__":
    unittest.main()
