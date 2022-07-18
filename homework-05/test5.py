#
# Copyright (C) scenus.com, 2022.
# All rights reserved.
# Ehsan Haghpanah; haghpanah@scenus.com
#

set_a = {"a", "b", "c"}
print(set_a)

set_a.add(2)
print(set_a)

set_a.add("a")		# will not add becase items in a set are unique
print(set_a)

set_a.remove("a")
print(set_a)

set_b = {"a", "b", "c", "a"}
print(set_b)