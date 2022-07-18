
#
# checks if provided string is an integer, float or numeric
def foo1(n: str) -> None:
	if (n.isdigit()):
		print(f"{n} seems to be an integer")
	else:
		print(f"{n} is not an integer")

	if (n.isdecimal()):
		print(f"{n} seems to be an decimal")
	else:
		print(f"{n} is not an decimal")

	if (n.isnumeric()):
		print(f"{n} seems to be an numeric")
	else:
		print(f"{n} is not an numeric")

# foo1("2")
# foo1("2.5")
