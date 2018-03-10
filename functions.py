def new_save(name) :
    s_file = open("save.txt","w")
    #Name, Lvl, Atk, Def
    #Stats may not be included
    s_file.write(name + "#0" + "#0" + "#0")
    s_file.close()
def load_save() :
    s_file = open("save.txt","r")
    save_data = s_file.read()
    stats = save_data.split("#")
    s_file.close()
    return stats
