# Antonita Pratcher
# CIS256 Fall 2025
# EX 4 
# Due: 02 November 2025

"""Program Description: This program is a hangman game. """

import random

# create list of words for game
words = ["apple", "blueberry", "cherry", "date", "elderberry", "fig",
         "guava", "honeydew", "jackfruit", "kiwi", "lemon", "mango", "nectarine,"
         "orange", "peach", "raspberry", "strawberry", "tangerine", "watermelon"]

# store word chosen in a variable
random_word = random.choice(words)

# create list storing random_word in as underscores
underscore_random_word = ['_'] * len(random_word)

# create variables setting max number of tries and variable setting tries for loop
max_try = 8
try_left = max_try

# create list of letters already guesses
user_guess = []

# create loop for game
while try_left > 0 and '_' in underscore_random_word: # for condition, tries are more than zero and there are letters that are still underscores
    print("\nCurrent word: ", end="")
