"""
    This module defines aliases for __type_check and __type_check_with to
    type_check and type_check_with. To import the user will do:

    from type_check import *

    Or:

    from type_check import type_check

    Instead off:

    from type_check.type_check import *

    Or:

    from type_check.type_check import type_check

    :copyright: (c) 2017 by Daniel Santos.
    :license: BSD, see LICENSE for more details.
"""

from type_check.type_check import __type_check, __type_check_with

type_check = __type_check
type_check_with = __type_check_with
