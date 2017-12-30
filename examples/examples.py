"""
    TypeCheck.examples
    
    :copyright: (c) Dec 2017 by Daniel Santos.
    :license: BSD, see LICENSE for more details.
"""

from type_check import *


# It's not limited to two arguments, you can add more as needed
@type_check(int, int)
def add(a, b):
    return a + b


# Can also use keys
@type_check(name=str, age=int)
def if_21(name, age):
    if age >= 21:
        return "{}, go ahead, you can!".format(name)
    else:
        return "Sorry, you still need to wait a bit"


# Custom objects are also allow and methods
class User:
    def __init__(self):
        pass

    def user_op(self, num):
        print(num)

    def __str__(self):
        return "This is an user!"


@type_check(User)
def send_user(inp):
    # Do user stuffs safe
    inp.user_op()


if __name__ == '__main__':
    print(add(3, 4))

    try:
        print(add("string!", 4))
    except TypeError:
        print("Safely found an error!")

    try:
        print(add(3, None))
    except TypeError:
        print("Safely found an error!")

    print(if_21("John", 23))

    try:
        print(if_21("John", "Smith"))
    except TypeError:
        print("Yep, there is an error")

    user = User()

    send_user(user)
