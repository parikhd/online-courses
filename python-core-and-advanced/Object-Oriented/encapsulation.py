class Employee:
    def __init__(self):
        self.id = '12345'
        self.__salary = '130K'  # private or hidden field


E = Employee()
print(E.id)
# print(E.salary)    # this will throw exception

print(E._Employee__salary)  # Name Mangling

