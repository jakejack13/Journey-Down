def new_save(name) :
    s_file = open("save.txt","w")
    s_file.write(name)
    s_file.close()
