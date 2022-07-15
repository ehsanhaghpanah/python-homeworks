#
# (C) Ehsan Haghpanah, 2022.
# haghpanah@scenus.com
#

from random import randint
from enum import Enum

class CheckResult(Enum):
    STOP = 0
    MORE = 1
    LESS = 2

# by default it is inherited from 'object'
class Game(object):

    #
    # default constructor
    def __init__(self, lower_bound: int, upper_bound: int) -> None:
        
        # storing for future reference 
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

        # generating random number
        self.random_number = randint(self.lower_bound, self.upper_bound)

    #
    # checks if provided input number is correct or not
    # and reurn the direction
    def check(self, number: int) -> CheckResult:
        if number == self.random_number:
            return CheckResult.STOP
        elif number < self.random_number:
            return CheckResult.MORE
        else:
            return CheckResult.LESS