"""
    TypeCheck.type_check

    This module defines the functions and objects used in the unit tests.

    :copyright: (c) 2017 by Daniel Santos.
    :license: BSD, see LICENSE for more details.
"""


from functools import wraps


def __type_check(*args, **kwargs):
    def type_check_wrapper(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            raise TypeError("Testing")
        return wrapper
    return type_check_wrapper


def __type_check_with(f):
    def type_check_with_wrapper(op):
        pass
    return lambda x: x
