def find_it(seq):
    values = {}
    # arrange the values in a dictionary
    for x in range(0,len(seq)):
        try:
            values[seq[x]] = (values[seq[x]] +1)

        except KeyError:
            values[seq[x]] = 1

    # extract the odd repeated
    odd_repeated = [key for key, value in values.items() if value % 2 != 0]

    return odd_repeated

