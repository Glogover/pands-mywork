# random.py
# This program generates a random number between 0 and 100 to guess
# Author: Marcin Kaminski

from random import randint


numberToGuess = 0
attempt = 1
guess = int(input("Please guess the number (between 0 and 100): "))

while( guess != numberToGuess):
    numberToGuess = randint(0, 100)
    #print(f"Hint! {numberToGuess} is the number to guess ")  # Uncomment to check if the program works correctly
    attempt += 1
    guess = int(input(f"Attempt # {attempt}. Please guess again: "))

print("Well done! Yes the number was ", numberToGuess)

