# The sequence of triangle numbers is generated by adding the natural numbers.
# So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28.
# The first ten terms would be:
#
# 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
#
# Let us list the factors of the first seven triangle numbers:
#
#      1: 1
#      3: 1,3
#      6: 1,2,3,6
#     10: 1,2,5,10
#     15: 1,3,5,15
#     21: 1,3,7,21
#     28: 1,2,4,7,14,28
#
# We can see that 28 is the first triangle number to have over five divisors.
#
# What is the value of the first triangle number to have over
# five hundred divisors?

# 1. create iterator that produces triangle numbers
# 2. find all divosors of that numbers and count them
import math
import sys


class TriNumGen:
    # iterator that produces triangle numbers
    def __iter__(self):
        self.a = 2
        return self

    def __next__(self):
        retval = 0
        for i in range(1, self.a):
            retval += i
        self.a += 1
        return retval


def triNumGen():
    # generator function because it's easier
    retval = 0
    for i in range(1, sys.maxsize):
        retval += i
        yield retval


def divisorCount(number):
    counter = 0
    for i in range(1, int(math.sqrt(number)+1)):
        if number % i == 0:
            if number/i == i:
                counter += 1
            else:
                counter += 2
    return counter


# initialising iter class
# triClass = TriNumGen()
# myIterClass = iter(triClass)

myIterFunc = triNumGen()

for i in range(0, sys.maxsize):
    TriNum = next(myIterFunc)
    divNum = divisorCount(TriNum)
    if divNum > 500:
        print(TriNum, " has ", divisorCount(TriNum), " Divisors")
        break
