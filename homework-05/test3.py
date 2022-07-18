
def foo(x: float, y: float) -> tuple:
	return x ** 2, y ** 2

print(foo(2, 3))
l = list(foo(3, 4))
print(l)

a = [1]
print(tuple(a)) # a single item tuple is presented as (1,)

l = []
l.append(1)
l.append(2)
m = []
m.append(3)
m.append(4)
print(l + m)
print((l + m) * 2)

t = tuple(l) + tuple(m)
print(t)
