import random


def generate_random_number(start: int, end: int) -> int:
    """
    Generates a random number between the specified start and end values (inclusive).

    Args:
        start (int): The lower bound of the range.
        end (int): The upper bound of the range.

    Returns:
        int: A random integer between start and end.
    """
    return random.randint(start, end)