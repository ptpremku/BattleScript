import os
import random

strengthPoints, agilityPoints, staminaPoints = 0,0,0
opponentStrength, opponentAgility, opponentStamina = 0,0,0

def createChar(charName):
    print("Creating a new character")
    userChoice = input("Enter new character name: ")

    if os.path.exists("char\\" + userChoice + ".txt"):
        print("File exists")

    else:
        print("Creating " + userChoice)
        f = open("char\\" + userChoice + ".txt", "x")

        print("Let's give your character some attributes (MAX 45 to each attribute)")

    while True:
        strengthPoints = input("Enter your strength points: ")
        if strengthPoints.isdigit() and int(strengthPoints) <= 45:
            strengthPoints = int(strengthPoints)
            break

        else:
            print("Invalid input, try again")

    while True:
        agilityPoints = input("Enter your agility points: ")
        if agilityPoints.isdigit() and int(agilityPoints) <= 45:
            agilityPoints = int(agilityPoints)
        break

    else:
        print("Invalid input, try again")

    while True:
        staminaPoints = input("Enter your stamina points: ")
        if staminaPoints.isdigit() and int(staminaPoints) <= 45:
            staminaPoints = int(staminaPoints)
        break

    else:
        print("Invalid input, try again")


    f = open("char\\" + userChoice + ".txt", "a")
    f.write(userChoice + f",{strengthPoints},{agilityPoints},{staminaPoints}")
    f.close()

    print("You have successfully created " + userChoice)

def startGameEasy(charName):

    charFilePath = f"char\\{charName}.txt"

    # Read character's initial stats
    with open(charFilePath, "r") as file:
        charLine = file.readline().strip()
    charName, strengthPoints, agilityPoints, staminaPoints = charLine.split(",")

    # Convert stats to integers for manipulation
    strengthPoints = int(strengthPoints)
    agilityPoints = int(agilityPoints)
    staminaPoints = int(staminaPoints)

    # Select opponent from Easy.txt
    with open("NPCS/Easy.txt", "r") as file:
        lines = file.readlines()
        opponent = random.choice(lines).strip()

    stats = opponent.split(",")

    print("You will be going against " + stats[0])

    i = 0
    while i < 3:
        print("Choose your Strength!!!")
        userChoice = input("1. Strength\n2. Agility\n3. Stamina\n")

        if userChoice == "1":
            i += 1

            print("Opponent will choose their random strategy")

            opponentChoice = random.randint(1, 3)

            if opponentChoice == 1:
                opponentStat = int(stats[1])
                print("Opponent chose strength")
            elif opponentChoice == 2:
                opponentStat = int(stats[2])
                print("Opponent chose agility")
            elif opponentChoice == 3:
                opponentStat = int(stats[3])
                print("Opponent chose stamina")

            if strengthPoints >= opponentStat:
                print("You won!!!\nYou have now + 2 pts in strength")
                strengthPoints += 2
                with open(charFilePath, "w") as f:
                    f.write(f"{charName},{strengthPoints},{agilityPoints},{staminaPoints}")
            else:
                print("You lost!!!\nNo points will be added\nBut a point will be taken away from you")
                if strengthPoints > 2:
                    strengthPoints -= 1
                    with open(charFilePath, "w") as f:
                        f.write(f"{charName},{strengthPoints},{agilityPoints},{staminaPoints}")


        elif userChoice == "2":
            i += 1

            print("Opponent will choose their random strategy")

            opponentChoice = random.randint(1, 3)

            if opponentChoice == 1:
                opponentStat = int(stats[1])
                print("Opponent chose strength")
            elif opponentChoice == 2:
                opponentStat = int(stats[2])
                print("Opponent chose agility")
            elif opponentChoice == 3:
                opponentStat = int(stats[3])
                print("Opponent chose stamina")

            if agilityPoints >= opponentStat:
                print("You won!!!\nYou have now + 2 pts in agility")
                agilityPoints += 2
                with open(charFilePath, "w") as f:
                    f.write(f"{charName},{strengthPoints},{agilityPoints},{staminaPoints}")
            else:
                print("You lost!!!\nNo points will be added\nBut a point will be taken away from you")
                if agilityPoints > 2:
                    agilityPoints -= 1
                    with open(charFilePath, "w") as f:
                        f.write(f"{charName},{strengthPoints},{agilityPoints},{staminaPoints}")

        elif userChoice == "3":
            i += 1

            print("Opponent will choose their random strategy")

            opponentChoice = random.randint(1, 3)

            if opponentChoice == 1:
                opponentStat = int(stats[1])
                print("Opponent chose strength")
            elif opponentChoice == 2:
                opponentStat = int(stats[2])
                print("Opponent chose agility")
            elif opponentChoice == 3:
                opponentStat = int(stats[3])
                print("Opponent chose stamina")

            if staminaPoints >= opponentStat:
                print("You won!!!\nYou have now + 2 pts in stamina")
                staminaPoints += 2
                with open(charFilePath, "w") as f:
                    f.write(f"{charName},{strengthPoints},{agilityPoints},{staminaPoints}")
            else:
                print("You lost!!!\nNo points will be added\nBut a point will be taken away from you")
                if staminaPoints > 2:
                    staminaPoints -= 1
                    with open(charFilePath, "w") as f:
                        f.write(f"{charName},{strengthPoints},{agilityPoints},{staminaPoints}")

