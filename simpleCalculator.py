def simpleCalculator(a, b, op):
    res = 0
    if(op == '+'):
        res = a + b
    elif(op == '-'):
        res = a - b
    elif(op == '*'):
        res = a*b
    elif(op == '**'):
        res = a**b
    elif(op == '/'):
        res = a/b
    elif(op == '//'):
        res = a//b
    else:
        print('Invalid operator.!')
        return
    
    print('The result for ', a, op, b, ' is ', res)

# simpleCalculator(2, 4, '[]')

# all test cases checked and passed