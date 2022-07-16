#
# Copyright (C) scenus.com, 2022.
# All rights reserved.
# Ehsan Haghpanah; haghpanah@scenus.com
#

from multipledispatch import dispatch

#
# tries to parse provided string as an integer
#
# @param text : a string representing an integer number
#
def try_parse(text: str) -> int:
    try:
        return int(text)
    except:
        return None

#
# tries to get an integer number from input
#
@dispatch()
def get_int() -> int:
    return get_int("Enter an Integer Number = ", "ERROR: Not a Valid Integer Number, Returning None")

#
# tries to get an integer number from input
#
# @param i_msg : input function prompt message
#
@dispatch(str)
def get_int(i_msg: str) -> int:
    return get_int(i_msg, "ERROR: Not a Valid Integer Number, Returning None")

#
# tries to get an integer number from input
#
# @param i_msg : input function prompt message
# @param e_msg : error message
#
@dispatch(str, str)
def get_int(i_msg: str, e_msg: str) -> int:

    rs = try_parse(input(i_msg))
    if (rs == None):
        print(e_msg)

    return rs