#
# Copyright (C) scenus.com, 2022.
# All rights reserved.
# Ehsan Haghpanah; haghpanah@scenus.com
#

from helpers import *

a = get_list()
print(len(a))
print(f"first = {a[0]}, last = {a[-1]}")

b = a[:]
b.sort()
print(len(b))
print(f"first = {b[0]}, last = {b[-1]}")

c = b.copy()
b.reverse()

if (c[0] == b[0]):
	print("the same")
else:
	print("copied")
