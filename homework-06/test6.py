#
# Copyright (C) scenus.com, 2022.
# All rights reserved.
# Ehsan Haghpanah; haghpanah@scenus.com
#

import helpers

# print(dir(helpers))

def foo(*numbers) -> list:
     a = []
     for n in numbers:
          a.append(n)
     return a

# print(foo(2, 4, 5))

def greeting(name):
     print(f"name = {name}")

greeting("a")
greeting("a", "b")