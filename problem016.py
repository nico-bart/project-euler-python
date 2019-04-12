bigInt = pow(2, 1000)

sum = 0
for char in str(bigInt):
    char = int(char)
    sum += char

print(sum)
