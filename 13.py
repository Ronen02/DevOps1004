
# 1. Function input name from users
def save_name():
    n = input("Enter a name: ")
    my_file = open("names.txt", "a")
    my_file.write(F"{n}\n")

# 2. print hello {name} for each name in the names.txt file
def show_names():
    with open("names.txt") as my_file:
        for line in my_file.readlines():
            print(f"Hello {line}", end = '')


def call_urls():
    with open("urls.txt") as urls:
        for line in urls.readlines():
            url_caller(line.strip())

# 3. use urls from urls.txt to call to the url_caller we wrote before
