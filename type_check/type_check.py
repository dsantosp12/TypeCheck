"""
    TypeCheck.type_check

    This module defines the functions and objects used in the unit tests.

    :copyright: (c) 2017 by Daniel Santos.
    :license: BSD, see LICENSE for more details.
"""


from functools import wraps
import types


def __type_check(*deco_args, **deco_kwargs):
    def type_check_wrapper(f):
        if not isinstance(f, types.FunctionType):
            raise TypeError(
                "This decorator is intended to functions or methods")

        @wraps(f)
        def wrapper(*f_args, **f_kwargs):
            # Path for keyword arguments
            if len(deco_kwargs) > 0:
                if not len(deco_kwargs) == len(f_args):
                    raise IndexError("The number of argument in the decorator "
                                     "don't match the function")
                else:
                    idx = 0
                    for key in deco_kwargs:
                        value = deco_kwargs[key]
                        if not isinstance(f_args[idx], value):
                            raise TypeError(
                                "Argument {} is not of type {}".format(
                                    key, value))
                        idx += 1
            else:  # Path for regular arguments
                if not len(deco_args) == len(f_args):
                    raise IndexError("The number of argument in the decorator "
                                     "don't match the function")
                idx = 0
                for arg in deco_args:
                    if not isinstance(f_args[idx], arg):
                        raise TypeError(
                            "Argument {} is not of type {}".format(idx+1, arg))
                    idx += 1
            return f(*f_args, **f_kwargs)
        return wrapper
    return type_check_wrapper


def __type_check_with(f):
    def type_check_with_wrapper(op):
        pass
    return lambda x: x
