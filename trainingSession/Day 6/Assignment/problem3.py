option = input(
    "Please enter which operation you wish to perform: '+', '-', '*', '/', '**':")
outputtype = input("Choose output data type: 'int' or 'float': ")
a = int(input('Please input first operand: '))
b = int(input('Please input second operand: '))


if option == '+':
    print((lambda x, y: int(x+y) if outputtype == 'int' else float(x+y))(a, b))
elif option == '-':
    print((lambda x, y: int(x-y) if outputtype == 'int' else float(x-y))(a, b))
elif option == '*':
    print((lambda x, y: int(x*y) if outputtype == 'int' else float(x*y))(a, b))
elif option == '/':
    print((lambda x, y: int(x/y) if outputtype == 'int' else float(x/y))(a, b))
elif option == '**':
    print((lambda x, y: int(x**y) if outputtype == 'int' else float(x**y))(a, b))
