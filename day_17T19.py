# Loops in Python

# for loop

# print even/odd numbers in the given range
# rangeValue = int(input('Enter the value for n : '))
rangeValue = 20
even = []
odd = []

for i in range(1, rangeValue+1):
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)

# print(even, odd)

# ------------------------------------------------------------------------

# factorial of a number using while

nVal = int(input('Enter the value for n : '))

# using recursion
# def factN(n):
#     factFnVal = n
#     while n > 1:
#         factFnVal * factN(n-1)
#     return factFnVal

factVal = 1

while(nVal != 0):
    factVal *= nVal
    nVal -= 1

print(factVal)

# print(factN(nVal))