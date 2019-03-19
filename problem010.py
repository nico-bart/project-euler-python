# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#
# Find the sum of all the primes below two million.

# smart method for finding prime numbers: Sieve of Eratosthenes
N = 2000000
gestrichen = []
primes = []
for i in range(0, N):
    gestrichen.append(False)

for i in range(2, N):
    if not gestrichen[i]:
        primes.append(i)
        for j in range(i*i, N, i):
            gestrichen[j] = True

sum = 0
for i in primes:
    print(i)
    sum += i

print(sum)
