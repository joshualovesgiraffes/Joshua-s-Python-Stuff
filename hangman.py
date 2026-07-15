
import random
import sys
import os

print("------------------")
print("|   Welcome to   |")
print("|     Hangman    |")
print("------------------")

words = ["hangman", "hello", "health", "experience", "table", "chair", "computer", "giraffes"]
word = random.choice(words)

length = len(word)
display = ["_"] * length

length = len(word) - 1

number_of_incorrect = 0
number_of_correct = 0

while True:
    if number_of_correct == length - 1:
        print("Congratulations! You guessed the word: " + word)
        input("Press ENTER to exit.")
        sys.exit()
    if number_of_incorrect == 10:
        print("You have run out of guesses. The word was: " + word)
        input("Press ENTER to exit.")
        sys.exit()
    guess = input("Guess a letter: ").lower()

    if guess not in word:
        print(f"{guess} was not in the word.")
        number_of_incorrect += 1

    if guess in word:
        number_of_correct += 1
        positions = [i for i, letter in enumerate(word) if letter == guess]
        for pos in positions:
            display[pos] = guess
        print(f"{guess} was in the word!")
        print("")
        print("".join(display))
        print("")