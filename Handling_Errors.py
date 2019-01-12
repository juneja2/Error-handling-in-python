
try:
    for i in ['a', 'b', 'c']:
        print(i ** 2)

except TypeError:
    print("You are doing pow operation on string")

try:
    x = 100
    y = 0
    z = x/y
except ZeroDivisionError:
    print("Division by zero is not allowed")
finally:
    print("End try/except/finally")

def ask():
    while True:
        try:
            number = int(input("Input an interger: "))
        except ValueError:
            print("Invalid input for an integer")
        else:
            print("Number sqrt = {}".format(number ** 0.5))
            break
ask()
