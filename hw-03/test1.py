#
# (C) Ehsan Haghpanah (haghpanah@scenus.com), 2022.
#

from os import listdir
from os import path

def get_subfolders(pa: str) -> list:
	return [path.join(pa, dr) for dr in listdir(pa) if (path.isdir(path.join(pa, dr)))]

def get_files(pa: str, ex: str) -> list:
	return [path.join(pa, fi) for fi in listdir(pa) if (path.isfile(path.join(pa, fi)) and fi.endswith(ex))]

def find_files(pa: str, ex: str, ls: list) -> list:
	ls.extend(get_files(pa, ex))
	ds = get_subfolders(pa)
	for dr in ds:
		find_files(dr, ex, ls)
	return ls

def main_run() -> None:
	ls = []
	find_files("f:\z2", ".csv", ls)
	print(ls)

main_run()