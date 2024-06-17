import unittest
from day1 import CalibrationValueFinder, NoDigitError

class TestDay1(unittest.TestCase):

    def setUp(self):
        self.calibration_value_finder = CalibrationValueFinder()


    def test_find_calibration_value(self):
        test_cases = [
            ('1abc2', 12),
            ('pqr3stu8vwx', 38),
            ('a1b2c3d4e5f', 15),
            ('treb7uchet', 77)
        ]

        for line, expected in test_cases:
            with self.subTest(line=line, expected=expected):
                result = self.calibration_value_finder.find_calibration_value(line)
                self.assertEqual(result, expected)

    def test_no_digit(self):
        with self.assertRaises(NoDigitError):
            self.calibration_value_finder.find_calibration_value('nodigit')


    def test_sum_calibration_values(self):
        test_case = ['1abc2', 'pqr3stu8vwx', 'a1b2c3d4e5f', 'treb7uchet']

        self.assertEqual(self.calibration_value_finder.sum_calibration_values(test_case), 142)
    

    def test_sum_txt_input(self):
        with open('day1_input.txt', 'r') as file:
            test_case = file.readlines()
        
        self.assertEqual(self.calibration_value_finder.sum_calibration_values(test_case), 54632)

if __name__ == '__main__':
    unittest.main()
