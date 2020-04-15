dict1 = {}
dict1['name'] = input("Please enter your username.")
dict1['age'] = input("Please enter your age.")
dict1['password'] = input("Please input password")
with open('userinfo.txt', 'w') as f:
    f.write(str(dict1))

    # f.write("name : " + dict1['name'] + "\n")
    # f.write("age : " + dict1['age'])
