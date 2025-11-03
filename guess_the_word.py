# Antonita Pratcher
# CIS256 Fall 2025
# EX 4 
# Due: 02 November 2025

"""Program Description: This program is a hangman game. """

import random

# create list of words for the game
words = ["apple", "blueberry", "cherry", "date", "elderberry", "fig",
         "guava", "honeydew", "jackfruit", "kiwi", "lemon", "mango", "nectarine",
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

# introduction to game for user
print(f"\nLet's play guess the fruit!")

# create loop for game
while try_left > 0 and '_' in underscore_random_word: # for condition, tries are more than zero and there are letters that are still underscores
    print("\nCurrent word: ", end="")

    for letter in underscore_random_word: # prints the guessed letter
        print(letter, end=" ")
    print()  # skip a line

    print("Guessed letters: ", end="") # prints all guessed letters
    for letter in user_guess:
        print(letter, end=" ")
    print()  # skip a line

    print(f"Tries left: {try_left}") # lets user know number of tries left

    # stores the user's guess in a variable ensuring input is lowercase
    guess = input("Guess a letter: ").lower()

# add letter to list of tried letters
    user_guess.append(guess)

    # loop affirming that the letted tried is in word. loop circles through random word
    if guess in random_word:
        print(f"One step closer! '{guess}' is in the word!")
        for point in range(len(random_word)):
            if random_word[point] == guess:
                underscore_random_word[point] = guess 
    else:
        print(f"Please try again.'{guess}' is not in the word.")
        try_left -= 1 # counter that reduces number of tries left when letter is incorrectly guessed

# confirms if user successfully guessed word 
if '_' not in underscore_random_word:
    print(f"\nCongratulations! You correctly guessed: {random_word}")
else:
    print(f"\nSorry, you've run out of tries. The word was: {random_word}")