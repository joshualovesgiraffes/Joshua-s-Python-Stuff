
import random
import sys
import os

print("------------------")
print("|   Welcome to   |")
print("|     Hangman    |")
print("------------------")

words = ("hangman")

word = random.choice(words)

while attempts > 0:
    guess = input("Guess a letter: ")

if guess in word:
    print(f"{guess} was in word!")

