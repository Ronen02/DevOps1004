def div_numbers(a, b):
    print(int(a / b))


try:
    div_numbers(8, 2)
    div_numbers(9, 0)

except ZeroDivisionError as e:
    print("Could not divide by zero")
except BaseException as e:
    print(e.args)
    print('Something went terribly wrong')
print('Aviel')
