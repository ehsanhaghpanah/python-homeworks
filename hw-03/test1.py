#
# (C) Ehsan Haghpanah (haghpanah@scenus.com), 2022.
#

from os import listdir
from os import path

def get_subfolders(pa: str) -> list:
	return [dr for dr in listdir(pa) if (path.isdir(dr))]

def get_files(pa: str, ex: str) -> list:
	return [fi for fi in listdir(pa) if (path.isfile(fi) and fi.endswith(ex))]

def find_files(pa: str, ex: str, ls: list) -> None:
	ls.extend(get_files(pa, ex))
	ds = get_subfolders(pa)
	for dr in ds:
		find_files(dr, ex, ls)


def foo(ls: list):
	ls.extend([3, 5])

a = [1, 2, 4]
foo(a)
print(a)