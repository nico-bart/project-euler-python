"""A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is
9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
"""
print("""Find the largest palindrome made from the product of two
 3-digit numbers.""")

threeDigits = []
biggestPalindrome = 0

# build a list of all multiples of three digit numbers
for i in range(100, 999):
    for j in range(i, 999):
        threeDigits.append(i*j)

# convert each number to string
# check if number-string has an uneven lenght. If so it cant be palindrome
# else check if it is actual palindrome
for k in range(0, len(threeDigits)):
    print(k, "st entry yields ", threeDigits[k])
    sThreeDigits = str(threeDigits[k])
    if len(sThreeDigits) % 2 == 0:
        a,b = sThreeDigits[:len(sThreeDigits)//2], sThreeDigits[len(sThreeDigits)//2:]
        b = b[::-1]
        if a == b and biggestPalindrome < threeDigits[k]:
            biggestPalindrome = threeDigits[k]
    else:
        pass

print(biggestPalindrome)
