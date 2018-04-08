def new_save(name) :
    s_file = open("save.txt","w")
    #Name, Floor, State
    s_file.write(name + "#0#0")
    s_file.close()
def load_save() :
    s_file = open("save.txt","r")
    save_data = s_file.read()
    #Stats read and split into list for use
    stats = save_data.split("#")
    s_file.close()
    return stats
def save_game(name,room,state) :
    s_file = open("save.txt","w")
    #Overrides previous save and writes name#room#state
    s_file.write(name + "#" + str(room) + "#" + str(state))
