#!/usr/bin/python3
""" 0-add_integer Module """


def add_integer(a, b=98):
    """
    To Add two integers

    Args:
        a: first integer
        b: second integer

    Returns:
        the addition of two integers
    """
    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    elif type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    else:
        new_a, new_b = int(a), int(b)
        return new_a + new_b
