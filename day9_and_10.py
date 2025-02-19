# Type casting
a = 9
b = "10"

print(str(a))
print(int(b))
print(bool(b))


# Taking user input

c = input("Enter your name: ")
print("My name is", c)

age = input("Enter your age: ")
# print("My birthyear is", 2024 - age) cant be done because age is a string

print("My birthyear is", 2024 - int(age)) #returns an integer value for the birthyear 
# Hence, typecasting is necessary whenever we are taking user input if we want to perform any operation on it