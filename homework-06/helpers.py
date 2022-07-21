#
# Copyright (C) scenus.com, 2022.
# All rights reserved.
# Ehsan Haghpanah; haghpanah@scenus.com
#

from multipledispatch import dispatch

import inspect, os.path
import string
import random

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

#
#
@dispatch(int)
def get_random_words(n: int) -> list:
	l = get_list()
	return [random.choice(l) for i in range(n)]

#
#
@dispatch(int, int, int)
def get_random_words(n: int, min_len: int, max_len: int) -> list:
	if (min_len < 1) : min_len = 1
	if (max_len < 1) : max_len = 1

	a = []
	for i in range(n):
		s = ''.join(random.choice(string.ascii_lowercase) for j in range(random.randint(min_len, max_len))) 
		a.append(s)
	return a

#
#
@dispatch(int, str, int, int)
def get_random_words(n: int, t: str, min_len: int, max_len: int) -> list:
	if (min_len < 1) : min_len = 1
	if (max_len < 1) : max_len = 1
	return [''.join(random.choice(t) for i in range(random.randint(min_len, max_len))) for j in range(n)]	
