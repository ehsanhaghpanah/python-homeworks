#
# Copyright (C) scenus.com, 2022.
# All rights reserved.
# Ehsan Haghpanah; haghpanah@scenus.com
#

# python dictionary(s)
a = {'prop1' : 'val1', 'prop2' : 'val2', 'prop3' : 3, 'prop4' : 3.5}
print(a)

b = {}
b["p1"] = "v1"
b["p2"] = 2
b["p3"] = [1, 2, 3]
b["p4"] = (1, 3, 'a')
print(b)

print(b.items())
print(b.keys())
print(b.values())

avg = lambda li : sum(li) / len(li)

la = [1.1, 2.3, 5.4, 7.6]
print(avg(la))

lb = [5400, 5200, 5200, 5370, 5380, 5410, 5280, 5270, 5210, 5310]

check = lambda p, l : p >= avg(l)

def checker(x: int) -> bool:
	if (x >= avg(lb)):
		return True
	return False
print(avg(lb))
result = list(filter(checker, lb))
print(result)
