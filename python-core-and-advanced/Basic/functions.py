var = 123  # global


def average(a, b):
    print("Average is {}".format((a + b) / 2))
    return (a + b) / 2


print(average(55, 10))


def testmultireturns():  # we can return a tuple
    return 10, 20, 30


print(testmultireturns())


def accessglobalvar():
    print(globals()['var'])
    var = 456
    print(var)


accessglobalvar()

avg = average  # Assign Function to a Variable
print(avg(2, 4))


# Function inside a Function


def outerfunc():
    print("Outer")

    def innerfunc():
        print("Inner")

    innerfunc()


outerfunc()


# Passing Function itself as variable

def display(func):
    print("Hello " + func)


def func():
    return "Python"


display(func())


# Return function from a function

def display():
    print("Display Function")

    def message():
        print("Message Function")

    return message


func = display()
func()


# Recursive Function

def factorial(num):
    if (num <= 1):
        return 1
    return num * factorial(num - 1)


print(factorial(10))


# Default Arguments


def sum(a=0, b=0):
    print(a, b)
    return a + b


print("Sum is: ", sum(b=1))  # 1
print("Sum is: ", sum())  # 0
