# guess2.py
# This program prompts the user to guess a number. 
# The program should keep prompting the user to guess the number until the user gets the right on

numberToGuess = 30

guess = int(input("Please guess the number: "))
while guess != numberToGuess:
    if guess < numberToGuess:
      print("too low")
    else:
      print("too high")

    guess = int(input("Please guess again: "))

print("Well done! Yes the number was ", numberToGuess)