#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
import random

NUM_LETTERS = 7


def calc_word_value(word: str) -> int:
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


def max_word_value(words):
    """Calc the max value of a collection of words"""
    print(words)
    return max(words, key=calc_word_value)


def draw_letters():
    return [POUCH[random.randint(0, len(POUCH) - 1)] for _ in range(0, 7)]


def player_input():
    allowed_letters = draw_letters()
    player_word = input(
        f"Build the largest valid word using a combination of the following letters:\n{allowed_letters}")
    if all(i.upper() in allowed_letters for i in player_word):
        if player_word in DICTIONARY:
            print(f"Returning {player_word}")
        else:
            print("There's a problem with your word choice, please try again")
            main()
    else:
        print("There's a problem with your word choice, please try again")
        main()
    return player_word, calc_word_value(player_word)


def optimal_word(user_letters, word):
    if set(user_letters).issuperset(set(list(word))):
        return word
    else:
        return False



def main():
    potential_optimal_words = {}
    user_word_choice = player_input()
    for word in DICTIONARY:
        if optimal_word(user_word_choice[0], word):
            potential_optimal_words[word] = calc_word_value(word)
    max_word = max_word_value(wr for wr in potential_optimal_words.keys())
    print("user", user_word_choice[0], calc_word_value(user_word_choice[0]))
    print("max", max_word, calc_word_value(max_word))
    print(f"you scored {calc_word_value(user_word_choice[0]) / calc_word_value(max_word)}")


if __name__ == "__main__":
    main()

"""
Build the largest valid word using a combination of the following letters:
['R', 'R', 'T', 'W', 'A', 'A', 'S']sa
Returning sa
<generator object main.<locals>.<genexpr> at 0x03292A80>
user sa 2
max sasa 4
you scored 0.5

Process finished with exit code 0
"""