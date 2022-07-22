#
# (C) Ehsan Haghpanah (haghpanah@scenus.com), 2022.
#

def try_parse(text: str) -> int:
    try:
        return int(text)
    except:
        return None

def is_perfect_number(nm: int) -> bool:
	ls = [qo for qo in range(2, ((nm // 2) + 1)) if ((nm % qo) == 0)]
	return ((sum(ls) + 1) == nm)

def main_run() -> None:
	nm = try_parse(input("please give me a number = "))
	if (nm == None):
		print("ERROR: not a valid integer number!")
		exit()

	if (is_perfect_number(nm)):
		print(f"number = {nm} is perfect")
	else:
		print(f"number = {nm} is not perfect")

main_run()