# Choose inheritence over composition IS-A over HAS-A

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start(self):
        print('Engine Start')

    def stop(self):
        print('Engine Stop')

class i10(Car):
    def __init__(self, make, model, speed):
        Car.__init__(self, make, model)
        self.speed = speed


class swift(Car):
    def __init__(self, make, model, speed):
        Car.__init__(self, make, model)
        self.speed = speed

    def start(self):    # Overriding parent function
        print('Overriden Engine Start')


class city(Car):
    def __init__(self, make, model, speed):
        super().__init__(make, model)
        self.speed = speed

    def start(self):    # Overriding parent function
        print('Overriden Engine Start')
        super().start()



I = i10('Hyundai', 'i10', 140)
I.start()

M = swift('Maruti Suzuki', 'swift', 150)
M.start()

C = city('Honda', 'city', 160)
C.start()

