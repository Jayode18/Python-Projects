import time
import sys

def newLine():
    print("\n")

# ------------------------------------Actual Code-------------------------------------------
def getInfo():
    print("Hello! Before we begin. I need a few details from you.")
newLine()
pName = input("Adventurer, what is your name? ")
time.sleep(0.5)
newLine()
print("Ah yes... ", pName, "a fine name indeed.")

def startMenu():
    print("##################################")
    print("# Welcome to the Text Adventure! #")
    print("##################################") 
    print("#            -Play-              #")
    print("#            -Help-              #")
    print("#            -Quit-              #")
    print("#      © 2019 Jack O'Donnell.    #")
    print("###################################")

def beginGame():
    startGame = input(">>> ")
    try:
        if(startGame == "play"):
          print("This is working correctly")

        elif(startGame == "help"):
          print("####################################### ")
          print("#               Help Menu             #")
          print("####################################### ")
          print(" -  Use up, down, left and right to move  ")
          print(" - Try to be specific when executing commands")
          print(" - Type 'look' to inspect things closely. ")
          print(" -       Best of luck adventurer!         ")
          print("##########################################")
        elif(startGame == "quit"):
            sys.quit()
