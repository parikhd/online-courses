class Car:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def display(self):
        print(self.name, self.color)

    class Engine:
        def __init__(self, chassis):
            self.chassis = chassis

        def start(self):
            print("Engine with chassis {0} Start...".format(self.chassis))


C1 = Car("Hyundai", "Black")
C1.Engine = Car.Engine("123456")
C1.display()
C1.Engine.start()