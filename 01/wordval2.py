from data import DICTIONARY, LETTER_SCORES

with open(DICTIONARY, "r") as read_file:
    word_list = read_file.read().splitlines()

def load_words():
    """Load dictionary into a list and return list"""
    return word_list


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum([LETTER_SCORES[x] for x in word.upper()])


def max_word_value(*args):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    iterateon = word_list if len(args) == 0 else args[0]
    top_dogs = (0, None)
    for word in iterateon:
        if "-" in word:
            word = word.replace("-", "")
        if calc_word_value(word) > top_dogs[0]:
            top_dogs = calc_word_value(word), word
    return top_dogs[1]


if __name__ == "__main__":
    pass  # run unittests to validate
