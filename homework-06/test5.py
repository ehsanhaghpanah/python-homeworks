#
# Copyright (C) scenus.com, 2022.
# All rights reserved.
# Ehsan Haghpanah; haghpanah@scenus.com
#

def f1():
	a = ['a', 'a', 'b', 'c']
	print(f"a = {a}, type = {type(a)}, len = {len(a)}")
	b = set(a)
	print(f"b = {b}, type = {type(b)}, len = {len(b)}")
	c = list(b)
	c.sort()
	print(f"c = {c}, type = {type(c)}, len = {len(c)}")

def f2():
	a = {}
	a["name"] = "john"
	a["code"] = "a345"
	a["amount"] = 2.5
	a["index"] = 55
	print(a)
	print(f"type(a) = {type(a)}")
	print(a.items())
	print(f"type(a.items()) = {type(a.items())}")
	print(type(a))
	print(f"a.keys = {a.keys()}, a.values = {a.values()}")
	print(f"type(a.keys()) = {type(a.keys())}")
	print(f"type(a.values()) = {type(a.values())}")
	b = list(a)
	print(b)

class MyClass1:
	def __init__(self, n = 1):
		self.number = n

class MyClass2:
	def __init__(self, attr = []):
		self.attr = attr

class MyClass3:
	code = 1

# a = MyClass1()
# a.number = 2
# b = MyClass1()
# print(a.number)
# print(b.number)

# c = MyClass2()
# c.attr.append(2)
# d = MyClass2()
# print(c.attr)
# print(d.attr)
# d.attr.remove(2)
# print(c.attr)
# print(d.attr)

x = MyClass3()
x.code = 3
print(x.code)