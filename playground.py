"""
    Learn How to use
    > Default and Optional argument   ( args = 'default value' )
    > Many Positional Arguments ( *args )
    > Keyword Arguments    ( **args )
"""


def my_funct(value="default"):
    print(value)


my_funct()  # will print out : default
my_funct("override")  # will printout  : override


def my_function(a, b=2, c=3):
    print(a, b, c)


my_function(1, 4)  # will print out :   1 4 3
my_function(1)  # will print out :   1 2 3
my_function(1, c=4)  # will print out :   1 2 4


def my_function2(*args):
    for n in args:
        print(n)


my_function2(1)  # will print out : 1
my_function2(1, 2, 3)  # will print out : 1, 2, 3


def add(*args):
    total = 0
    for i in args:
        total += int(i)
    return total


print(add(1, 2, 3))  # will print out : 6
print(add(4, 5, 6, 7))  # will print out : 22


# keyword arguments
def kwargs(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(str(key) + " : " + str(value))


kwargs(add=3, test=3)
# print out : {'add': 3, 'test': 3}
#              add : 3, test : 3

def calculate(n, **args):
    print(args)
    n += args["add"]
    n *= args["multiply"]
    print(n)


calculate(2, add=3, multiply=5)  # will print out : 25


class Car:
    def __init__(self, **defaults):
        self.brand = defaults.get("brand")
        self.model = defaults.get("model")

mycar = Car(brand="Nissan", model="GTR")

print(mycar.model)  # print out : GTR
print(mycar.brand)  # print out : Nissan


def quiz(arg, *args, **kwargs):
    print(arg, args, kwargs)

quiz(1, 2, 3, 4, x=5, y=6) # will print out : 1 (2, 3, 4) {'x': 5, 'y': 6}

