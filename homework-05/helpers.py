#
# Copyright (C) scenus.com, 2022.
# All rights reserved.
# Ehsan Haghpanah; haghpanah@scenus.com
#

import inspect, os.path

#
# loads a long list from a file
def get_list() -> list:
	filename = inspect.getframeinfo(inspect.currentframe()).filename
	filepath = os.path.dirname(os.path.abspath(filename))
	with open(filepath + '\data.txt') as file_object:
		data = file_object.read()
	data = data[1:-1]
	l = data.split(",")
	l = [i.strip().strip("\"") for i in l]
	return l
