#
#
from typing import overload


class Instrument:

	name = None
	code = None

	#
	#
	def __init__(self, name: str, code: str) -> None:
		self.name = name
		self.code = code

	#
	# 	
	def echo(self) -> None:
		print(f"name = {self.name}, code = {self.code}")

	@overload
	def foo(self, s: str) -> None:
		pass

	@overload
	def foo(self, i: int) -> None:
		pass

	def foo(x):
		print(f"type of{type(x)}")