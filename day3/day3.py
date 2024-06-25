from typing import List, Tuple, Set

import string


class EngineSchematic:
    def __init__(self, rows: List[str]):
        self._rows = rows
        self._row = None
        self._col = None


    def __iter__(self):
        return self

    def __next__(self) -> str:
        # If row and col are None, set to 0, 0 and return
        if self._row is None and self._col is None:
            self._row, self._col = 0, 0
            return self._rows[self._row][self._col]

        # If at end of string, go to start of next row, otherwise get next char in row
        if self._col + 1 >= len(self._rows[self._row]):
            self._row += 1
            self._col = 0
        else:
            self._col += 1

        # If at end of whole schematic, raise StopIteration
        if self._row >= len(self._rows):
            raise StopIteration

        return self._rows[self._row][self._col]
    
    
    def __getitem__(self, index) -> str:
        return self._rows[index]
    

    def get_current_index(self) -> Tuple[int, int]:
        return self._row, self._col
    

    def __len__(self) -> int:
        return len(self._rows)


class PartFinder():

    SYMBOLS = "@#$%&*+-=/"

    def get_adjacent_indices(self, schematic: EngineSchematic, 
                             digit_indices: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
        adjacent_indices = []

        # Add diagonals
        adjacent_indices.append((digit_indices[0][0] - 1, digit_indices[0][1] - 1))
        adjacent_indices.append((digit_indices[0][0] + 1, digit_indices[0][1] - 1))
        adjacent_indices.append((digit_indices[-1][0] - 1, digit_indices[-1][1] + 1))
        adjacent_indices.append((digit_indices[-1][0] + 1, digit_indices[-1][1] + 1))

        # Add left and right
        adjacent_indices.append((digit_indices[0][0], digit_indices[0][1] - 1))
        adjacent_indices.append((digit_indices[-1][0], digit_indices[-1][1] + 1))

        # Add top and bottom
        for indices in digit_indices:
            adjacent_indices.append((indices[0] - 1, indices[1]))
            adjacent_indices.append((indices[0] + 1, indices[1]))

        return set(
            filter(
                lambda tup: all(x >= 0 for x in tup) and tup[0] < len(schematic) and tup[1] < len(schematic[0]), 
                adjacent_indices)
        )


    def check_adjacent_indices(self, schematic: EngineSchematic, 
                                  adjacent_indices: Set[Tuple[int, int]]) -> bool:
        for r, c in adjacent_indices:
            if schematic[r][c] in self.SYMBOLS:
                return True
            
        return False


    def find_part_number(self, schematic: EngineSchematic) -> int:
        digit_indices = []

        potential_part_number = ""

        try:
            while (c := next(schematic)) not in string.digits:
                pass

            potential_part_number += c
            digit_indices.append(schematic.get_current_index())

            while (c := next(schematic)) in string.digits:
                potential_part_number += c
                digit_indices.append(schematic.get_current_index())
        
        except StopIteration:
            return None
    

        # Get integer version of potential part number
        potential_part_number = int(potential_part_number)

        # Get all indices adjacent to part number
        adjacent_indices = self.get_adjacent_indices(schematic, digit_indices)

        if self.check_adjacent_indices(schematic, adjacent_indices):
            return potential_part_number
        
        return 0


    
    def sum_part_numbers(self, schematic: EngineSchematic) -> int:
        running_sum = 0
        while (part_num := self.find_part_number(schematic)) is not None:
            running_sum += part_num

        return running_sum
