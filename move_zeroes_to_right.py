"""Move zeroes"""


def move_zeroes(inputArray):
    """Move zeroes to the rigth

    Args:
        inputArray (String, Int, Boolean): [an array of elements]

    Returns:
        [array]: [an array of the input elements with the zeroes moved to the end]
    """
    returnArray = []
    zeroesCounter = 0

    # check each element

    for element in inputArray:
        # is a zero?
        if '0' == str(element):
            zeroesCounter += 1
        else:
            returnArray.append(element)

    # add the zeroes
    while(zeroesCounter > 0):
        returnArray.append(0)
        zeroesCounter -= 1

    return returnArray
