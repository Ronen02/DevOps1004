def save_name(name_to_save):
    my_file = open("names.txt", "w")
    my_file.write(name_to_save + "\n")
    my_file.close()


def show_names():
    my_file = None
    try:
        my_file = open("names123.txt")
        for name in my_file.readlines():
            print(f"hello {name}", end='')
        my_file.close()
    except FileNotFoundError as e:
        print("unable to find file: " + str(e.args))
        if my_file is not None:
            my_file.close()


save_name("Ronen")
show_names()
