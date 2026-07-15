import sys
import os

while True:
    print("------------------")
    print("|   Welcome to   |")
    print("|   Calculator   |")
    print("------------------")

    symbolchoice = input("What is your operation today? (+, -, x, /): ")

    symboloptions = ("+", "-", "x", "/")

    while symbolchoice not in symboloptions:
        print("Please enter a valid symbol.")
        symbolchoice = input("What is your operation today? (+, -, x, /): ")


    num1 = input("First number(s) of your operation (x+2): ")
    num2 = input("Second number(s) of your operation (2+x): ")

    num1int = int(num1)
    num2int = int(num2)

    if symbolchoice == "+":
        result = num1int + num2int

    if symbolchoice == "-":
        result = num1int - num2int

    if symbolchoice == "x":
        result = num1int * num2int

    if symbolchoice == "/":
        result = num1int / num2int

    print("")
    print(result)
    print("")
    print()
    again = input("Do you want to Calculate again? (y/n): ").strip().lower()
    if again == "y":
        os.system('cls')
        continue
    elif again == "n":
        sys.exit()
    else:
        print()
        print("Please enter 'y' or 'n'.")
        print()
        again = input("Do you want to Calculate again? (y/n): ").strip().lower()
        if again == "y":
            os.system('cls')
            continue
        elif again == "n":
            sys.exit()
        else:
            sys.exit()