def startGameMedium(charName):

    charFilePath = f"char\\{charName}.txt"

    # Read character's initial stats
    with open(charFilePath, "r") as file:
        charLine = file.readline().strip()
    charName, strengthPoints, agilityPoints, staminaPoints = charLine.split(",")

    # Convert stats to integers for manipulation
    strengthPoints = int(strengthPoints)
    agilityPoints = int(agilityPoints)
    staminaPoints = int(staminaPoints)

    # Select opponent from Easy.txt
    with open("NPCS/Medium.txt", "r") as file:
        lines = file.readlines()
        opponent = random.choice(lines).strip()

    stats = opponent.split(",")

    print("You will be going against " + stats[0])

    i = 0
    while i < 3:
        print("Choose your Strength!!!")
        userChoice = input("1. Strength\n2. Agility\n3. Stamina\n")

        if userChoice == "1":
            i += 1

            print("Opponent will choose their random strategy")

            opponentChoice = random.randint(1, 3)

            if opponentChoice == 1:
                opponentStat = int(stats[1])
                print("Opponent chose strength")
            elif opponentChoice == 2:
                opponentStat = int(stats[2])
                print("Opponent chose agility")
            elif opponentChoice == 3:
                opponentStat = int(stats[3])
                print("Opponent chose stamina")

            if strengthPoints >= opponentStat:
                print("You won!!!\nYou have now + 2 pts in strength")
                strengthPoints += 3
                with open(charFilePath, "w") as f:
                    f.write(f"{charName},{strengthPoints},{agilityPoints},{staminaPoints}")
            else:
                print("You lost!!!\nNo points will be added\nBut 2 points will be taken away from you")
                if strengthPoints > 3:
                    strengthPoints -= 2
                    with open(charFilePath, "w") as f:
                        f.write(f"{charName},{strengthPoints},{agilityPoints},{staminaPoints}")


        elif userChoice == "2":
            i += 1

            print("Opponent will choose their random strategy")

            opponentChoice = random.randint(1, 3)

            if opponentChoice == 1:
                opponentStat = int(stats[1])
                print("Opponent chose strength")
            elif opponentChoice == 2:
                opponentStat = int(stats[2])
                print("Opponent chose agility")
            elif opponentChoice == 3:
                opponentStat = int(stats[3])
                print("Opponent chose stamina")

            if agilityPoints >= opponentStat:
                print("You won!!!\nYou have now + 2 pts in agility")
                agilityPoints += 3
                with open(charFilePath, "w") as f:
                    f.write(f"{charName},{strengthPoints},{agilityPoints},{staminaPoints}")
            else:
                print("You lost!!!\nNo points will be added\nBut 2 points will be taken away from you")
                if agilityPoints > 3:
                    agilityPoints -= 2
                    with open(charFilePath, "w") as f:
                        f.write(f"{charName},{strengthPoints},{agilityPoints},{staminaPoints}")

        elif userChoice == "3":
            i += 1

            print("Opponent will choose their random strategy")

            opponentChoice = random.randint(1, 3)

            if opponentChoice == 1:
                opponentStat = int(stats[1])
                print("Opponent chose strength")
            elif opponentChoice == 2:
                opponentStat = int(stats[2])
                print("Opponent chose agility")
            elif opponentChoice == 3:
                opponentStat = int(stats[3])
                print("Opponent chose stamina")

            if staminaPoints >= opponentStat:
                print("You won!!!\nYou have now + 2 pts in stamina")
                staminaPoints += 3
                with open(charFilePath, "w") as f:
                    f.write(f"{charName},{strengthPoints},{agilityPoints},{staminaPoints}")
            else:
                print("You lost!!!\nNo points will be added\nBut 2 points will be taken away from you")
                if staminaPoints > 3:
                    staminaPoints -= 2
                    with open(charFilePath, "w") as f:
                        f.write(f"{charName},{strengthPoints},{agilityPoints},{staminaPoints}")

