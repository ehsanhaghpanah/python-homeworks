#
# Copyright (C) scenus.com, 2022.
# All rights reserved.
# Ehsan Haghpanah; haghpanah@scenus.com
#

import os
import sys

# https://docs.python.org/2/using/windows.html

# %AppData%\Local\Programs\Python\Python38
# D:\Users\Administrator\AppData\Local\Programs\Python\Python38

print(os.path.dirname(sys.executable))
