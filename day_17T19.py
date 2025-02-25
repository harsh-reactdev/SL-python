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

# nVal = int(input('Enter the value for n : '))
nVal = 5

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

# print(factVal)

# print(factN(nVal))

# ------------------------------------------------------------------------
# emulating do-while loop in python

while True:
    # print('Executing...')
    # rest of the loop body

    # by placing the if condition check on the bottom, we ensure that the loop body is run at least once before the condition is checked and the loop is terminate, in case.
    if(1 == 1): # add the condition on which the loop has to stop
        # print('Done.')
        break

# ------------------------------------------------------------------------
# break and continue

# print all non prime natural numbers
npRange = 100

nonPrimes = []
primes = [2]

# print('1\n2')
if npRange > 1:
    for i in range(3, npRange):
        isPrime = True
        for j in range(2, i):
            if i%j == 0:
                # print(i) #prints all non prime numbers
                nonPrimes.append(i)
                isPrime = False
                break
        
        if isPrime:
            # print(i) prints all primes
            primes.append(i)
            
# print(f"Primes : {primes}\n Non Primes : {nonPrimes}")