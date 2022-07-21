#
# Copyright (C) scenus.com, 2022.
# All rights reserved.
# Ehsan Haghpanah; haghpanah@scenus.com
#

import helpers

# print(helpers.get_random_words(5, 2, 7))

a: list = helpers.get_random_words(7)
b = a.copy()
c = a.copy()
d = a.copy()

print(a)
print(a.pop())
print(a.pop(2))
print(a)

print(b)
print(b.pop(-1))

i = a[0]
print(c)
print(i)
c.remove(i)
print(c)

d.sort()
print(d)
d.reverse()
print(d)
