import os.path
from pathlib import Path
from functions import new_save
from functions import load_save

print("Journey Down")
print("By Jacob Kerr, 2018")
#Creating and loading save file and stored as stats
my_file = Path("save.txt")
if not my_file.is_file():
    new_save(input("Please enter your name: "))
    new_game = 1
else:
    new_game = 0
stats = load_save()
