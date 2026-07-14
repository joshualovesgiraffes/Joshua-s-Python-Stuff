import random
import sys
import os

while True:
    options = ("rock", "paper", "scissors", "abort")
    computeroptions = ("rock", "paper", "scissors")

    print("------------------")
    print("|   Welcome to   |")
    print("|      RPS       |")
    print("------------------")

    computer = random.choice(computeroptions)
    player = input("Enter a choice (rock, paper, scissors, abort): ")

    while player not in options:
        print(colored("Please enter a valid input.", "yellow"))
        player = input("Enter a choice (rock, paper, scissors, abort): ")

    # idk why i added this, idk a failsafe i guess
    if computer not in options:
        print("[RARE BUG] We have encountered a system error of the computer not choosing inside options.")
        input("Press ENTER to confirm abort.")
        if abort == "":
            sys.exit()

    if player == 'abort':
        abort = input("Press ENTER to confirm abort.", "red")

    if abort == "":
            sys.exit()

    if player != "abort" and computer in options:
        print("")
        print(f"Player: {player}")
        print(f"Computer: {computer}")
        print("-----------------------")
        if player == computer:
            print("Tie.")
        if computer == "scissors" and player == "paper":
            print(":( Computer won...")
        if player == "scissors" and computer == "paper":
            print(":] you won!!")
        if computer == "rock" and player == "scissors":
            print(":( Computer won...")
        if player == "rock" and computer == "scissors":
            print(":] you won!!")
        if computer == "rock" and player == "paper":
            print(":] you won!!")
        if player == "rock" and computer == "paper":
            print(":( computer won...")
    print()
    again = input("Do you want to play Rock Paper Scissors again? (y/n): ").strip().lower()
    if again == "y":
        os.system('cls')
        continue
    elif again == "n":
        sys.exit()
    else:
        print()
        print("Please enter 'y' or 'n'.")
        print()
        again = input("Do you want to play Rock Paper Scissors again? (y/n): ").strip().lower()
        if again == "y":
            os.system('cls')
            continue
        elif again == "n":
            sys.exit()
        else:
            sys.exit()