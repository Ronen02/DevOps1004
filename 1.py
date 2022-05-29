a = "Hello World"
b = 4
c = False
d = ["ben", "Raz", 32, ["ski", "Snowboard"]]
e = ["aviel", 32, True]
f = {"fname": "ben", "lname": "raz", "age": 32, "hobbies": ["ski", "Snowboard"]}
print(a)
print(d[1])
d[3] = ["Guitar"]
print(d)
e[2] = 40
print(f["lname"])
if f["lname"] != "ben":
    print("your name is ben")