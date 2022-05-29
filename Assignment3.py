# 1 - 2

# try:
#     a = 1/0;
# except BaseException as e:
#     print(e.args)
# 3 yes the following code is legal

# try:
#     x = 1
# finally:
#     print("finally")

# 6
# except IOError is when an input/output operation fails.
# except ZeroDivisionError mean you can't divide by zero

# my_file = open("words.txt", "w")
# my_file.write("Ronen")
# my_file = open("words.txt")
# for name in my_file.readlines():
#     print(name)
# my_file.write("שלום")
# for name in my_file.readlines():
#     print(name)

from PIL import Image, ImageDraw
im = Image.new('RGB', (500, 300), (128, 128, 128))
draw = ImageDraw.Draw(im)
draw.rectangle((200, 100, 300, 200), fill=(0, 0, 0), outline=(0, 0, 0))
im.save('new.png', quality=100)
