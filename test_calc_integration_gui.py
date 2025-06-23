import unittest

from calc import build_gui


# This test class focuses on testing each calculator operation individually.
class TestSingleOperationIntegration(unittest.TestCase):
    def test_addition_flow(self):
        # Set up the GUI and unpack all relevant widgets.
        # build_gui returns: root, x_entry, y_entry, add_button, sub_button, mul_button, div_button, result_label
        root, x_entry, y_entry, add_button, sub_button, mul_button, div_button, result_label = build_gui()

        # Insert test values into the input fields.
        x_entry.insert(0, "4")
        y_entry.insert(0, "5")

        # Simulate clicking the "Add" button.
        add_button.invoke()

        # Assert that the result label displays the correct sum.
        self.assertEqual(result_label["text"], "Result: 9.0")

        # Destroy the root window to clean up after the test.
        root.destroy()

    def test_subtraction_flow(self):
        # Set up the GUI and unpack widgets.
        root, x_entry, y_entry, add_button, sub_button, mul_button, div_button, result_label = build_gui()

        # Insert test values.
        x_entry.insert(0, "10")
        y_entry.insert(0, "3")

        # Simulate clicking the "Subtract" button.
        sub_button.invoke()

        # Assert the result label shows the correct difference.
        self.assertEqual(result_label["text"], "Result: 7.0")
        root.destroy()

    def test_multiplication_flow(self):
        # Set up the GUI and unpack widgets.
        root, x_entry, y_entry, add_button, sub_button, mul_button, div_button, result_label = build_gui()

        # Insert test values.
        x_entry.insert(0, "6")
        y_entry.insert(0, "7")

        # Simulate clicking the "Multiply" button.
        mul_button.invoke()

        # Assert the result label shows the correct product.
        self.assertEqual(result_label["text"], "Result: 42.0")
        root.destroy()

    def test_division_flow(self):
        # Set up the GUI and unpack widgets.
        root, x_entry, y_entry, add_button, sub_button, mul_button, div_button, result_label = build_gui()

        # Insert test values.
        x_entry.insert(0, "8")
        y_entry.insert(0, "2")

        # Simulate clicking the "Divide" button.
        div_button.invoke()

        # Assert the result label shows the correct quotient.
        self.assertEqual(result_label["text"], "Result: 4.0")
        root.destroy()


# This test class focuses on testing a sequence of operations in a single flow.
class TestMultiOperationFlow(unittest.TestCase):
    def test_operations_flow(self):
        # Set up the GUI and unpack widgets.
        root, x_entry, y_entry, add_button, sub_button, mul_button, div_button, result_label = build_gui()

        # --- Addition Test ---
        # Clear both entry fields before each operation.
        x_entry.delete(0, "end")
        y_entry.delete(0, "end")
        x_entry.insert(0, "4")
        y_entry.insert(0, "5")
        add_button.invoke()
        # Assert the result label shows the correct sum.
        self.assertEqual(result_label["text"], "Result: 9.0")

        # --- Subtraction Test ---
        x_entry.delete(0, "end")
        y_entry.delete(0, "end")
        x_entry.insert(0, "10")
        y_entry.insert(0, "3")
        sub_button.invoke()
        # Assert the result label shows the correct difference.
        self.assertEqual(result_label["text"], "Result: 7.0")

        # --- Multiplication Test ---
        x_entry.delete(0, "end")
        y_entry.delete(0, "end")
        x_entry.insert(0, "6")
        y_entry.insert(0, "7")
        mul_button.invoke()
        # Assert the result label shows the correct product.
        self.assertEqual(result_label["text"], "Result: 42.0")

        # --- Division Test ---
        x_entry.delete(0, "end")
        y_entry.delete(0, "end")
        x_entry.insert(0, "8")
        y_entry.insert(0, "2")
        div_button.invoke()
        # Assert the result label shows the correct quotient.
        self.assertEqual(result_label["text"], "Result: 4.0")

        # Destroy the root window to clean up after the test.
        root.destroy()


# This allows the test file to be run directly.
if __name__ == "__main__":
    unittest.main()
