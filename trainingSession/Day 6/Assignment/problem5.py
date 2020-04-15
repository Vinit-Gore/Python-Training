number = int(input('Please input a number: '))
table = []
for i in range(1, 13):
    (lambda x: table.append(x*i))(number)
print(table)
