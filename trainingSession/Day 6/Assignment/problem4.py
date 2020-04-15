option = input(
    "Please enter which string operation you wish to perform: concat '+', repeat '*', slice '[]',range slice '[:]', membership 'in': ")
a = input('Please input string: ')

if option == '+':
    b = input('Please input second string: ')
    print((lambda x, y: x+y)(a, b))
elif option == '*':
    b = int(input('Please input number of times the string should be repeated: '))
    print((lambda x, y: x*y)(a, b))
elif option == '[]':
    b = int(input('Please enter the subscript: '))
    print((lambda x, y: x[y])(a, b))
elif option == '[:]':
    b = int(input('Please input start index: '))
    c = int(input('Please input end index: '))
    print((lambda x, y, z: x[y:z])(a, b, c))
elif option == 'in':
    b = input('Please input substring to search: ')
    print((lambda x, y: y in x)(a, b))
