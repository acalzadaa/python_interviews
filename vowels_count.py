def get_count(input_str):
    num_vowels = len(list(filter(lambda vowel : vowel if vowel in ['a', 'e', 'i', 'o', 'u'] else "", input_str.lower())))
    return num_vowels
