# # A
# x = int(input("Enter first number: "))
# y = int(input("Enter second number: "))
# if x > y:
#     print("BIG")
# if x == y:
#     print("Equals")
# if x < y:
#     print("Small")
#
# # B
# a = 0
# for i in range(5):
#     print(a)
#     a = a + 1

# # C
# n = random.randint(1, 4)
# if n == 1:
#     print("Summer")
# if n == 2:
#     print("Winter")
# if n == 3:
#     print("Fall")
# if n == 4:
#     print("Spring")

# D
# 1. 10 times
# 2. 10

# E
# age = int(input("Enter your age: "))
# name = input("Enter the first letter of your name: ")
# currency = 3.35
# fly = input("Enter true or False: did you fly abroad? ")
# apartment = int(input("Enter your apartment number: "))
#
# print(age, name, currency, fly, apartment)
# print(age + currency)

# F
# phone_number = input("Please enter your phone number: ")
# print(f"Phone Number: {phone_number}")

# G
# def printhello():
#     print("hello")
#
#
# def calculate():
#     a = 5 + 3.2
#     print(a)
#
#
# printhello()
# calculate()

# H
# def nametaker():
#     name = input("Enter your name: ")
#     print(name)
#
# def divider():
#     number = int(input("Enter a number: "))
#     number = number / 2
#     print(number)
#
#
# nametaker()
# divider()

# I
# def sum():
#     first = int(input("Enter first number: "))
#     second = int(input("Enter second number: "))
#     total = first + second
#     print(total)
#
# def word():
#     firstword = input("Enter a word: ")
#     secondword = input("Enter another word: ")
#     print(f"{firstword} {secondword}")
#
#
# sum()
# word()

# Challenges
# K
# for i in range(1):
#     print("#")
#     for i in range(1):
#         print("##")
#         for i in range(1):
#             print("###")
#             for i in range(1):
#                 print("####")
#                 for i in range(1):
#                     print("#####")

# L
# for i in range(1):
#     print("#     #")
#     for i in range(1):
#         print(" #   # ")
#         for i in range(1):
#             print("  # #  ")
#             for i in range(1):
#                 print("   #   ")
#                 for i in range(1):
#                     print("  # #  ")
#                     for i in range(1):
#                         print(" #   # ")
#                         for i in range(1):
#                             print("#     #")

# M
n = int(input("Enter a number: "))
tot = 0
while n > 0:
    dig = n % 10
    tot = tot + dig
    n = n // 10
print("The total sum of digits is:", tot)
