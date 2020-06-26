def sqnum(x):
    return x ** 2


def decorme(fun):
    def test(x):
        result = fun(x)
        result += 2
        return result
    return test


print(decorme(sqnum)(20))

@decorme
def cubnum(x):
    return x ** 3

print(cubnum(10))
