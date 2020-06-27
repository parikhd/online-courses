print("Let us explore OOP")


class Course:
    def __init__(self):
        self.name = 'Python'
        self.ratings = (5, 4, 5, 5)


c1 = Course()

print(c1.name, c1.ratings)
print(type(c1))


class Author:
    def __init__(self, name, location):
        self.name = name
        self.location = location


a1 = Author("Dhruv Parikh", "Bangalore")
print(a1.name, a1.location)


class Programmer:

    # Static Field
    role = "Developer"

    def setname(self, name):
        self.name = name

    def settechstack(self, techStack):
        self.techStack = techStack

    def display(self):
        print("Name is {0} Tech Stack is {1}".format(self.name, self.techStack))


P1 = Programmer()
P1.setname("Dhruv")
P1.settechstack([["Java", "Spring", "Python"]])
P1.display()
print(P1.role)
print(Programmer.role)
