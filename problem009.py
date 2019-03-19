# A Pythagorean triplet is a set of three natural numbers, a < b < c,
# for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.
#
# step 1: make a list of pythagorean triplets

import math

for i in range(1, 500):
    for j in range(i, 500):
        a = float(i)
        b = float(j)
        c = math.sqrt(a*a + b*b)
        if (c.is_integer() and a+b+c == 1000):
            print("Sqrt(", a, " square + ", b, " square)= ", c)
            print("Their sum is: ", a+b+c)
            print("Their product is:", a*b*c)
