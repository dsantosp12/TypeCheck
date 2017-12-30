"""
    TypeCheck.test_type_check

    This module contains the unit test code for the type_check function.
    The function stubs being tested are defined in function_stubs.py to avoid
    code duplication.

    :copyright: (c) 2017 by Daniel Santos.
    :license: BSD, see LICENSE for more details.
"""

import unittest

from tests.function_stubs import *


class TestTypeCheck(unittest.TestCase):
    """
        TestTypeCheck tests the type_check function.
    """

    def setUp(self):
        self.custom_obj = CustomObject()
        self.enum = enumerate([1, 2, 3])

    def test_type_check_single_arg(self):
        """
            Test functions with one arguments.

            Example:

            @type_check(complex)
            def f_with_complex(complex_num):
                ...
        """

        # The behavior of the following functions are meaningless,
        self.assertEqual(f_with_int(2), 3)
        self.assertEqual(f_with_float(2.3), 2.4)
        self.assertEqual(f_with_complex(4j), 1+4j)
        self.assertEqual(f_with_bytes(b'345'), b'345'.decode())
        self.assertEqual(f_with_bytearray(bytearray([1, 2, 3])),
                         bytearray([1, 2, 3]).decode())
        self.assertEqual(f_with_memoryview(memoryview(b'234')),
                         memoryview(b'243').shape)
        self.assertEqual(f_with_bool(True), False)
        self.assertEqual(f_with_str("Steph"), "Steph-tested")
        self.assertEqual(f_with_list([1, 5, 6]), 3)
        self.assertEqual(f_with_tuple((1, 2, 4, 5)), 4)
        self.assertEqual(f_with_slice(slice(1, 2, 4)), 1)
        self.assertEqual(f_with_set({1, 2, 3, 4}), {1, 2, 3, 4}.intersection())
        self.assertEqual(f_with_frozenset(frozenset([1, 2, 3, 4])),
                         frozenset(
                             [1, 2, 3, 4]
                         ).symmetric_difference([100, 200]))
        self.assertEqual(f_with_enumerate(self.enum), self.enum)
        self.assertEqual(f_with_custom(self.custom_obj), self.custom_obj)

    def test_type_check_single_arg_wrong_argument_type(self):
        """
            Test that functions using the decorator raise a TypeError exception
            if the incorrect type is provided.

            Example:

            @type_check(complex)
            def f_with_complex(complex_num):
                ...

        """
        # The behavior of the following functions are meaningless,
        with self.assertRaises(TypeError):
            f_with_int(2.4)

        with self.assertRaises(TypeError):
            f_with_float("this is a string")

        with self.assertRaises(TypeError):
            f_with_complex(None)

        with self.assertRaises(TypeError):
            f_with_bytes({4, 5, 6})

        with self.assertRaises(TypeError):
            f_with_bytearray(lambda x: x)

        with self.assertRaises(TypeError):
            f_with_memoryview(9.25)

        with self.assertRaises(TypeError):
            f_with_bool("this is a string")

        with self.assertRaises(TypeError):
            f_with_str(3)

        with self.assertRaises(TypeError):
            f_with_list((3, 5))

        with self.assertRaises(TypeError):
            f_with_tuple([3, 4, 5])

        with self.assertRaises(TypeError):
            f_with_slice(234)

        with self.assertRaises(TypeError):
            f_with_set([3, 4, 5])

        with self.assertRaises(TypeError):
            f_with_frozenset((4, 5, 6, 7, 7))

        with self.assertRaises(TypeError):
            f_with_enumerate(23)

        with self.assertRaises(TypeError):
            f_with_custom(5j)

    def test_type_check_multiple_args_same_type(self):
        """
            Test that function taking multiple arguments with the same type work
            as intended.

            Example:

            @type_check(str, str)
            def f_with_multi_str(first, last):
                ...
        """
        self.assertEqual(f_with_multi_int(5, 3), 8)
        self.assertEqual(f_with_multi_str("Daniel", "Santos"), "Daniel Santos")
        self.assertEqual(f_with_multi_list([1, 2], [3, 4]), [1, 2, 3, 4])

    def test_type_check_multiple_args_same_type_wrong_arguments_type(self):
        """
            Test that the function taking multiple arguments with the same type
            when given a wrong argument type throw a TypeError exception.
        """

        with self.assertRaises(TypeError):
            f_with_multi_str(5, [1, 2, 4])

        with self.assertRaises(TypeError):
            f_with_multi_str(3, "str")

        with self.assertRaises(TypeError):
            f_with_multi_str("str", 4)

    def test_type_check_multiple_named_args(self):
        """
            Test that functions behave normally, i.e., the type of the arguments
            get check, when the name of the arguments are provided in the
            decorator regardless of the order.

            Example:

            @type_check(first=str, last=str, age=int)
            def f_triple1(first, last, age):
                ...

            @type_check(first=str, age=int, last=str)
            def f_triple2(first, last, age):
                ...
        """
        equal_value = "Daniel Santos, age: 99"

        self.assertEqual(f_triple1("Daniel", "Santos", 99), equal_value)
        self.assertEqual(f_triple2("Daniel", "Santos", 99), equal_value)
        self.assertEqual(f_triple3("Daniel", "Santos", 99), equal_value)
        self.assertEqual(f_triple4("Daniel", "Santos", 99), equal_value)

    def test_type_check_multiple_named_arguments_check_type(self):
        """
            As the test above, but check that the TypeError exception is raised
            if any of the arguments have the wrong type.

            Example:

            @type_check(first=str, last=str, age=int)
            def f_triple1(first, last, age):
                ...

            @type_check(first=str, age=int, last=str)
            def f_triple2(first, last, age):
                ...
        """

        # Triple 1
        with self.assertRaises(TypeError):
            f_triple1(4.3, [1, 2, 3], (0, 3))

        with self.assertRaises(TypeError):
            f_triple1(4.3, [1, 2, 3], 99)

        with self.assertRaises(TypeError):
            f_triple1(4.3, "Santos", (2, 3))

        with self.assertRaises(TypeError):
            f_triple1(4.3, "Santos", 99)

        with self.assertRaises(TypeError):
            f_triple1("Daniel", [1, 2, 3], (0, 3))

        with self.assertRaises(TypeError):
            f_triple1("Daniel", [1, 2, 3], 5j)

        with self.assertRaises(TypeError):
            f_triple1("Daniel", "Santos", 9.8)

        # Triple 2
        with self.assertRaises(TypeError):
            f_triple2(4.3, [1, 2, 3], (0, 3))

        with self.assertRaises(TypeError):
            f_triple2(4.3, [1, 2, 3], 99)

        with self.assertRaises(TypeError):
            f_triple2(4.3, "Santos", (2, 3))

        with self.assertRaises(TypeError):
            f_triple2(4.3, "Santos", 99)

        with self.assertRaises(TypeError):
            f_triple2("Daniel", [1, 2, 3], (0, 3))

        with self.assertRaises(TypeError):
            f_triple2("Daniel", [1, 2, 3], 5j)

        with self.assertRaises(TypeError):
            f_triple2("Daniel", "Santos", 9.8)

        # Triple 3
        with self.assertRaises(TypeError):
            f_triple3(4.3, [1, 2, 3], (0, 3))

        with self.assertRaises(TypeError):
            f_triple3(4.3, [1, 2, 3], 99)

        with self.assertRaises(TypeError):
            f_triple3(4.3, "Santos", (2, 3))

        with self.assertRaises(TypeError):
            f_triple3(4.3, "Santos", 99)

        with self.assertRaises(TypeError):
            f_triple3("Daniel", [1, 2, 3], (0, 3))

        with self.assertRaises(TypeError):
            f_triple3("Daniel", [1, 2, 3], 5j)

        with self.assertRaises(TypeError):
            f_triple3("Daniel", "Santos", 9.8)

        # Triple 4
        with self.assertRaises(TypeError):
            f_triple4(4.3, [1, 2, 3], (0, 3))

        with self.assertRaises(TypeError):
            f_triple4(4.3, [1, 2, 3], 99)

        with self.assertRaises(TypeError):
            f_triple4(4.3, "Santos", (2, 3))

        with self.assertRaises(TypeError):
            f_triple4(4.3, "Santos", 99)

        with self.assertRaises(TypeError):
            f_triple4("Daniel", [1, 2, 3], (0, 3))

        with self.assertRaises(TypeError):
            f_triple4("Daniel", [1, 2, 3], 5j)

        with self.assertRaises(TypeError):
            f_triple4("Daniel", "Santos", 9.8)
