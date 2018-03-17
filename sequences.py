def intro_sequence() :
    print("Tutorial: Press enter to advance through dialogue. Type in commands when given a prompt. (Press enter to continue.)")
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
        intro_decision = input("Will you check the cave, the sunlight behind you, or continue on your quest? ").lower()
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

def room_sequence(room,state) :
    room_num = int(room)
    if room_num == 0 :
        intro_sequence()
    if room_num == 1 :
        print("Congrats! You made it to room 1.")