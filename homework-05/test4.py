#
# Copyright (C) scenus.com, 2022.
# All rights reserved.
# Ehsan Haghpanah; haghpanah@scenus.com
#

def foo(x: int, y: float, name: str) -> tuple:
	return (x ** 3, y ** 0.5, name.lower())

print(foo(2, 4, "AAAA"))

goo = lambda x, y, name : (x ** 3, y ** 0.5, name.lower())

print(goo(2, 4, "AAAA"))