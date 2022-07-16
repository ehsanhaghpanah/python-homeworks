#
# Copyright (C) scenus.com, 2022.
# All rights reserved.
# Ehsan Haghpanah; haghpanah@scenus.com
#

def parse_integer(string, base = 10, default_value = None):
	if string.isdigit():
		return int(string, base)
	else:
		return default_value