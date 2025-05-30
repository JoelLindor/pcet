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

    if not action:
        return "Error: You must enter a numeric value."
    elif " " in str(action):
        return "Error: Your input contained a space."
    elif "." in str(action):
        return "Error: Your input contained a decimal point."
    elif "-" in str(action):
        return "Error: Your input contained a negative value"
    elif not str(action).isdigit():
        return "Error: You can only enter a numeral as an action."
    elif not int(action) in range(1, 5):
        return "You can only pick from actions 1/2/3/4."
    else:
        # Changing this to a dict object for the purpose of testing the results with unittests.
        return {"Valid": int(action)}


def get_inputs(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            logger.error("Error: Please enter a valid number.")


# Start execution.
if __name__ == "__main__":
    logger.info("This is a Calculator...")
    logger.info("Please select from one of the following functions:")
    logger.info("1. Add")
    logger.info("2. Subtract")
    logger.info("3. Multiply")
    logger.info("4. Divide")

    # Use a while loop to make sure the action function is a valid operation.
    while True:
        action = input("Enter the number of the function you wish to perform.\n")
        result = doathing(action)
        if isinstance(result, dict) and "Valid" in result:
            action = result.get("Valid")
            break  # break out of the loop when we know the action is valid.
        else:
            logger.info(result)

    # Nuking the try/except and turning the inputs into another function, so i can loop
    # them for valid input just like the action.
    x = get_inputs("Enter the first number: ")
    y = get_inputs("Enter the second number: ")

    # Perform the selected operation:
    # Add
    if action == 1:
        logger.info(f"Result: {add(x, y)}")
    # Subtract
    elif action == 2:
        logger.info(f"Result: {subtract(x, y)}")
    # Multiply
    elif action == 3:
        logger.info(f"Result: {multiply(x, y)}")
    # Divide
    elif action == 4:
        logger.info(f"Result: {divide(x, y)}")
    # Close If/Else statement because well, I can?
    else:
        logger.error(
            "How did you even get to this line? Action should never be a value other than 1-4! "
            "But this is an else statement to close the if loop."
        )
