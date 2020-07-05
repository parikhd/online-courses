# Duck Typing

class Duck:
    def talk(self):
        print("Quack Quack")


class Human:
    def talk(self):
        print("Hello World")


def makenoise(o):
    o.talk()


d = Duck()
h = Human()

makenoise(d)
makenoise(h)


#   Dependency Injection using Duck Typing

class Flight:
    def __init__(self, engine):
        self.engine = engine

    def fly(self):
        self.engine.start()


class RollsRoyce:
    def start(self):
        print("Rolls Royce Engine Start")


rr = RollsRoyce()
f = Flight(rr)
f.fly()
