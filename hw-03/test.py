
a = [1, 2, 3]
b = [3, 4, 5]
a.extend(b)
a = list(set(a))

print(a)