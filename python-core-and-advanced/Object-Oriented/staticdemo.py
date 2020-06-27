class InstanceCounter:

    count = 0

    def __init__(self):
        InstanceCounter.count += 1

    @staticmethod
    def displaycount():
        print(InstanceCounter.count)

I1 = InstanceCounter()
InstanceCounter.displaycount()
I2 = InstanceCounter()
InstanceCounter.displaycount()
