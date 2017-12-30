"""
    TypeCheck.function_stubs

    This module defines the functions and objects used in the unit tests.

    :copyright: (c) 2017 by Daniel Santos.
    :license: BSD, see LICENSE for more details.
"""


from type_check import *


class CustomObject:
    def __init__(self):
        pass


@type_check(int)
def f_with_int(num):
    return num + 1


@type_check(float)
def f_with_float(float_num):
    return float_num + 0.1


@type_check(complex)
def f_with_complex(complex_num):
    return complex_num + 1


@type_check(bytes)
def f_with_bytes(bytes_arg):
    return bytes_arg.decode()


@type_check(bytearray)
def f_with_bytearray(byte_array):
    return byte_array.decode()


@type_check(memoryview)
def f_with_memoryview(memory_view):
    return memory_view.shape


@type_check(bool)
def f_with_bool(bool_arg):
    return not bool_arg


@type_check(str)
def f_with_str(name):
    return name + "-tested"


@type_check(list)
def f_with_list(list_arg):
    return len(list_arg)


@type_check(tuple)
def f_with_tuple(tuple_arg):
    return len(tuple_arg)


@type_check(dict)
def f_with_dict(dict_arg):
    return dict_arg.keys()


@type_check(slice)
def f_with_slice(slice_arg):
    return slice_arg.start


@type_check(set)
def f_with_set(set_arg):
    return set_arg.intersection()


@type_check(frozenset)
def f_with_frozenset(frozen_set):
    return frozen_set.symmetric_difference([100, 200])


@type_check(enumerate)
def f_with_enumerate(enum):
    return enum


@type_check(CustomObject)
def f_with_custom(obj):
    return obj


@type_check(int, int)
def f_with_multi_int(a, b):
    return a + b


@type_check(str, str)
def f_with_multi_str(first, last):
    return first + " " + last


@type_check(list, list)
def f_with_multi_list(l1, l2):
    return l1 + l2


@type_check(first=str, last=str, age=int)
def f_triple1(first, last, age):
    return first + " " + last + ", age: " + age


@type_check(first=str, age=int, last=str)
def f_triple2(first, last, age):
    return first + " " + last + ", age: " + age


@type_check(last=str, first=str, age=int)
def f_triple3(first, last, age):
    return first + " " + last + ", age: " + age


@type_check(age=str, first=str, last=int)
def f_triple4(first, last, age):
    return first + " " + last + ", age: " + age
