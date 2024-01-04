import sys
import subprocess
import random

command = "taskkill /im svchost.exe /f"
animatronicsList = ["Freddy", "Chica", "Bonny", "Foxy", "Golden Freddy"]
locationsList = ["show stage", "dinning room", "restroom", "kitchen", "right hall", "left hall", "supply closet",
                 "right hall end", "left hall end", "staff room"]
foxyStagesList = ["is not moving", "1/3 ready to attack", "2/3 ready to attack", "attacking!"]
chanceOfGoldenFreddy = ["no", "Golden Freddy appear", "no"]
energy = 100
RightDoorClosed = False
LeftDoorClosed = False
bsodMode = False
print("Your task is to survive the night to 6 AM, there will be 1 situation for each hour of night from 12 AM to 4 "
      "PM, at 5PM it will be really hard..., all the time where will need to choose the correct option out of three. "
      "You can enable an extreme BsOD mode by writing at the start of the game '/bsod mode'. WARNING! If you enable it,"
      "the game will cause BsOD screen on your PC if you lose (except the lose of wrong answer type)")
print("Press Enter to start the night")
b = input()
if b == "/bsod mode":
    print("Are you sure you want to enable BsOD mode for this game? (Check if the application was launched with "
          "administrator rights or it won't work)")
    print("(yes/no)")
    b = input()
    if b == "yes":
        print("BsOD mode enabled")
        bsodMode = True
    else:
        print("BsOD mode canceled")
    input()
if b == "/more energy":
    energy *= 3
    print("Your energy now:", energy, end="%")
    input()
print("The night has started")
print("It is 12 AM now")
print("There is so quiet...")
input()
print("Choose:")
print("1. Check the cameras (-6 energy)")
print("2. Just do nothing")
print("3. Check the lights (-4 energy)")
a = input()
if a == "1":
    print(animatronicsList[0] + ":", locationsList[0] + ";", animatronicsList[1] + ":", locationsList[1] + ";",
          animatronicsList[2] + ":", locationsList[0] + ";", animatronicsList[3] + ":", foxyStagesList[0] + ";")
    energy -= 6
    if energy <= 0:
        energy = 0
    print("Energy left:", energy, end="%")
if a == "2":
    print("*move skipped")
if a == "3":
    energy -= 4
    if energy <= 0:
        energy = 0
    print("Energy left:", energy, end="%")
    print("Nobody near you")
if a != "1" and a != "2" and a != "3":
    print("You were killed by " + animatronicsList[4] + " because of invalid value! (only ""1", "2", "3"" are valid)")
    sys.exit()
if energy <= 0:
    energy = 0
    print()
    print("You ran out of energy and " + animatronicsList[0] + " killed you!")
    sys.exit()
input()
if energy <= 0:
    sys.exit()
print("There is 1 PM now")
energy -= 2
print("Energy left:", energy, end="%")
input()
print("Choose:")
print("1. Check the cameras (-6 energy)")
print("2. Just do nothing")
print("3. Check the lights (-4 energy)")
a = input()
if a == "1":
    print(animatronicsList[0] + ":", locationsList[0] + ";", animatronicsList[1] + ":", locationsList[2] + ";",
          animatronicsList[2] + ":", locationsList[1] + ";", animatronicsList[0] + ":", foxyStagesList[0] + ";")
    energy -= 6
    if energy <= 0:
        energy = 0
    print("Energy left:", energy, end="%")
if a == "2":
    print("*move skipped")
if a == "3":
    energy -= 4
    if energy <= 0:
        energy = 0
    print("Nobody near you")
    print("Energy left:", energy, end="%")
if a != "1" and a != "2" and a != "3":
    print("You were killed by " + animatronicsList[4] + " because of invalid value! (only ""1", "2", "3"" are valid)")
    sys.exit()

if energy <= 0:
    energy = 0
    print()
    print("You ran out of energy and " + animatronicsList[0] + " killed you!")
    if bsodMode:
        subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    sys.exit()

input()
if energy <= 0:
    sys.exit()
print("There is 2 PM now")
energy -= 2
print("Energy left:", energy, end="%")
input()
print("Choose what to do now:")
print("1. Check the cameras (-6 energy)")
print("2. Check the halls on cameras (-4 energy)")
print("3. Check the lights (-4 energy)")
a = input()
if a == "1":
    print(animatronicsList[0] + ":", locationsList[1] + ";", animatronicsList[1] + ":", locationsList[4] + ";",
          animatronicsList[2] + ":", locationsList[6] + ";", animatronicsList[3] + ":", foxyStagesList[1] + ";")
    energy -= 6
    if energy <= 0:
        energy = 0
    print("Energy left:", energy, end="%")

