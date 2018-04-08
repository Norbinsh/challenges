from data import DICTIONARY, LETTER_SCORES
import time
from typing import Any

start_time = time.time()

def load_words() -> list:
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, "r") as f:
        return [line.rstrip("\n") for line in f]

def calc_word_value(word: str) -> int:
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    # place_holder = 0
    # for letter in word:
    #     if letter.isalpha():
    #         place_holder += LETTER_SCORES[letter.capitalize()]
    # return place_holder
    return sum(LETTER_SCORES[letter.upper()] for letter in word if letter.isalpha())


def max_word_value(words_arg: Any=None) -> str:
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""

    if words_arg is None:
        return max(load_words(), key=calc_word_value)
    # temp_max = 0
    # max_word = None
    # if words_arg is None:
    #     word_list = load_words()
    #     for word in word_list:
    #         current_word_value = calc_word_value(word)
    #         if current_word_value > temp_max:
    #             temp_max = current_word_value
    #             max_word = word
    #     return max_word
    else:
        temp_max = 0
        for word in words_arg:
            current_word_value = calc_word_value(word)
            if current_word_value > temp_max:
                temp_max = current_word_value
        return word




if __name__ == "__main__":
    pass # run unittests to validate

# print(f"time taken: {time.time() - start_time}")