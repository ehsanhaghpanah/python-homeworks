
from functools import singledispatchmethod

class BudgetInfo:

	@singledispatchmethod
	def __init__(self, amount):
		raise ValueError(f"unsupported value: {amount}")

	@__init__.register(int)
	def _constractor_a(self, amount):
		self.amount = amount + 1
		print("int")

	@__init__.register(float)
	def _constractor_b(self, amount):
		self.amount = amount * 2
		print("float")

a = BudgetInfo(5)
print(a.amount)
b = BudgetInfo(6.0)
print(b.amount)
c = BudgetInfo()

class CashFlow:
	@singledispatchmethod
	def __init__(self):
		raise ValueError(f"unsupported constractor")

	@__init__.register(int)
	def _constractor_a(self, amount: int):
		self.amount = amount + 1
		print("int")

	@__init__.register(str)
	def _constractor_b(self, name: str):
		self.name = name
		print("str")

a = CashFlow(1)
