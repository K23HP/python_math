class NegativeSquareRoot(Exception):
    pass

def calc_square_root(num: int, decimal=3) -> float:
    """This function calculates and returns the square root 
    of the positive integer.

    Args:
        num (int): Positive integer to calculate square root.

    Raises:
        NegativeSquareRoot: Raise error, if the argument is negative.

    Returns:
        float: The square root of the argument.
    """
    if num < 0:
        raise NegativeSquareRoot("No negative number has a square root!")
    else:
        return round(num ** (1/2), decimal)