
# def foo():
# 	return (1, 2)
# print(foo())

# a = (2, )
# print(a)

# b = []
# if (a):
# 	print("not-empty")
# else:
# 	print("empty")

# d = {'p1':'v1', 'p2':'v2', 'p3':'v3'}
# for x in d:
# 	print(x.value())

# o = {}
# o['name'] = 'ali'
# o['age'] = 20
# print(o)
# del o['name']
# print(o)

from typing import NewType

UserId = NewType('UserId', int)
print(type(UserId))

some_id = UserId(524313)
print(type(some_id))
