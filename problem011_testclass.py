class Maximum(object):
    def __init__(self, number=0):
        self.number = number

    def safeMax(self, newNumber):
        if (newNumber > self.number):
            self.number = newNumber

    def getMax(self):
        return self.number


Maxi1 = Maximum(0)

for i in range(0, 10):
    Maxi1.safeMax(i)

print(Maxi1.getMax())
