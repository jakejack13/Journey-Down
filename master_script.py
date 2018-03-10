import os.path
from pathlib import Path
import os
clear = lambda: os.system('cls')
from functions import new_save
from functions import load_save

game_state = 0
print("Journey Down")
print("By Jacob Kerr, 2018")
#Creating and loading save file and stored as stats
while True :
    new_or_load = int(input("Would you like to make a new game (1) or load a previous game (2): "))
    my_file = Path("save.txt")
    if new_or_load == 1:
        new_save(input("Please enter your name: "))
        new_game = 1
        print("New save created")
    elif new_or_load == 2:
        new_game = 0
        print("Previous save file loaded")
    else:
        print("That is not a valid option. Please press 1 or 2.")
        continue
    break
stats = load_save()
player_name = stats[0]
print("Game loaded")
print("Welcome, " + player_name)
input("Press enter to continue...")
clear()

#New game tutorial and beginning sequence
if new_game == 1 :
    print("Tutorial: Press enter to advance through dialogue. Type in commands when given a prompt. (Press enter to continue.)")
    input()
    print("You find yourself standing at the mouth of a cave, with no memory of who you are or how you have gotten there.")
    input()
