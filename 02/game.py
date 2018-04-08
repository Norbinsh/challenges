#!python3
# Code Challenge 02 - Word Values Part II - a simple game
# http://pybit.es/codechallenge02.html

from data import DICTIONARY, LETTER_SCORES, POUCH
import random

NUM_LETTERS = 7


# re-use from challenge 01
def calc_word_value(word: str) -> int:
    """Calc a given word value based on Scrabble LETTER_SCORES mapping"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word)


# re-use from challenge 01
def max_word_value(words):
    """Calc the max value of a collection of words"""
    return max(words, key=calc_word_value)

def draw_letters():
    return [POUCH[random.randint(0, len(POUCH) -1)] for num in range(0,7)]

def player_input():
    allowed_letters = draw_letters()
    player_word = input(f"Build the largest valid word using a combination of the following letters:\n{allowed_letters}")
    if all(i in allowed_letters for i in player_word):
        with open(DICTIONARY, "r") as rf:
            if player_word in rf.readlines():
                print("We good!!")
    else:
        print("Letters out of scope were used, please try again")
        player_input()

def main():
    pass


if __name__ == "__main__":
    main()

player_input()