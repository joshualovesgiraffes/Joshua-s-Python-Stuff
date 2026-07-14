import sys
import random

playerchoice = input("Enter number ... 1 to 8\n")


computerchoice = random.choice("12345678")
playerchoiceint = int(playerchoice)
computerchoiceint = int(computerchoice)

if playerchoiceint >= 9:
    red("Number has to be 1 to 8.")
    input("Press ENTER To exit")
    sys.exit("")
elif playerchoiceint <= 0:
    red("Number has to be 1 to 8.")
    input("Press ENTER To exit")
    sys.exit("")
    
if playerchoiceint == computerchoiceint:
    print("🎉 You got it!")
    print("Computers choice: " + computerchoice)
else:
    print("😔 Aw man! You didnt get it..")
    print("Computers choice: " + computerchoice)
print("")
input("Press ENTER To exit. 😊 Thanks for playing this game made by Joshua1056")