import string


class NoDigitError(Exception):
    """Exception raised when a line does not contain any digits."""
    pass


class CalibrationValueFinder():
    
    def find_calibration_value(self, line: str) -> int:

        # Find first digit
        first_digit = None
        for char in line:
            if char in string.digits:
                first_digit = int(char)
                break

        # Make sure string has at least one digit
        if first_digit is None:
            raise NoDigitError()

        # Find second digit
        second_digit = None
        for char in reversed(line):
            if char in string.digits:
                second_digit = int(char)
                break

        return first_digit * 10 + second_digit
    

    def sum_calibration_values(self, lines: list) -> int:
        calibration_values = [self.find_calibration_value(line) for line in lines]

        return sum(calibration_values)
    