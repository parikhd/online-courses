print(" Multiple \nnLines")

a, b = 10, 20
print(a, b, sep=":")

name = "Dhruv"
marks = 10.5010

print("Name is {} Marks is {}".format(name, marks))
print("Name is {0} Marks is {1}".format(name, marks))
print("Name is %s Marks is %.2f" % (name, marks))

# Reading from console
name = input("Enter Name: ")

# Type Casting the read value
marks = (int(input("Enter Marks: ")))

print(name, "->", marks)

lst = input("Enter space separated nos: ").split()
print(type(lst))
intList=[];
for x in lst:
    intList.append(int(x))
print(intList)

lst = [int(num) for num in input("Enter nos: ").split()]    # Shortcut to directly convert to int
print(lst)