def startGameHard(charName):

    charFilePath = f"char\\{charName}.txt"

    # Read character's initial stats
    with open(charFilePath, "r") as file:
        charLine = file.readline().strip()
    charName, strengthPoints, agilityPoints, staminaPoints = charLine.split(",")

    # Convert stats to integers for manipulation
    strengthPoints = int(strengthPoints)
    agilityPoints = int(agilityPoints)
    staminaPoints = int(staminaPoints)

    # Select opponent from Easy.txt
    with open("NPCS/Hard.txt", "r") as file:
        lines = file.readlines()
        opponent = random.choice(lines).strip()

    stats = opponent.split(",")

    print("You will be going against " + stats[0])

    i = 0
    while i < 3:
        print("Choose your Strength!!!")
        userChoice = input("1. Strength\n2. Agility\n3. Stamina\n")

        if userChoice == "1":
            i += 1

            print("Opponent will choose their random strategy")

            opponentChoice = random.randint(1, 3)

            if opponentChoice == 1:
                opponentStat = int(stats[1])
                print("Opponent chose strength")
            elif opponentChoice == 2:
                opponentStat = int(stats[2])
                print("Opponent chose agility")
            elif opponentChoice == 3:
                opponentStat = int(stats[3])
                print("Opponent chose stamina")

            if strengthPoints >= opponentStat:
                print("You won!!!\nYou have now + 2 pts in strength")
                strengthPoints += 3
                with open(charFilePath, "w") as f:
                    f.write(f"{charName},{strengthPoints},{agilityPoints},{staminaPoints}")
            else:
                print("You lost!!!\nNo points will be added\nBut 4 points will be taken away from you")
                if strengthPoints > 4:
                    strengthPoints -= 3
                    with open(charFilePath, "w") as f:
                        f.write(f"{charName},{strengthPoints},{agilityPoints},{staminaPoints}")


        elif userChoice == "2":
            i += 1

            print("Opponent will choose their random strategy")

            opponentChoice = random.randint(1, 3)

            if opponentChoice == 1:
                opponentStat = int(stats[1])
                print("Opponent chose strength")
            elif opponentChoice == 2:
                opponentStat = int(stats[2])
                print("Opponent chose agility")
            elif opponentChoice == 3:
                opponentStat = int(stats[3])
                print("Opponent chose stamina")

            if agilityPoints >= opponentStat:
                print("You won!!!\nYou have now + 2 pts in agility")
                agilityPoints += 3
                with open(charFilePath, "w") as f:
                    f.write(f"{charName},{strengthPoints},{agilityPoints},{staminaPoints}")
            else:
                print("You lost!!!\nNo points will be added\nBut 4 points will be taken away from you")
                if agilityPoints > 4:
                    agilityPoints -= 3
                    with open(charFilePath, "w") as f:
                        f.write(f"{charName},{strengthPoints},{agilityPoints},{staminaPoints}")

        elif userChoice == "3":
            i += 1

            print("Opponent will choose their random strategy")

            opponentChoice = random.randint(1, 3)

            if opponentChoice == 1:
                opponentStat = int(stats[1])
                print("Opponent chose strength")
            elif opponentChoice == 2:
                opponentStat = int(stats[2])
                print("Opponent chose agility")
            elif opponentChoice == 3:
                opponentStat = int(stats[3])
                print("Opponent chose stamina")

            if staminaPoints >= opponentStat:
                print("You won!!!\nYou have now + 2 pts in stamina")
                staminaPoints += 3
                with open(charFilePath, "w") as f:
                    f.write(f"{charName},{strengthPoints},{agilityPoints},{staminaPoints}")
            else:
                print("You lost!!!\nNo points will be added\nBut 4 points will be taken away from you")
                if staminaPoints > 4:
                    staminaPoints -= 3
                    with open(charFilePath, "w") as f:
                        f.write(f"{charName},{strengthPoints},{agilityPoints},{staminaPoints}")

