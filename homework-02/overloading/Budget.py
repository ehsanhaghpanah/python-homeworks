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
