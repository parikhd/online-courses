lst = [x ** 2 for x in range(1, 11)]
print(lst)

lst = [x for x in range(1, 11) if x % 2 == 0]
print(lst)

a = [1, 2, 3, 5, 6]
b = [4, 5, 6, 2, 3]
z = [a[i]*b[i] for i in range(0, len(a))]
print(z)

z = [a[i] for i in range(0, len(a)) if a[i] in b ]
print(z)
