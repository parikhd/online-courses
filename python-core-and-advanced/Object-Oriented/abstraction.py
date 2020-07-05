from abc import abstractmethod, ABC

class Test(ABC):

    @abstractmethod
    def talk(self):
        pass


class TestExtends(Test):
    def talk(self):
        print("Implementing abstract method talk()")


te = TestExtends()
te.talk()

# If all methods are abstract method then the class behaves as interface

