# Each new term in the Fibonacci sequence is generated by adding the previous
# two terms. By starting with 1 and 2, the first 10 terms will be:
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
# By considering the terms in the Fibonacci sequence whose values do not
# exceed four million, find the sum of the even-valued terms.


import time
before = time.time()

# recursive calculation of the fibonacci sequence
# easily found via google
# memo safes the results for less redundancy
memo = {0:0, 1:1}
def fib(n):
    if not n in memo:
        memo[n] = fib(n-1) + fib(n-2)
    return memo[n]

sum = 0
for i in range(0,40):
    j = fib(i)
    if j > 4000000:
        break
    if j%2 == 0 and j <= 4000000:
        sum += j
    print(j-4000000) # a nice countdown for the user

print(sum)
print(time.time() - before)