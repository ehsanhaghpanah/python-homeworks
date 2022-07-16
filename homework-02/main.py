#
# Copyright (C) scenus.com, 2022.
# All rights reserved.
# Ehsan Haghpanah; haghpanah@scenus.com
#

from classes.CashFlow import CashFlow
from classes.DiscountedCashFlow import DiscountedCashFlow

a = CashFlow(1.1, 2)
print(f"a -> calc = {a.calc()}")

b = DiscountedCashFlow(1.1, 2, 3)
print(f"b -> calc = {b.calc()}")
print(f"b -> calc = {b.foo()}")