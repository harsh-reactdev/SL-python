# Day 11
# strings

a = 'this is a string'
b = "this is a string too, in double quotes"

# below two are used for multi line strings where a new line is necessary
c = """this too in triple double quotes"""
d = '''i kid you not, but this one too, is a string, in triple single quotes/'''

# ----------------------------------------------------------------------------------

# DAY 12
# string slicing

# print(a[2 : 5])
# print(a[-7:-5]) #slicing starts from the last index (-1)



# ---------------------------------------   
# Day 14
# If Else

# age = int(input('Enter your age : '))
age = 18

if age >= 18:
    print('You can drive.!')
else:
    print('You cannot drive.')

# ---------------------------------------   

# num = int(input('Enter a number : '))
num = 8

if num < 0:
    print('Number is negative')
elif num == 0:
    print('The number is zero')
else:
    print('The number is even')


# ---------------------------------------   
# time = int(input("what is the time now ? "))
time = 12

if time < 12:
    print('Good morning, Senor.!')
elif time > 12 and time < 16:
    print('Good noon, Senor.!')
else:
    print('Good evening, Master.!')

# --------------------------------------- 
# Exercise 2 : Good morming Sir

import time

def getTime():
    return time.localtime().tm_hour

current_time = getTime()

if(current_time < 12):
    print('Good Morning, Senor')
elif(current_time > 12):
    if(current_time < 3):
        print('Good Afternoon, Senor')
    elif(current_time < 7):
        print('Good evening, Senor')
    else:
        print('Have a Good Night, Senor')
# print(type(time.localtime().tm_hour))

# print(type(time.strftime('%H:%M:%S'))) // return is of string type
#  returns time in the format as specified in the argument

# --------------------------------------- 

# DAY 16 : Match case in Python

# I'm going to build a simple calculator using the match case statement in python

# calculator function
def calculate(n1, n2, op):
    match op:
        case 1:
            print(f"The sum of {n1} and {n2} is {n1+n2}")
        case 2:
            print(f"The difference between {n1} and {n2} is {n1-n2}")
        case 3:
            print(f"The product of {n1} and {n2} is {n1*n2}")
        case 4:
            print(f"The quotient of {n1} and {n2} is {n1/n2}")
        case _: #default case is indicated using _ (underscore) as the matching character
            print("Invalid choice")

# input
num1 = int(input('Enter the first integer : '))
num2 = int(input('Enter the second integer : '))
operation = int(input('Enter the operation you would like to perform :\n1. Add 2. Subtract 3. Multiply 4. Divide'))

calculate(num1, num2, operation)

# print(num1, num2, operation)

