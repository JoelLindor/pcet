import unittest

from calc import doathing


class TestDoaThing(unittest.TestCase):

    def test_input_with_space(self):
        self.assertEqual(doathing(" 2"), "Error: Your input contained a space.")

    def test_non_digit_input(self):
        self.assertEqual(doathing("Jimmy"), "Error: You can only enter a numeral as an action.")

    def test_number_out_of_range(self):
        self.assertEqual(doathing("5"), "You can only pick from actions 1/2/3/4.")
        self.assertEqual(doathing(0), "You can only pick from actions 1/2/3/4.")

    def test_gibberish_input(self):
        self.assertEqual(doathing("709w283475982w37498qw27"), "Error: You can only enter a numeral as an action.")


if __name__ == "__main__":
    unittest.main()
