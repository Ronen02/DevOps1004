def get_age():
    age = int(input("Enter your age: "))
    if age < 0:
        raise ValueError("Age can not be negative")

try:
    get_age()
except ValueError as e:
    print(e.args)