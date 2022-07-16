#
# Copyright (C) scenus.com, 2022.
# All rights reserved.
# Ehsan Haghpanah; haghpanah@scenus.com
#

from classes.CashFlow import CashFlow

#
# a class represent 'Discounted Cash Flow'
class DiscountedCashFlow(CashFlow):

    def __init__(self, cash: float, flow: int, discount: float) -> None:
        super().__init__(cash, flow)
        self.discount = discount

    def foo(self) -> float:
        return super().calc() * self.discount
