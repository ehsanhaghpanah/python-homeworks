#
# Copyright (C) scenus.com, 2022.
# All rights reserved.
# Ehsan Haghpanah; haghpanah@scenus.com
#

from re import A


# a = ["aa", "ab", "ba", "aa", "as", "aa", "da"]
# print(len(a))
# print(a.count("aa"))
# print(a.index("aa"))
# print(a)
# a.append("ss")
# print(a)
# a.pop(1)
# print(a)
# a.remove("aa") # just removes first occurance
# print(a)

# a = ["bb", "aa", "dd", "cc", "ff", "ee", "gg", "hh", "aa", "cc"]
# print(a)
# print(a[3:])
# print(a[:3])
# a.sort()
# print(a)
# b = a[3:] + a[:3]
# print(b)
# b.sort()
# print(b)

# a = ["bb", "aa", "dd", "cc", "ff", "ee", "gg", "hh", "aa", "cc"]
# b = [x.upper() for x in a]
# print(b)

# a = list(range(10, 30, 4))
# print(a)

#
# list = [<iterator(s)> for <iterator(s)> in set(s) if <condition(s)-on-iterator(s)>]
# in this case 'else' block is not required
a = [n for n in range(1, 100) if (n % 3 == 0)]
print(a[:4])
print(len(a))

#
# list = [<iterator(s)> if <condition(s)-on-iterator(s)> <inline-expression(s)> else <inline-expression(s)> for <iterator(s)> in set(s)]
# in this case 'else' block is required
b = [n if (n % 3 == 0) else "*" for n in range(1, 100)]
print(b[:4])

