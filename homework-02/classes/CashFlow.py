#
# Copyright (C) scenus.com, 2022.
# All rights reserved.
# Ehsan Haghpanah; haghpanah@scenus.com
#

#
# a class represent 'Cash Flow'
class CashFlow:

	#
	# just for test for now
	def __init__(self, cash: float, flow: int) -> None:
		self.cash = cash
		self.flow = flow

	#
	# just for test for now
	def calc(self) -> float:
		return self.cash * self.flow