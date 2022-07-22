#
# (C) Ehsan Haghpanah (haghpanah@scenus.com), 2022.
#

#
# tries to parse provided string as an integer
#
# @param    text : a string representing an integer number
# @return   an integer if possible otherwise none
#
def try_parse(text: str) -> int:
    try:
        return int(text)
    except:
        return None

#
# tries to get an integer number from input
#
# @param    i_msg : input function prompt message
# @return   an integer if possible otherwise none
#
def get_int(i_msg: str) -> int:
    rs = try_parse(input(i_msg))
    if (rs == None):
        print("ERROR: Not a Valid Integer Number!")
    return rs

#
# checks if provided integer number is perfect or not
#
# @param    nm : an integer number
# @return   true if provided number is perfect otherwise flase
#
def is_perfect_number_1(nm: int) -> bool:
	ls = [1]
	for qo in range(2, ((nm // 2) + 1)):
		if ((nm % qo) == 0):
			ls.append(qo)
	sm = sum(ls)
	return (sm == nm)

#
# checks if provided integer number is perfect or not
#
# @param    nm : an integer number
# @return   true if provided number is perfect otherwise flase
#
def is_perfect_number_2(nm: int) -> bool:
	ls = [qo for qo in range(2, ((nm // 2) + 1)) if ((nm % qo) == 0)]
	return ((sum(ls) + 1) == nm)

#
# main function
def main_run() -> None:
	nm = get_int("please give me a number = ")
	if (nm == None):
		print("Not a suitable input, maybe!")
		exit()
	
	if (is_perfect_number_1(nm)):
		print(f"number = {nm} is perfect")
	else:
		print(f"number = {nm} is not perfect")

#
# main entry point
main_run()