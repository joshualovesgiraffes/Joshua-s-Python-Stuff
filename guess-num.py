import sys
import random

computerchoice = random.randint(1, 100)
computerchoiceint = int(computerchoice)

while True:
    playerchoice = input("Enter number ... 1 to 100\n")

    playerchoiceint = int(playerchoice)

    if playerchoiceint >= 100:
        print("Number has to be 1 to 100.")
        continue
    elif playerchoiceint <= 1:
        print("Number has to be 1 to 100.")
        continue
    
    if playerchoiceint == computerchoiceint:
        print("🎉 You got it!")
        print("Computers choice: " + str(computerchoice))
        input("Press ENTER to exit.")
        sys.exit()
    else:
        if playerchoiceint > computerchoiceint:
            print("Your number is too high.")
        else:
            print("Your number is too low.")
    
    if playerchoice == None:
        print("Please enter a valid input.")
        continue