import unittest
from day1 import CalibrationValueFinder, NoDigitError

class TestDay1(unittest.TestCase):

    def setUp(self):
        self.calibration_value_finder = CalibrationValueFinder()


    def test_find_calibration_value(self):
        test_cases = [
            ("1abc2", 12),
            ("pqr3stu8vwx", 38),
            ("a1b2c3d4e5f", 15),
            ("treb7uchet", 77),
            ("two1nine", 29),
            ("eighttwothree", 83),
            ("xyzone4fourt", 14),
            ("4four", 44)
        ]

        for line, expected in test_cases:
            with self.subTest(line=line, expected=expected):
                result = self.calibration_value_finder.find_calibration_value(line)
                self.assertEqual(result, expected)


    def test_no_digit(self):
        with self.assertRaises(NoDigitError):
            self.calibration_value_finder.find_calibration_value("nodigit")


    def test_sum_calibration_values(self):
        test_case = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f", "treb7uchet"]

        self.assertEqual(self.calibration_value_finder.sum_calibration_values(test_case), 142)


    def test_sum_txt_input(self):
        with open("day1_input.txt", "r") as file:
            test_case = file.readlines()
        
        self.assertEqual(self.calibration_value_finder.sum_calibration_values(test_case), 53998)

    
    def test_replace_spelled_out_digits(self):
        test_cases = [
            ("one3", "13"),
            ("4two", "42"),
            ("asdfthreezxcv", "asdf3zxcv"),
            ("four", "4"),
            ("five", "5"),
            ("six", "6"),
            ("seven", "7"),
            ("eight", "8"),
            ("nine", "9"),
            ("oneone", "11"),
            ("eightwo", "8wo"),          # Important!
        ]

        for line, expected in test_cases:
            with self.subTest(line=line, expected=expected):
                result = self.calibration_value_finder.replace_spelled_out_digits(line)
                self.assertEqual(result, expected)
                

    def test_p2(self):
        test_case = (
            [
                "two1nine",
                "eightwothree",
                "abcone2threexyz",
                "xtwone3four",
                "4nineeightseven2",
                "zoneight234",
                "7pqrstsixteen"
            ], 
            281
        )
        self.assertEqual(self.calibration_value_finder.sum_calibration_values(test_case[0]), test_case[1])


if __name__ == "__main__":
    unittest.main()
