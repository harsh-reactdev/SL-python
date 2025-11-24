# recursion

# factorial
def fact(value):
    if value == 1 or value == 0:
        return 1
    else:
        return value * fact(value - 1)

# print(fact(50))

def fibonac(value):
    if value == 0:
        pass