#Long sequence, created separate function
def intro_sequence() :
    print("Tutorial: Press enter to advance through dialogue. Type in commands when given a prompt. Commands are usually indicated in captial letters. (Press enter to continue.)")
    input()
    print("You find yourself standing at the mouth of a cave, with no memory of who you are or how you have gotten there.")
    input()
    print("Sunlight streams into the cavern from behind you, but you can barely see it slant downwards into the abyss, where only shadows can touch.")
    input()
    print("You don’t know why, but you feel drawn to the cave, feel it calling to you. You look through your memories, but, of course, you cannot find anything.")
    input()
    print("The cave seems to be the answer to your problems.")
    input()
    while True :
        intro_decision = input("Will you check the CAVE, the SUNLIGHT behind you, or CONTINUE on your quest? ").lower()
        if intro_decision == "sunlight" :
            print("You check the sunlight behind you. You are standing at the edge of the ledge, looking down into a valley filled with trees.")
            input()
            print("Beyond the valley, the ocean looms out as far as the eye can see, touching the horizon. There seems to be no sign of human activity anywhere.")
            input()
            print("You are alone, with your thoughts and without memory.")
            input()
        elif intro_decision == "cave" :
            print("You peer into the depths of the cave, but there is nothing you can discern from it. It seems to be a regular old cave.")
            input()
            print("It continues straight for about 10 feet before steeply dropping off deeper into the darkness.")
            input()
            print("You’re not sure why, but you feel as if this is the path you are meant to take.")
            input()
        elif intro_decision == "continue" :
            break
        else:
            print("Sorry, that is not a correct command. Please input a correct command.")
        continue
    print("With every passing minute you stand in front of the cave, you feel more and more sure that this is the right path.")
    input()
    print("You hesitantly take a few steps forward, abandoning the sunlight for the darkness. You still cannot see anything other than a few feet in front of you.")
    input()
    print("Strangely, you don’t feel scared at all. Instead, you feel calm and even… excited?")
    input()
    print("As you step onto the decline of the cave floor, you feel something slimy beneath your feet. Pausing, you reach down, confused as why you didn’t see anything before.")
    input()
    print("Reaching down causes you to pitch forward, off balance, slipping and sliding down the decline into the abyss below. Behind you, you hear the rumbling of something closing off the cave mouth, plunging you into darkness.")
    input()
    print("You stumble, collapsing as you hit the bottom of the slide. You slowly gather yourself and prop yourself back onto your feet.")
    input()
    print("Determination growing even stronger, you set off onto your Journey Down.")
    input()
    return 1

def room_sequence(name,room,state) :
    room_num = room
    if room_num == 0 :
        #Redundant, autoruns intro if new game selected, run in case close during intro
        intro_sequence()
        return 1
    elif room_num == 1 :
        print("You walk into a small space that seems to resemble a room. The walls, ceiling, and floor are smooth and flat, chiseled and sanded out of the rock with precision.")
        input()
        print("There are three doors, one on each wall. They are made out of solid oak wood, with polished brass knobs.")
        input()
        r1_d = input("Do you open the LEFT door, CENTER door, or RIGHT door? ").lower()
        #Decision to room 2,3,4
        while True :
            if r1_d == "left" :
                return 2
                break
            elif r1_d == "center" :
                return 3
                break
            elif r1_d == "right" :
                return 4
                break
            else :
                print("Sorry, that is not a correct command. Please input a correct command.")
                continue
    elif room_num == 2 :
        print("You enter a room similar to the last, with the same sandstone walls and wooden doors.")
        input()
        print("However, there is a slight difference in this room. Standing in the corner is a simple wooden stool, made out of the same wood as the doors.")
        input()
        print("On it is a small leatherbound book. There are no markings on it except for a blue ribbon sticking out of the middle.")
        input()
        r2_d = input("Do you INSPECT the book or go through one of the DOORS? ").lower()
        while True:
            if r2_d == "inspect" :
                print("You pick up the book and flip through the pages. It seems to be a journal of some kind.")
                input()
                print("There are dates written at the top of every page, but there isn't any writing in the book. You flip to the page that is marked by the blue ribbon.")
                input()
                print("On it is a name: " + name + ". Nothing else is written.")
                input()
                print("There is a glimmer of recognition in your mind after seeing the name, but you are not sure why. You decide to keep the book.")
                input()
                continue
            elif r2_d == "doors" :
                #Go to different "room" for door selection here?
                r2_d2 = input("Do you go through the LEFT door, MIDDLE door, or RIGHT door?").lower()
                    while True:
                        if r2_d2 == "left" :
                            return 6
                            break
                        elif r2_d2 == "middle" :
                            return 7
                            break
                        elif r2_d2 == "right" :
                            return 8
                            break
                        else :
                            print("Sorry, that is not a correct command. Please input a correct command.")
                            continue
            else :
                print("Sorry, that is not a correct command. Please input a correct command.")
                continue
    elif room_num == 3 :
        print("Room 3")
        return False
    elif room_num == 4 :
        print("Room 4")
        return False
    elif room_num == 5 :
        print("Room 5")
        return False
    elif room_num == 6 :
        return False
    elif room_num == 7 :
        return False
    elif room_num == 8 :
        return False

    else :
        print("Congrats! You broke the game. Just for that, I'll corrupt your save file for you. No need to thank me.")
        return False
