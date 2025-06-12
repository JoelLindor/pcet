import argparse
import logging
import tkinter as tk
from tkinter import messagebox

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def add(x, y):
    """Function that will add the x and y parameters"""
    return x + y


def subtract(x, y):
    """Function that will subtract the x and y parameters"""
    return x - y


def multiply(x, y):
    """Function that will multiply the x and y parameters"""
    return x * y


def divide(x, y):
    """Function that will divide the x and y parameters"""
    if y == 0:
        # If attempting to divide by 0, return the string below.
        return "Error: Division by 0 is impossible."
    else:
        return x / y


def calculate(action, x, y):
    """Function to run the calc from cli"""
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


def perform_operation(action, entry1, entry2, result_label):
    """
    Function that determines which operation is to be performed.
    Determination is based on button click or key bind.
    """

    try:
        x = float(entry1.get())
        y = float(entry2.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numeric values.")
        return

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
        if isinstance(result, str):  # Error message
            messagebox.showerror("Math Error", result)
            return
        message = f"The result of dividing {x} / {y} is: {result}"
    else:
        message = "Invalid operation."

    logger.info(message)
    result_label.config(text=message)

    # Clear the input fields after displaying the result,
    # then move the curser back to the entry1 box.
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry1.focus_set()


def build_gui(on_keypress=None):
    # GUI Setup / Script execution starts here.
    root = tk.Tk()
    root.title("Python GUI Calculator")

    # Add the Label and inputbox for the first number.
    tk.Label(root, text="Enter first number:").grid(row=0, column=0, padx=1, pady=15)
    entry1 = tk.Entry(root)
    entry1.grid(row=0, column=1, padx=10, pady=5)

    # Add the Label and inputbox for the second number.
    tk.Label(root, text="Enter second number:").grid(row=1, column=0, padx=1, pady=15)
    entry2 = tk.Entry(root)
    entry2.grid(row=1, column=1, padx=10, pady=5)

    # Add labels for the results
    result_label = tk.Label(root, text="", fg="blue")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    # Frame the buttons up
    button_frame = tk.Frame(root)
    button_frame.grid(row=2, column=0, columnspan=2, pady=10)

    # Add the Label and display for the result of the operation in the GUI
    result_label = tk.Label(root, text="", fg="blue")
    result_label.grid(row=3, column=0, columnspan=2, pady=10)

    # Button click handling
    def handle(action):
        if on_keypress:
            on_keypress(action)
        else:
            perform_operation(action, entry1, entry2, result_label)

    # Buttons
    actions = [("Add", 1, "Ctrl+A"), ("Subtract", 2, "Ctrl+S"), ("Multiply", 3, "Ctrl+M"), ("Divide", 4, "Ctrl+D")]

    for idx, (label, action, shortcut) in enumerate(actions):
        tk.Button(button_frame, text=label, width=10, command=lambda a=action: handle(a)).grid(row=0, column=idx, padx=5)
        tk.Label(button_frame, text=shortcut).grid(row=1, column=idx)

    # Establish keyboard shortcuts to override pushing the buttons
    root.bind("<Control-a>", lambda _: handle(1))  # Add
    root.bind("<Control-s>", lambda _: handle(2))  # Subtract
    root.bind("<Control-m>", lambda _: handle(3))  # Multiply
    root.bind("<Control-d>", lambda _: handle(4))  # Divide

    # Shortcut labels under buttons
    tk.Label(button_frame, text="Ctrl+A").grid(row=1, column=0, pady=(2, 0))
    tk.Label(button_frame, text="Ctrl+S").grid(row=1, column=1, pady=(2, 0))
    tk.Label(button_frame, text="Ctrl+M").grid(row=1, column=2, pady=(2, 0))
    tk.Label(button_frame, text="Ctrl+D").grid(row=1, column=3, pady=(2, 0))

    return root


def run_gui():
    """Function to build the entire GUI if cli input was not received"""
    root = build_gui()
    root.mainloop()


def main():
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

    if args.gui:
        run_gui()
        return

    action = None
    if args.add:
        action = 1
    elif args.subtract:
        action = 2
    elif args.multiply:
        action = 3
    elif args.divide:
        action = 4

    # If all CLI inputs are provided, run CLI mode
    if action and (args.x is None or args.y is None):
        # This is error handling to inform the user they started with cli args, but did not include them all.
        logger.error("Error: Both --x and --y must be provided for CLI use.")
        return
    elif action and args.x is not None and args.y is not None:
        result = calculate(action, args.x, args.y)
        if isinstance(result, str) and result.startswith("Error"):
            logger.error(result)
        else:
            op = {1: "+", 2: "-", 3: "*", 4: "/"}[action]
            logger.info(f"Result: {args.x} {op} {args.y} = {result}")
    else:
        # Fall back to GUI if CLI args are incomplete
        run_gui()


if __name__ == "__main__":
    main()
