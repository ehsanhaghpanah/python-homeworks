#
# Copyright (C) scenus.com, 2022.
# All rights reserved.
# Ehsan Haghpanah; haghpanah@scenus.com
#

# l = range(100, 999, 50)
# for i in l:
# 	print(i)
# print(type(l))
# l = list(l)
# print(type(l))

# a = [(x * 2) for x in l]
# print(a)

l = [(i ** 3) for i in range(1, 6)]
a = l[:3]
print(l)
print(a)
print(l[-2:])
print(l[:1])
print(l[-5:])
