# By listing the first six prime numbers:
# 2, 3, 5, 7, 11, and 13,
#
# we can see that the 6th prime is 13. What is the 10 001st prime number?
#
print("What is the 10 001st prime number?")

# # Method # 1 ----------------------------------------
# # this gets quite slow for large Numbers
# import math
# def primzahl(integ):
#     for i in range(2, math.ceil(integ/2)+1 ):
#         if integ%i == 0:
#             return False
#     return True
#
# primzahlCounter = 0
# check = 2
# while primzahlCounter < 10003:
# #for check in range(2,1000):
#     if primzahl(check):
#         primzahlCounter += 1
#         #primzahlArray.append(primzahlCounter : check)
#         print(primzahlCounter, check)
#     check += 1

# Method Nr 2 --------------------------------------------
# smarter method: Sieve of Eratosthenes
N = 10000000
primeCounterLimit = 10001
primeCounter = 0
stroke = []
for i in range(0, N):
    stroke.append(False)

for i in range(2, N):
    if not stroke[i]:
        primeCounter += 1
        print(primeCounter, i)

        for j in range(i*i, N, i):
            stroke[j] = True
    if primeCounter == primeCounterLimit:
        break
print("Thats the 10 001st prime number.")
