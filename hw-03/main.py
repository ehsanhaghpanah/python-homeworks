#
# (C) Ehsan Haghpanah (haghpanah@scenus.com), 2022.
#

from os import listdir
from os import path

def get_subfolders(pa: str) -> list:
	if (not path.exists(pa)):
		print("path-not-exist")
		return None
	return [dr for dr in listdir(pa) if (path.isdir(dr))]

def get_files(pa: str, ex: str) -> list:
	if (not path.exists(pa)):
		print("path-not-exist")
		return None
	return [fi for fi in listdir(pa) if (path.isfile(fi) and fi.endswith(ex))]

def find_files(pa: str, ex: str, ls: list) -> list:
	if (not path.exists(pa)):
		print("path-not-exist")
		return
	ls.extend(get_files(pa, ex))
	ds = get_subfolders(pa)
	for dr in ds:
		find_files(dr, ex, ls)
	return ls

def main_run() -> None:
	# foo("f:\z2", "")
	print(get_subfolders("f:\z2"))

main_run()