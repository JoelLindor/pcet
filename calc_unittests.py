import unittest

import calc


class TestDoaThing(unittest.TestCase):

    def test_empty_string(self):
        self.assertEqual(calc.doathing(""), "Error: You must enter a numeric value.")

    def test_input_with_space(self):
        self.assertEqual(calc.doathing(" 2"), "Error: Your input contained a space.")

    def test_non_digit_input(self):
        self.assertEqual(calc.doathing("Jimmy"), "Error: You can only enter a numeral as an action.")

    def test_number_out_of_range(self):
        self.assertEqual(calc.doathing("5"), "You can only pick from actions 1/2/3/4.")
        self.assertEqual(calc.doathing(0), "You can only pick from actions 1/2/3/4.")

    def test_gibberish_input(self):
        self.assertEqual(calc.doathing("709w283475982w37498qw27"), "Error: You can only enter a numeral as an action.")

    def test_valid_inputs(self):
        self.assertEqual(calc.doathing("1"), {"Valid": 1})
        self.assertEqual(calc.doathing("2"), {"Valid": 2})
        self.assertEqual(calc.doathing("3"), {"Valid": 3})
        self.assertEqual(calc.doathing("4"), {"Valid": 4})

    class TestArithmeticOperations(unittest.TestCase):

        def test_add(self):
            self.assertEqual(calc.add(3, 5), 8)
            self.assertEqual(calc.add(-1, 1), 0)
            self.assertEqual(calc.add(0, 0), 0)

        def test_subtract(self):
            self.assertEqual(calc.subtract(10, 5), 5)
            self.assertEqual(calc.subtract(-1, -1), 0)

        def test_multiply(self):
            self.assertEqual(calc.multiply(4, 5), 20)
            self.assertEqual(calc.multiply(-2, 3), -6)

        def test_divide(self):
            self.assertEqual(calc.divide(10, 2), 5)
            self.assertEqual(calc.divide(5, 2), 2.5)

        def test_divide_by_zero(self):
            self.assertEqual(calc.divide(5, 0), "Error: Division by 0 is impossible dumbass.")


if __name__ == "__main__":
    unittest.main()
