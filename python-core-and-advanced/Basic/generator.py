def mygenerator(x, y):
    while (x < y):
        i = x ** 2
        yield i
        x += 1


print(type(mygenerator(1, 10)))

for i in mygenerator(1, 10): print(i)