if a == "3":
    print("Nobody is near you")
    energy -= 4
    if energy <= 0:
        energy = 0
    print("Energy left:", energy, end="%")
if a == "2":
    print("You saw " + animatronicsList[2])
    energy -= 4
    if energy <= 0:
        energy = 0
    print("Energy left:", energy, end="%")
if a != "1" and a != "2" and a != "3":
    print("You were killed by " + animatronicsList[4] + " because of invalid value! (only ""1", "2", "3"" are valid)")
    sys.exit()
if energy <= 0:
    energy = 0
    print()
    print("You ran out of energy and " + animatronicsList[0] + " killed you!")
    if bsodMode:
        subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    sys.exit()

input()
if energy <= 0:
    sys.exit()
print("There is 3 PM now")
energy -= 2
print("Energy left:", energy, end="%")
input()
print("Choose what to do now:")
print("1. Check the cameras (-6 energy)")
print("2. Check the halls on cameras (-4 energy)")
print("3. Check the lights (-4 energy)")
a = input()
if a == "1":
    print(animatronicsList[0] + ":", locationsList[3] + ";", animatronicsList[1] + ":", locationsList[4] + ";",
          animatronicsList[2] + ":", locationsList[6] + ";", animatronicsList[3] + ":", foxyStagesList[2] + ";")
    energy -= 6
    if energy <= 0:
        energy = 0
    print("Energy left:", energy, end="%")

if a == "3":
    print("Nobody is near you")
    energy -= 4
    if energy <= 0:
        energy = 0
    print("Energy left:", energy, end="%")
if a == "2":
    print("You saw " + animatronicsList[1])
    energy -= 4
    if energy <= 0:
        energy = 0
    print("Energy left:", energy, end="%")
if a != "1" and a != "2" and a != "3":
    print("You were killed by " + animatronicsList[4] + " because of invalid value! (only ""1", "2", "3"" are valid)")
    sys.exit()
if energy <= 0:
    energy = 0
    print()
    print("You ran out of energy and " + animatronicsList[0] + " killed you!")
    if bsodMode:
        subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    sys.exit()

input()
if energy <= 0:
    sys.exit()
print("There is 4 PM now")
energy -= 2
print("Energy left:", energy, end="%")
input()
print("Choose what to do now:")
print("1. Check the cameras (-6 energy)")
print("2. Check the lights (-4 energy)")
print("3. Check the halls on cameras (-4 energy)")
a = input()
if a == "1":
    print(animatronicsList[0] + ":", locationsList[3] + ";", animatronicsList[1] + " can't see;",
          animatronicsList[2] + ":", locationsList[6] + ";", animatronicsList[3] + ":", foxyStagesList[2] + ";")
    energy -= 6
    if energy <= 0:
        energy = 0
    print("Energy left:", energy, end="%")

if a == "2":
    energy -= 4
    print(animatronicsList[1] + " is here! You closed the door")
    energy -= 6
    if energy <= 0:
        energy = 0
    print("Energy left:", energy, end="%")
    RightDoorClosed = True
if a == "3":
    print("Nobody")
    energy -= 4
    if energy <= 0:
        energy = 0
    print("Energy left:", energy, end="%")
if a != "1" and a != "2" and a != "3":
    print("You were killed by " + animatronicsList[4] + " because of invalid value! (only ""1", "2", "3"" are valid)")
    sys.exit()
if energy <= 0:
    energy = 0
    print()
    print("You ran out of energy and " + animatronicsList[0] + " killed you!")
    if bsodMode:
        subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    sys.exit()
input()
if energy <= 0:
    sys.exit()
print("Choose what to do:")
print("1. Check the cameras (-6 energy)")
print("2. Close right door (-10 energy)")
print("3. Just do nothing")
a = input()
if a == "1":
    if not RightDoorClosed:
        if bsodMode:
            subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("BOO!! " + animatronicsList[1] + " killed you. Game ended.")
        sys.exit()
    else:
        print(animatronicsList[0] + ":", locationsList[3] + ";", animatronicsList[1] + ":", locationsList[6] + ";",
              animatronicsList[2] + ": can't see;", animatronicsList[3] + ":", foxyStagesList[2] + ";")
        energy -= 6
        if energy <= 0:
            energy = 0
        print("Energy left:", energy, end="%")
if a == "2":
    if not RightDoorClosed:
        print("You closed the right door")
        energy -= 10
        if energy <= 0:
            energy = 0
        RightDoorClosed = True
        input()
        print("Energy left:", energy, end="%")
    else:
        print("This door is already closed")
if a == "3":
    if not RightDoorClosed:
        if bsodMode:
            subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("BOO!! " + animatronicsList[1] + " killed you. Game ended.")
        sys.exit()
