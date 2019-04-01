import json
print("""Find the prime factors of 600851475143""")


bign = 600851475143
factors = []

wikiPrimes = json.loads(open('E:/Dev/python/project-euler-python/wikiPrimes.json', 'r').read())
# with open('E:/Dev/python/project-euler-python/wikiPrimes.dat', 'r') as f:
# wikiPrimes = f.read().split(',','\n')

# go brute force:
for i in wikiPrimes:
    if bign % i == 0:
        factors.append(i)
        bign /= i
        print(bign)

print("Solution: ", factors)
