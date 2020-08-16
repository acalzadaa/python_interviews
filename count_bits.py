""" Write a function that takes an integer as input, and returns the number of bits that are equal to one
    in the binary representation of that number. You can guarantee that input is non-negative.

    Example: The binary representation of 1234 is 10011010010, so the function should return 5 in this case
"""
def bits_original(n):
    """First draft, create a function using FOR, IF, etc

    Args:
        value (int): an integer value to convert

    Returns:
        [int]: [the number of 1's in the binary representation of the integer]
    """
    binary_value = '{0:b}'.format(n)
    return_value = []

    for num in binary_value:
        if num == "1":
            return_value.append(num)
    return len(return_value)


def bits(n):
    """The lambda version of the original version

    Args:
        value ([int]): an integer number to be converted to binary

    Returns:
        int: the total of 1's in the binary representation of the integer
    """
    return len(list(filter(lambda num : num if num == "1" else "", '{0:b}'.format(n) )))

