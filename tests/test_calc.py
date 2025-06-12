import sys
import os
import unittest
from unittest.mock import patch

# Adjust path to allow importing from the parent directory
# Ensures that Python can find 'calc.py' to import its functions
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importing all the functions we're going to test from calc.py
from calc import add, subtract, multiply, divide, doathing


# Creating a Test Class inheriting from unittest.TestCase
# Each method in this class is a separate test case
class TestCal(unittest.TestCase):

    # Testing the add function directly
    def test_add(self):
        # Verifying that adding 2 and 3 results in 5
        self.assertEqual(add(2, 3), 5)

    # Testing the subtract function directly
    def test_subtract(self):
        # Ensuring that subtracting 3 from 5 results in 2
        self.assertEqual(subtract(5, 3), 2)

    # Testing the multiply function directly
    def test_multiply(self):
        # Checking that multiplying 2 by 3 yields 6
        self.assertEqual(multiply(2, 3), 6)

    # Testing the divide function directly
    def test_divide(self):
        # Ensuring division of 6 by 3 gives 2
        self.assertEqual(divide(6, 3), 2)
        # Testing division by zero case
        self.assertEqual(divide(5, 0), "Error: Division by 0 is impossible dumbass.")


# The @patch decorator from Python's unittest.mock library temporarily replaces a specified object, such as a function,
# with a mock version during a test, enabling controlled simulation of interactions like user inputs or external calls.
# A decorator in Python is simply a special function that modifies or enhances another function’s behavior by wrapping
# around it, without altering the original function’s internal code.

# _mock_input is a Python convention to clearly indicate to both humans and linters that the parameter is intentionally unused.

    # Mocking user input for an "addition" scenario in doathing()
    @patch('builtins.input', side_effect=['1', '10', '5'])
    def test_doathing_add(self, _mock_input):
        # User selects '1' (add), then inputs '10' and '5'
        self.assertEqual(doathing(), 15)

    # Mocking user input for a "subtraction" scenario in doathing()
    @patch('builtins.input', side_effect=['2', '10', '5'])
    def test_doathing_subtract(self, _mock_input):
        # User selects '2' (subtract), then inputs '10' and '5'
        self.assertEqual(doathing(), 5)

    # Mocking user input for a "multiplication" scenario in doathing()
    @patch('builtins.input', side_effect=['3', '10', '5'])
    def test_doathing_multiply(self, _mock_input):
        # User selects '3' (multiply), then inputs '10' and '5'
        self.assertEqual(doathing(), 50)

    # Mocking user input for a "division" scenario in doathing()
    @patch('builtins.input', side_effect=['4', '10', '2'])
    def test_doathing_divide(self, _mock_input):
        # User selects '4' (divide), then inputs '10' and '2'
        self.assertEqual(doathing(), 5)

    # Mocking user input for division by zero in doathing()
    @patch('builtins.input', side_effect=['4', '10', '0'])
    def test_doathing_divide_by_zero(self, _mock_input):
        # User selects '4' (divide), then attempts division by zero
        self.assertEqual(doathing(), "Error: Division by 0 is impossible dumbass.")

    # Mocking invalid (non-numeric) user input for action selection in doathing()
    @patch('builtins.input', side_effect=['a'])
    def test_doathing_invalid_input(self, _mock_input):
        # User inputs a non-numeric character, testing error handling
        self.assertEqual(doathing(), "Error: Non-numeric action")

    # Mocking user input for an out-of-range action selection in doathing()
    @patch('builtins.input', side_effect=['5'])
    def test_doathing_out_of_range_input(self, _mock_input):
        # User inputs '5', which is outside the valid range (1-4)
        self.assertEqual(doathing(), "Error: Action out of range")


# Running the tests when this script is executed directly
if __name__ == "__main__":
    unittest.main()
