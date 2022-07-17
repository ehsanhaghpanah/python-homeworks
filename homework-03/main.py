#
# Copyright (C) scenus.com, 2022.
# All rights reserved.
# Ehsan Haghpanah; haghpanah@scenus.com
#

import inspect, os.path

filename = inspect.getframeinfo(inspect.currentframe()).filename
path     = os.path.dirname(os.path.abspath(filename))

print(filename)
print(path)




# from inspect import getsourcefile
# from os.path import abspath

# print(abspath(getsourcefile(lambda:0)))


# with open('data.txt') as file_object:
#     contents = file_object.read()
# print(contents)