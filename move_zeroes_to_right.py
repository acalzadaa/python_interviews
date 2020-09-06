"""Move zeroes"""


def move_zeroes(inputArray):
    """Move zeroes to the rigth

    Args:
        inputArray (String, Int, Boolean): [an array of elements]

    Returns:
        [array]: [an array of the input elements with the zeroes moved to the end]
    """
    returnArray = [element for element in inputArray if (type(element) is str or str(element).startswith("0") == False) ]
    return returnArray + [0] * (len(inputArray) - len(returnArray))
