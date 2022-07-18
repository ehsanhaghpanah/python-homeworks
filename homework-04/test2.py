
from multipledispatch import dispatch

class CashFlow(object):

	@dispatch(int)
	def __init__(self, cash: int) -> None:
		self.__cash = cash
		print("int")

	@dispatch(str)
	def __init__(self, name: str) -> None:
		self.__name = name
		print("str")

	@property
	def cash(self) -> int:
		return self.__cash

	@property
	def name(self) -> str:
		return self.__name

x = CashFlow(5)
print(x.cash)

z = CashFlow("a")
print(z.name)
