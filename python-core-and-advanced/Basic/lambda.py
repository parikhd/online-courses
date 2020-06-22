from functools import reduce

l = lambda x, y: x ** y

print(l(10, 3))

check = lambda x: "EVEN" if (x % 2 == 0) else "ODD"

print(check(9))

# filter
lst = [1, 4, 2, 5, 11, 35, 66, 8]
res = filter(lambda x: x % 2 == 0, lst)
print(list(res))

# map
lst = [1, 4, 2, 5, 11, 35, 66, 8]
res = map(lambda x: x * 2, lst)
print(list(res))

# reduce
lst = [1, 2, 3, 4]
res = reduce(lambda x, y: x + y, lst)
print(res)
