def get_number():
    a = input("Enter Number")
    if a.isdecimal():
        return int(a)
    return -1
