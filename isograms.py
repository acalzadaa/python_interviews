# An isogram is a word that has no repeating letters, consecutive or non-consecutive.
# Implement a function that determines whether a string that contains only letters is an isogram.
# Assume the empty string is an isogram. Ignore letter case.

def is_isogram(string):
    return (True if len(list(filter(lambda letter: letter if string.lower().count(letter) > 1 else "", string))) == 0 else False)

