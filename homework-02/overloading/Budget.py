#
# Copyright (C) scenus.com, 2022.
# All rights reserved.
# Ehsan Haghpanah; haghpanah@scenus.com
#

from multipledispatch import dispatch
from classes.CashFlow import CashFlow

class Budget:

	#
	# default constractor
	def __init__(self, amount: float) -> None:
		self.amount = amount
		self.cashflow = CashFlow(amount, 0)

	#
	# overloaded 1
	@dispatch()
	def foo(self) -> None:
		pass

	#
	# overloaded 2
	@dispatch(int)
	def foo(self, x: int) -> None:
		pass