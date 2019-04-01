# What is the greatest product of four adjacent numbers in the same direction
# (up, down, left, right, or diagonally) in the 20×20 grid?

import problem011data
numbers = problem011data.numbers


class Maximum(object):
    def __init__(self, number=0):
        self.number = number

    def safeMax(self, newNumber):
        if (newNumber > self.number):
            self.number = newNumber

    def getMax(self):
        return self.number


Max1 = Maximum(0)

print(numbers)

# horizontally
for row in range(0, 20):
    for col in range(0, 17):
        product = (numbers[row][col] * numbers[row][col+1]
                   * numbers[row][col+2] * numbers[row][col+3])
        Max1.safeMax(product)

# vertically
for row in range(0, 17):
    for col in range(0, 20):
        product = (numbers[row][col] * numbers[row+1][col]
                   * numbers[row+2][col] * numbers[row+3][col])
        Max1.safeMax(product)

# diagonally top left to bottom right
#
for row in range(0, 17):
    for col in range(0, 17):
        product = (numbers[row][col] * numbers[row+1][col+1]
                   * numbers[row+2][col+2] * numbers[row+3][col+3])
        Max1.safeMax(product)

for row in range(0, 17):
    for col in range(0, 17):
        product = (numbers[row+3][col] * numbers[row+2][col+1]
                   * numbers[row+1][col+2] * numbers[row][col+3])
        Max1.safeMax(product)

print(Max1.getMax())
