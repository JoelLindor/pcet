import logging

logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: Division by 0 is impossible dumbass."
    else:
        return x / y


def doathing(action):
    """The main function to figure out which equation we are going to be doing"""

    # TODO Put this if loop inside a while loop.
    if " " in str(action):
        return "Error: Your input contained a space."
    elif not str(action).isdigit():
        return "Error: You can only enter a numeral as an action."
    elif not int(action) in range(1, 4):
        return "You can only pick from actions 1/2/3/4."
    else:
        return "Valid"


# Start execution.
if __name__ == "__main__":
    logger.info("This is a Calculator...")
    logger.info("Please select from one of the following functions:")
    logger.info("1. Add")
    logger.info("2. Subtract")
    logger.info("3. Multiply")
    logger.info("4. Divide")
    action = input("Enter the number of the function you wish to perform.\n")

    doathing(action)