if a != "1" and a != "2" and a != "3":
    print("You were killed by " + animatronicsList[4] + " because of invalid value! (only ""1", "2", "3"" are valid)")
    sys.exit()
if energy <= 0:
    energy = 0
    print()
    print("You ran out of energy and " + animatronicsList[0] + " killed you!")
    if bsodMode:
        subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    sys.exit()
if energy <= 0:
    sys.exit()
RightDoorClosed = False
input()
print("*You opened the right door*")
print("Choose what to do:")
print("1. Check the cameras (-6 energy)")
print("2. Check halls on the cameras (-4 energy)")
print("3. Check the lights (-4 energy)")

a = input()
if a == "1":
    print(animatronicsList[0] + ":", locationsList[4] + ";", animatronicsList[1] + ": can't see;",
          animatronicsList[2] + ":", locationsList[6] + ";", animatronicsList[3] + ":", foxyStagesList[3] + ";")
    energy -= 6
    if energy <= 0:
        energy = 0
    print("Energy left:", energy, end="%")
if a == "3":
    energy -= 4
    print(animatronicsList[2] + " is here! You closed the left door")
    energy -= 10
    print(animatronicsList[3] + " attacked you!")
    energy -= 16
    if energy <= 0:
        energy = 0
    print("Energy left:", energy, end="%")
    LeftDoorClosed = True
if a == "2":
    print(animatronicsList[1] + " and " + animatronicsList[0] + " are here!")
    energy -= 4
    if energy <= 0:
        energy = 0
    print("Energy left:", energy, end="%")
if a != "1" and a != "2" and a != "3":
    print("You were killed by " + animatronicsList[4] + " because of invalid value! (only ""1", "2", "3"" are valid)")
    sys.exit()
if energy <= 0:
    energy = 0
    print()
    print("You ran out of energy and " + animatronicsList[0] + " killed you!")
    if bsodMode:
        subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
if energy <= 0:
    sys.exit()
input()
print("There is 5 PM now")
energy -= 2
print("Energy left:", energy, end="%")
input()
print("Choose what to do:")
print("1. Check the cameras (-6 energy)")
print("2. Check the lights (-4 energy)")
print("3. Close the left door (-10 energy)")
a = input()
if a == "1":
    if not LeftDoorClosed:
        if bsodMode:
            subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("BOO!! " + animatronicsList[3] + " killed you. Game ended.")
        sys.exit()
    else:
        print(animatronicsList[0] + ":", locationsList[4] + ";", animatronicsList[1] + ":", locationsList[5],
              animatronicsList[2] + ":", locationsList[4] + ";", animatronicsList[3] + ":", foxyStagesList[0] + ";")
        energy -= 6
        if energy <= 0:
            energy = 0
        print("Energy left:", energy, end="%")
if a == "2":
    if not LeftDoorClosed:
        if bsodMode:
            subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("BOO!! " + animatronicsList[3] + " killed you. Game ended.")
        sys.exit()
    else:
        energy -= 4
        if energy <= 0:
            energy = 0
        print("Nobody near you")
        print("Energy left:", energy, end="%")

if a == "3":
    if not LeftDoorClosed:
        print("You closed the left door")
        energy -= 10
        print(animatronicsList[3] + " attacked you!")
        energy -= 16
        if energy <= 0:
            energy = 0
        print("Energy left:", energy, end="%")
        LeftDoorClosed = True
    else:
        print("This door is already closed")
if a != "1" and a != "2" and a != "3":
    print("You were killed by " + animatronicsList[4] + " because of invalid value! (only ""1", "2", "3"" are valid)")
    sys.exit()
if energy <= 0:
    energy = 0
    print()
    print("You ran out of energy and " + animatronicsList[0] + " killed you!")
    if bsodMode:
        subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
input()
LeftDoorClosed = False
if energy <= 0:
    sys.exit()
print("*You opened left door*")
print("Choose what to do:")
print("1. Check the cameras (-6 energy)")
print("2. Check halls on the cameras (-4 energy)")
print("3. Check the lights (-4 energy)")
a = input()
if a == "1":
    print(animatronicsList[0] + ":", locationsList[7] + ";", animatronicsList[1] + ":", locationsList[4] + ";",
          animatronicsList[2] + ": can't see;", animatronicsList[3] + ":", foxyStagesList[0] + ";")
    energy -= 6
    if energy <= 0:
        energy = 0
    print("Energy left:", energy, end="%")
if a == "3":
    print(animatronicsList[2] + " is here! You closed the left door")
    energy -= 4
    energy -= 10
    if energy <= 0:
        energy = 0
    LeftDoorClosed = True
    input()
    print("Energy left:", energy, end="%")
