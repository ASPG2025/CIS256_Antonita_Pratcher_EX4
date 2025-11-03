# Antonita Pratcher
# CIS256 Fall 2025
# EX 4 Part 3
# Due: 02 November 2025

"""Program Description: This program selects a word that comes from a predefined list 
and says if guesses are correct vs. incorrect """

import random

animal_list = ["alligator", "bear","camel", "dolphin", "elephant", "fox", "giraffe",
               "hyena", "iguana", "jellyfish", "koala", "lion","monkey","owl", "panda",
               "rabbit","squirrel","turtle", "vulture", "whale","zebra"]

secret_animal = random.choice(animal_list)

# introduction to game for user. present list of animals to user
print(f"\nLet's play guess the secret animal!")
print("Here is the list of animals. Guess the selected one!:")
for animal in animal_list:
    print(animal, end=", ")
print("\n")
