# Antonita Pratcher
# CIS256 Fall 2025
# EX 4 Part 3
# Due: 02 November 2025

"""Program Description: This program selects a word that comes from a predefined list 
and says if guesses are correct vs. incorrect """

import random

# list of animals that will be used 
animal_list = ["alligator", "bear","camel", "dolphin", "elephant", "fox", "giraffe",
               "hyena", "iguana", "jellyfish", "koala", "lion","monkey","owl", "panda",
               "rabbit","squirrel","turtle", "vulture", "whale","zebra"]

# program randomly chooses an animal from list
secret_animal = random.choice(animal_list)

# introduction to game for user. present the list of animals to user
print(f"\nLet's play, 'Guess the secret animal'!")
print("Here is the list of animals. Guess the selected one!:\n")
for animal in animal_list:
    print(animal, end=", ")
print("\n")

# sets a variable for the number of tries to be used ain a counter
tries_left = 8

# while loop that will circle through until tries_left = 0 or animal is guessed
while tries_left > 0:
    print(f"\nYou have {tries_left} tries.")
    guess = input("Guess the animal - no hints!: ").lower()

# conditional statement stored in loop. If animal is correctly guessed, stop program, otherwise, continue and reduce counter -1
    if guess == secret_animal:
        print(f"Congratulations!! You guessed correctly! The secret animal is'{secret_animal}'.")
        break
    else:
        print(f"Sorry, {guess} is not the secret animal. Please try again!")
        tries_left -= 1

# once user runs out of tries, reveal secret animal to user
if tries_left == 0:
    print(f"\nSorry, you've run out of tries. The secret animal was '{secret_animal}'.")