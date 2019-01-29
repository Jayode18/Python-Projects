import os
import time
import sys
import random

# When clear() is called clear the screen


def clear():
    if os.name == 'posix':
        os.system('clear')

    elif os.name in ('ce', 'nt', 'dos'):
        os.system('cls')


#### CHARACTER CREATION CODE ####


def inputName():

    print("Before our adventure can begin, tell me.")
    print("What is your name?")
    print("\n")

    global charName
    charName = input(">>> ")

    print("\n")
    print("Ah so your name is", charName, "then?")
    print("\n")

    nameCheck = input("Is this correct? y/n? ")
    print("\n")

    if nameCheck == ("n"):
        changeName = input("What is your name? ")
        charName = changeName

        print("\n")
        print("Ah so your name is", charName, "then?")
        print("\n")
        print("Excellent. Let's continue.")
        print("\n")

    elif nameCheck == ("N"):
        changeName = input("What is your name? ")
        charName = changeName

        print("\n")
        print("Ah so your name is", charName, "then?")
        print("\n")
        print("Excellent. Let's continue.")
        print("\n")

    elif nameCheck == ("y"):
        print("Excellent. Let's continue.")
        clear()

    elif nameCheck == ("Y"):
        print("Excellent. Let's continue.")
        clear()

    else:
        clear()
        print("I'm sorry, I don't understand what you're saying")
        print("\n")



#### MENUS AND GFX ####


def mainMenu():
    print("##################################")
    print("# Welcome to the Text Adventure! #")
    print("##################################")
    print("#            ==Play==            #")
    print("#            ==Help==            #")
    print("#            ==Quit==            #")
    print("##################################")


def helpMenu():
    print("##################################")
    print("#          Help Menu             #")
    print("##################################")
    print("#    Make sure to look closely   #")
    print("#    Be specific when commanding #")
    print("#    Check your inventory often  #")
    print("#Returning to the menu in 60 secs# ")
    print("##################################")


#### MENU CODE ####


def startup():
    mainMenu()
    menuSelect = input(">>> ")
    if menuSelect == ("play"):
        clear()
        time.sleep(0.25)
        inputName()

    elif menuSelect == ("help"):
        clear()
        time.sleep(0.25)
        helpMenu()
        time.sleep(60)
        clear()
        startup()

    elif menuSelect == ("quit"):
        sys.exit()

    else:
        print("I'm sorry. I don't know what you mean...")
        time.sleep(2)
        clear()
        startup()


        startup()

#### CHARACTER CREATION CODE CONT. ####

 
print("What colour is your hair?")
print("\n")
hairColour = input(">>> ")

clear()
print("So your name is", charName, "and you have", hairColour, "hair?")

confirmChar = input(">>> ")

if confirmChar == ("Y"):
  clear()
  print("And finally... what is your race?")

elif confirmChar == ("y"):
  clear() 
  print("And finally... what is your race?")

elif confirmChar == ("N"):
  clear()
  inputName()

elif confirmChar == ("n"):
  clear()
  inputName()



charRace = input(">>> ")

#### GAME CODE ####


print("It is time ", charName, ".", "It is time for your journey to begin.")
print("\n")


clear()

print(".", end="")
time.sleep(0.5)
print(".", end="")
time.sleep(0.5)
print(".", end="")
print("\n")

time.sleep(1)



def decideLocation():
  print("Ugh... my head. Where am I?")
  print("1. A dingy old pub.")
  print("2. A derelict cottage in the middle of a forest")
  print("\n")
  global startingLocation


decideLocation()

startingLocation = input(">>> ")


if startingLocation == ("1"):
  print("Huh. Looks like a pub to me. I guess I'm upstairs? How did I get here?")

elif startingLocation == ("2"):
  print("A cottage? What the?! How the hell did I end up here?")

else:
  clear()
  print("I'm sorry. That's not a valid choice.")
  time.sleep(1)
  clear()
  decideLocation()

  startingLocation = input(">>> ")

  if startingLocation == ("1"):
   print("Huh. Looks like a pub to me. I guess I'm upstairs? How did I get here?")

  elif startingLocation == ("2"):
    print("A cottage? What the?! How the hell did I end up here?")







#### Create an RNG loot system ####

givenItem = int(random.randint(1, 100))


