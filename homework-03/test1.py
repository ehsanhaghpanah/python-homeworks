#
# Copyright (C) scenus.com, 2022.
# All rights reserved.
# Ehsan Haghpanah; haghpanah@scenus.com
#

import inspect, os.path

filename = inspect.getframeinfo(inspect.currentframe()).filename
filepath = os.path.dirname(os.path.abspath(filename))

with open(filepath + '\data.txt') as file_object:
    data = file_object.read()

data = data[1:-1]
list = data.split(",")
list = [item.strip().strip("\"") for item in list]

for idol in list[0:5]:
    print(f"{idol} -> {idol.lower()}")