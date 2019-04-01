# 2520 is the smallest number that can be divided by each of the numbers from
# 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the
# numbers from 1 to 20?
#
# Finde das kleinste gemeinsame Vielfache der Zahlen 1 bis 20
#
# One has to find all the prime factors of the numbers 1 to 20

# factors
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20
#
# 5, 7, 9, 11, 13, 16, 17, 19

# import json
# wikiPrimes = json.loads(open('E:/Dev/python/project-euler-python/wikiPrimes.json', 'r').read())
# with open('E:/Dev/python/project-euler-python/wikiPrimes.dat', 'r') as f:
# wikiPrimes = f.read().split(',','\n')
# go brute force:
# for i in wikiPrimes:
#    if bign % i == 0:
#        factors.append(i)
#        bign /= i
#        print(bign)

print(5*7*9*11*13*16*17*19)
