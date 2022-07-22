
# (C) Ehsan Haghpanah (haghpanah@scenus.com), 2022.

try_parse = lambda s : int(s) if s.isdigit() else None

def is_perfect_number(nm: int) -> bool:
	ls = [qo for qo in range(2, ((nm // 2) + 1)) if ((nm % qo) == 0)]
	return ((sum(ls) + 1) == nm)

def main_run() -> None:
	nm = try_parse(input("an integer = "))
	if (nm == None):
		print("ERROR: not an integer!")
		exit()

	if (is_perfect_number(nm)):
		print(f"{nm} is perfect")
	else:
		print(f"{nm} is not perfect")

main_run()