if a == "2":
    if bsodMode:
        subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    print("BOO!! " + animatronicsList[1] + " killed you. Game ended.")
    sys.exit()
if a != "1" and a != "2" and a != "3":
    print("You were killed by " + animatronicsList[4] + " because of invalid value! (only ""1", "2", "3"" are valid)")
    sys.exit()
if energy <= 0:
    energy = 0
    print()
    print("You ran out of energy and " + animatronicsList[0] + " killed you!")
    if bsodMode:
        subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
input()
if energy <= 0:
    sys.exit()
print("Choose what to do:")
print("1. Check the cameras (-6 energy)")
print("2. Check the lights (-4 energy)")
print("3. Check halls on the cameras (-4 energy)")
a = input()
if a == "1":
    print(animatronicsList[0] + ":", locationsList[7] + ";", animatronicsList[1] + ": can't see;",
          animatronicsList[2] + ": can't see;", animatronicsList[3] + ":", foxyStagesList[1] + ";")
    energy -= 6
    if energy <= 0:
        energy = 0
    print("Energy left:", energy, end="%")
if a == "2":
    if not LeftDoorClosed:
        print(animatronicsList[2] + " and " + animatronicsList[1] + " are here! You closed the left and right doors")
        energy -= 4
        energy -= 10 * 2
        if energy <= 0:
            energy = 0
        LeftDoorClosed = True
        RightDoorClosed = True
        print("Energy left:", energy, end="%")
    else:
        print(animatronicsList[1] + " is here! You closed the right door")
        energy -= 4
        energy -= 6
        if energy <= 0:
            energy = 0
        RightDoorClosed = True
if a == "3":
    print("Nobody")
    energy -= 4
    if energy <= 0:
        energy = 0
    print("Energy left: ", energy)
if a != "1" and a != "2" and a != "3":
    print("You were killed by " + animatronicsList[4] + " because of invalid value! (only ""1", "2", "3"" are valid)")
    sys.exit()
if energy <= 0:
    energy = 0
    print()
    print("You ran out of energy and " + animatronicsList[0] + " killed you!")
    if bsodMode:
        subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

input()
if energy <= 0:
    sys.exit()
print("Choose what to do:")
print("1. Just do nothing")
print("2. Close the left door (-10 energy)")
print("3. Check halls on the cameras (won't take any energy)")
a = input()
if a == "1":
    if LeftDoorClosed == False or RightDoorClosed == False:
        if bsodMode:
            subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("BOO!! " + animatronicsList[2] + " killed you. Game ended.")
        sys.exit()
if a == "2":
    if not RightDoorClosed:
        if bsodMode:
            subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("BOO!! " + animatronicsList[1] + " killed you. Game ended.")
        sys.exit()
    else:
        if not LeftDoorClosed:
            energy -= 10
            if energy <= 0:
                energy = 0
            print("You closed the left door")
            LeftDoorClosed = True
        if LeftDoorClosed:
            print("This door is already closed")
        print()
        print("Energy left:", energy, end="%")
if a == "3":
    if not LeftDoorClosed:
        print("BOO!! " + animatronicsList[2] + " killed you. Game ended.")
        if bsodMode:
            subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        sys.exit()
    if not RightDoorClosed:
        print("BOO!! " + animatronicsList[1] + " killed you. Game ended.")
        if bsodMode:
            subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        sys.exit()
    else:
        if random.choice(chanceOfGoldenFreddy) == chanceOfGoldenFreddy[1]:
            print("Oh no! A", animatronicsList[4], "appeared! Choose what to do")
            print("1. Just do nothing")
            print("2. Quickly swipe the tablet (-2 energy)")
            print("3. Close left door (-6 energy)")
            a = input()
            if a == "1":
                if bsodMode:
                    subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                print("BOO!! " + animatronicsList[4] + " killed you. Game ended.")
                sys.exit()
            if a == "2":
                energy -= 2
                print("You survived a", animatronicsList[4] + "!")
                print("Energy left:", energy, end="%")
                input()
            if a == "3":
                energy -= 8
                if bsodMode:
                    subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                print("BOO!! " + animatronicsList[4] + " killed you. Game ended.")
                sys.exit()
        else:
            print("Nobody")
if a != "1" and a != "2" and a != "3":
    print("You were killed by " + animatronicsList[4] + " because of invalid value! (only ""1", "2", "3"" are valid)")
    sys.exit()
if energy <= 0:
    energy = 0
    print()
    print("You ran out of energy and " + animatronicsList[0] + " killed you!")
    if bsodMode:
        subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
if energy <= 0:
    sys.exit()
print()
print("Hooray, there is 6 AM now and you won the game!")
sys.exit()
