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

# Day 14
# If Else

# age = int(input('Enter your age : '))
age = 18

if age >= 18:
    print('You can drive.!')
else:
    print('You cannot drive.')

# ---------------------------------------   

num = int(input('Enter a number : '))

if num < 0:
    print('Number is negative')
elif num == 0:
    print('The number is zero')
else:
    print('The number is even')
