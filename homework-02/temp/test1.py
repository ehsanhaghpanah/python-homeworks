#
# Copyright (C) scenus.com, 2022.
# All rights reserved.
# Ehsan Haghpanah; haghpanah@scenus.com
#

class Budget:

	#
	#
	def __init__(self) -> None:
		pass

	def fff(x: int) -> None:
		print(f"x = {x}")

	def goo(self) -> None:
		print("in -> goo")
		self.fff(1)

	#
	#
	def foo(self, i: int) -> None:
		pass

	#
	#
	def foo(self, s: str) -> None:
		pass

	def foo(x) -> None:
		print(f"type of x is {type(x)}")


#
# main entry point

b = Budget()
b.goo()
