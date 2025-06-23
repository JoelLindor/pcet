import argparse
import logging
import tkinter as tk
from tkinter import messagebox

# Set up logging for CLI output and debugging.
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)

# --- Calculator Operation Functions ---


def add(x, y):
    """Return the sum of x and y."""
    return x + y


def subtract(x, y):
    """Return the difference of x and y."""
    return x - y


def multiply(x, y):
    """Return the product of x and y."""
    return x * y


def divide(x, y):
    """Return the quotient of x and y, or an error message if dividing by zero."""
    if y == 0:
        # Division by zero is not allowed.
        return "Error: Division by 0 is impossible."
    else:
        return x / y


def calculate(action, x, y):
    """
    Perform the calculation based on the action code.
    action: 1=add, 2=subtract, 3=multiply, 4=divide
    Returns the result or an error message.
    """
    if action == 1:
        return add(x, y)
    elif action == 2:
        return subtract(x, y)
    elif action == 3:
        return multiply(x, y)
    elif action == 4:
        return divide(x, y)
    else:
        return "Invalid operation."


# --- GUI Operation Handler ---


def perform_operation(action, entry1, entry2, result_label):
    """
    Determine which operation to perform based on user input (button or key).
    Reads values from entry1 and entry2, performs the operation, and updates result_label.
    Handles input validation and error display.
    """
    try:
        # Attempt to convert user input to floats.
        x = float(entry1.get())
        y = float(entry2.get())
    except ValueError:
        # Show an error dialog if input is not numeric.
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
        return

    # Perform the selected operation and prepare a message for logging.
    if action == 1:
        result = add(x, y)
        message = f"The result of adding {x} + {y} is: {result}"
    elif action == 2:
        result = subtract(x, y)
        message = f"The result of subtracting {x} - {y} is: {result}"
    elif action == 3:
        result = multiply(x, y)
        message = f"The result of multiplying {x} * {y} is: {result}"
    elif action == 4:
        result = divide(x, y)
        if isinstance(result, str):  # Error message from divide
            messagebox.showerror("Math Error", result)
            return
        message = f"The result of dividing {x} / {y} is: {result}"
    else:
        message = "Invalid operation."

    # Log the operation result to the console.
    logger.info(message)
    # Update the result label in the GUI.
    result_label.config(text=f"Result: {result}" if not isinstance(result, str) else result)

    # Clear the input fields and set focus back to the first entry.
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry1.focus_set()


# --- GUI Construction Function ---


def build_gui(on_keypress=None):
    """
    Build and return the calculator GUI.
    Returns references to all widgets needed for testing.
    Optionally accepts an on_keypress callback for custom key handling (used in tests).
    """
    root = tk.Tk()
    root.title("Python GUI Calculator")

    # Label and input for the first number.
    tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=1, pady=15)
    entry1 = tk.Entry(root)
    entry1.grid(row=0, column=1, padx=10, pady=5)

    # Label and input for the second number.
    tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=1, pady=15)
    entry2 = tk.Entry(root)
    entry2.grid(row=1, column=1, padx=10, pady=5)

    # Label to display results.
    result_label = tk.Label(root, text="", fg="blue")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    # Frame to hold operation buttons.
    button_frame = tk.Frame(root)
    button_frame.grid(row=2, column=0, columnspan=2, pady=10)

    # Internal handler to call either the test callback or the real operation.
    def handle(action):
        if on_keypress:
            on_keypress(action)
        else:
            perform_operation(action, entry1, entry2, result_label)

    # Create operation buttons and assign them to variables for access in tests.
    add_button = tk.Button(button_frame, text="Add", width=10, command=lambda: handle(1))
    sub_button = tk.Button(button_frame, text="Subtract", width=10, command=lambda: handle(2))
    mul_button = tk.Button(button_frame, text="Multiply", width=10, command=lambda: handle(3))
    div_button = tk.Button(button_frame, text="Divide", width=10, command=lambda: handle(4))

    # Place the buttons in the button frame.
    add_button.grid(row=0, column=0, padx=5)
    sub_button.grid(row=0, column=1, padx=5)
    mul_button.grid(row=0, column=2, padx=5)
    div_button.grid(row=0, column=3, padx=5)

    # Add shortcut labels under each button for user reference.
    tk.Label(button_frame, text="Ctrl+A").grid(row=1, column=0, pady=(2, 0))
    tk.Label(button_frame, text="Ctrl+S").grid(row=1, column=1, pady=(2, 0))
    tk.Label(button_frame, text="Ctrl+M").grid(row=1, column=2, pady=(2, 0))
    tk.Label(button_frame, text="Ctrl+D").grid(row=1, column=3, pady=(2, 0))

    # Bind keyboard shortcuts to the corresponding operations.
    root.bind("<Control-a>", lambda _: handle(1))  # Add
    root.bind("<Control-s>", lambda _: handle(2))  # Subtract
    root.bind("<Control-m>", lambda _: handle(3))  # Multiply
    root.bind("<Control-d>", lambda _: handle(4))  # Divide

    # Return all widgets needed for testing and automation.
    return root, entry1, entry2, add_button, sub_button, mul_button, div_button, result_label


# --- GUI Runner ---


def run_gui():
    """
    Launch the calculator GUI.
    This is called if the user does not provide complete CLI arguments or uses --gui.
    """
    root, *_ = build_gui()
    root.mainloop()


# --- CLI and Main Entrypoint ---


def main():
    """
    Main entrypoint for the calculator.
    Parses command-line arguments and decides whether to run in CLI or GUI mode.
    """
    parser = argparse.ArgumentParser(description="Calculator - CLI or GUI")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--add", action="store_true", help="Add x and y")
    group.add_argument("--subtract", action="store_true", help="Subtract y from x")
    group.add_argument("--multiply", action="store_true", help="Multiply x and y")
    group.add_argument("--divide", action="store_true", help="Divide x by y")
    parser.add_argument("--x", type=float, help="First number")
    parser.add_argument("--y", type=float, help="Second number")
    parser.add_argument("--gui", action="store_true", help="Force GUI mode")

    args = parser.parse_args()

    # If --gui is specified, always launch the GUI.
    if args.gui:
        run_gui()
        return

    # Determine which operation to perform based on CLI flags.
    action = None
    if args.add:
        action = 1
    elif args.subtract:
        action = 2
    elif args.multiply:
        action = 3
    elif args.divide:
        action = 4

    # If an operation is specified but x or y is missing, show an error.
    if action and (args.x is None or args.y is None):
        logger.error("Error: Both --x and --y must be provided for CLI use.")
        return
    # If all CLI arguments are present, perform the calculation and print the result.
    elif action and args.x is not None and args.y is not None:
        result = calculate(action, args.x, args.y)
        if isinstance(result, str) and result.startswith("Error"):
            logger.error(result)
        else:
            op = {1: "+", 2: "-", 3: "*", 4: "/"}[action]
            logger.info(f"Result: {args.x} {op} {args.y} = {result}")
    else:
        # If not enough CLI arguments, fall back to GUI mode.
        run_gui()


# --- Script Entrypoint ---

if __name__ == "__main__":
    main()
