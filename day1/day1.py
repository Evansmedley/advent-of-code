import string
import re

from typing import Tuple


class NoDigitError(Exception):
    """Exception raised when a line does not contain any digits."""
    pass


class CalibrationValueFinder():

    DIGIT_SPELLINGS = {
        'one': '1', 
        'two': '2', 
        'three': '3', 
        'four': '4', 
        'five': '5', 
        'six': '6', 
        'seven': '7', 
        'eight': '8',
        'nine': '9'
    }


    def _find_first_spelled_out_digit(self, line: str, start_index: int=0) -> Tuple[str, int]:
        first_spelled_out_digit = (None, len(line))

        for spelled_digit in self.DIGIT_SPELLINGS.keys():
            if (index := line.find(spelled_digit)) < first_spelled_out_digit[1] and index >= 0:
                first_spelled_out_digit = (spelled_digit, index)
        
        return first_spelled_out_digit


    def replace_spelled_out_digits(self, line: str) -> int:

        # For each digit spelling, find the earliest instance of it in the string
        start_index = 0
        while (spelled_digit_to_replace := self._find_first_spelled_out_digit(line, start_index))[1] < len(line):
            line = line[:spelled_digit_to_replace[1]] + self.DIGIT_SPELLINGS[spelled_digit_to_replace[0]] \
                        + line[spelled_digit_to_replace[1] + len(spelled_digit_to_replace[0]):]
            start_index = spelled_digit_to_replace[1] + 1
        
        return line


    def find_calibration_value(self, line: str) -> int:
        line = self.replace_spelled_out_digits(line)
        
        digits = re.findall('[0-9]', line)

        if len(digits) == 0:
            raise NoDigitError()
        
        return int(digits[0]) * 10 + int(digits[-1])


    def sum_calibration_values(self, lines: list) -> int:
        calibration_values = [self.find_calibration_value(line) for line in lines]

        return sum(calibration_values)
    