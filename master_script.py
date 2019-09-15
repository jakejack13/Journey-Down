#Import game functions + extra functionality
import os.path
from pathlib import Path
import os
clear = lambda: os.system('cls')
from utility import new_save
from utility import load_save
from utility import save_game
from sequences import intro_sequence
from sequences import room_sequence

game_state = 0
print("Journey Down")
print("By Jacob Kerr, 2018")
#Creating and loading save file and stored as stats
while True :
    new_or_load = int(input("Would you like to make a new game (1) or load a previous game (2): "))
    my_file = Path("save.txt")
    if new_or_load == 1:
        #Add system to replace hashtags
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
stat_name = stats[0]
stat_room = int(stats[1])
stat_state = stats[2]
print("Game loaded")
print("Welcome, " + stat_name)
input("Press enter to continue...")
clear()

#New game tutorial and beginning sequence
if new_game == 1 :
    intro_sequence()
    stat_room = 1
    save_game(stat_name,stat_room,stat_state)
clear()
while True :
    #Prevents infinite loop if room not finished
    if stat_room == 0 :
        break
    stat_room = room_sequence(stat_name,stat_room,stat_state)
    save_game(stat_name,stat_room,stat_state)
    clear()
