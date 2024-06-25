import unittest

from day3 import EngineSchematic, PartFinder

class TestDay3(unittest.TestCase):

    def setUp(self):
        self._part_finder = PartFinder()

    # ENGINE SCHEMATIC TESTS
    def test_schematic_next(self):
        '''
        Test schematic next method and raising of StopIteration upon 
        reaching the end of the schematic.
        '''
        schematic = EngineSchematic(["012", "345"])
        expected = ["0", "1", "2", "3", "4", "5"]

        for val in expected:
            self.assertEqual(next(schematic), val)

        with self.assertRaises(StopIteration):
            next(schematic)


    def test_schematic_goto(self):
        schematic = EngineSchematic(["012", "345"])
        
        self.assertEqual(schematic[1][2], '5')


    def test_schematic_get_current_index(self):
        schematic = EngineSchematic(["012", "345"])
        next(schematic)
        next(schematic)

        self.assertEqual(schematic.get_current_index(), (0, 1))


    # PART NUMBER FINDER TESTS

    def test_get_adjacent_indices(self):
        schematic = EngineSchematic(
            ["467..114..", 
             "...*......", 
             "......#...",
             "617*......",
             ".....+.58.",
             "..592.....",
             "...$.*....",
             ".664.598.."]
        )

        result = self._part_finder.get_adjacent_indices(schematic, [(0, 0), (0, 1), (0, 2)])

        self.assertEqual(
            result, 
            set([(0, 3), (1, 0), (1, 1), (1, 2), (1, 3)])
        )


    def test_check_adjacent_indices(self):
        schematic = EngineSchematic(
            ["467..114..", 
             "...*......", 
             "......#...",
             "617*......",
             ".....+.58.",
             "..592.....",
             "...$.*....",
             ".664.598.."]
        )

        test_cases = [
            ([(0, 0), (0, 1), (0, 2)], True),
            ([(0, 5), (0, 6), (0, 7)], False)
        ]

        for input_indices, expected in test_cases:
            adjacent_indices = self._part_finder.get_adjacent_indices(schematic, input_indices)
            result = self._part_finder.check_adjacent_indices(schematic, adjacent_indices)
            self.assertEqual(result, expected)


    def test_find_part_number(self):
        schematic = EngineSchematic(["......", "...12*", "....9."])

        self.assertEqual(self._part_finder.find_part_number(schematic), 12)
        self.assertEqual(self._part_finder.find_part_number(schematic), 9)
        self.assertEqual(self._part_finder.find_part_number(schematic), None)


    def test_sum_part_numbers(self):
        schematic = EngineSchematic(
            ["467..114..", 
             "...*......", 
             "..35..633.",
             "......#...",
             "617*......",
             ".....+.58.",
             "..592.....",
             "......755.",
             "...$.*....",
             ".664.598.."]
        )

        self.assertEqual(self._part_finder.sum_part_numbers(schematic), 4361)


    def test_sum_part_nums_txt_input(self):
        with open("day3_input.txt", 'r') as file:
            schematic = EngineSchematic(file.readlines())

        self.assertEqual(self._part_finder.sum_part_numbers(schematic), 526404)


if __name__ == '__main__':
    unittest.main()