print("Welcome to this game")

userChoice = input("Choices given to you: \n 1. Load a character \n 2. Create a new characters \n 3. Quit \n 4. View your stats \n")

if userChoice == "1":
    print("Loading a character")

    userChoice = input("Enter character name: ")

    if os.path.exists("char\\" + userChoice + ".txt"):
        f = open("char\\" + userChoice + ".txt", "r")
        charLine = f.readline()
        f.close()

        stats = charLine.split(",")

        charName, strengthPoints, agilityPoints, staminaPoints = stats[0], stats[1], stats[2], stats[3]

        print(charName + " " + strengthPoints + " " + agilityPoints + " " + staminaPoints)

        difficulty = input("Choose Difficulty:\n1. Easy\n2. Medium\n3. Hard\n")

        if difficulty == "1":
            startGameEasy(charName)

        if difficulty == "2":
            startGameMedium(charName)

        if difficulty == "3":
            startGameHard(charName)

        while True:
            userChoice = input("Do you want to play again? (y/n) : ")

            if userChoice == "y":
                difficulty = input("Choose Difficulty:\n1. Easy\n2. Medium\n3. Hard\n")

                if difficulty == "1":
                    startGameEasy(charName)

                if difficulty == "2":
                    startGameMedium(charName)

                if difficulty == "3":
                    startGameHard(charName)

            elif userChoice == "n":
                print("Thank you for playing")
                break

            else:
                print("Invalid input")

    else:
        print("Player does not exist \n Let's make a new character ")
        userChoice = input("Enter character name again: ")
        createChar(userChoice)


if userChoice == "2":
    createChar(userChoice)

    difficulty = input("Choose Difficulty:\n1. Easy\n2. Medium\n3. Hard\n")

    charName = userChoice

    if difficulty == "1":
        startGameEasy(userChoice)

    if difficulty == "2":
        startGameMedium(userChoice)

    if difficulty == "3":
        startGameHard(userChoice)

    while True:
        userChoice = input("Do you want to play again? (y/n) : ")

        if userChoice == "y":
            difficulty = input("Choose Difficulty:\n1. Easy\n2. Medium\n3. Hard\n")

            if difficulty == "1":
                startGameEasy(charName)

            if difficulty == "2":
                startGameMedium(charName)

            if difficulty == "3":
                startGameHard(charName)

        elif userChoice == "n":
            print("Thank you for playing")
            break

        else:
            print("Invalid input")


if userChoice == "3":
    print("Quitting")

if userChoice == "4":
    userChoice = input("Enter character name: ")

    if os.path.exists("char\\" + userChoice + ".txt"):
        f = open("char\\" + userChoice + ".txt", "r")
        charLine = f.readline()
        f.close()

        stats = charLine.split(",")

        charName, strengthPoints, agilityPoints, staminaPoints = stats[0], stats[1], stats[2], stats[3]

        print(charName + " " + strengthPoints + " " + agilityPoints + " " + staminaPoints)