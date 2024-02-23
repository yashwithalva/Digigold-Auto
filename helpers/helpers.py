import random, string
from datetime import datetime


def randomword(length) -> str:
    """
    Generates a random word of fixed length
    Args:
        length: length of the random word

    Returns:
        str: Random word
    """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def add_log(message, verbose):
    """
    Prints a message in the command prompt
    Args:
        message: Log message
        verbose: INFO, DEBUG, WARNING, ERROR
    """
    print(f'{verbose} : [{datetime.now()}] >> [MESSAGE]: {message}\n')
