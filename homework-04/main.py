#
# Copyright (C) scenus.com, 2022.
# All rights reserved.
# Ehsan Haghpanah; haghpanah@scenus.com
#

from functools import singledispatchmethod

# serialization of an object into a dictionay 
# and deserializtion of a dictionary into an object

class Budget(object):

    # @singledispatchmethod
    # def __init__(self, name: str, amount: float, period: int) -> None:
    #     self.name = name
    #     self.amount = amount
    #     self.period = period

    @singledispatchmethod
    def __init__(self, name: str) -> None:
        print("name")

    @singledispatchmethod.register(str, int)
    def __init__(self, name: str, code: int) -> None:
        print("name and code")


a = Budget("a")

    