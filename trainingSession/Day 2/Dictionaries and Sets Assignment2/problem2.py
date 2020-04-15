employeelist = [
    {'name': 'Joel', 'salary': '25', 'experience': 2, 'status': 'Okay'},
    {'name': 'Abhay', 'salary': '30', 'experience': 3, 'status': 'Okay'},
    {'name': 'Bunty', 'salary': '20', 'experience': 4, 'status': 'Okay'},
    {'name': 'Chakor',  'experience': 1, 'status': 'Not Okay'},
    {'name': 'Dagdoo', 'salary': '18', 'experience': 1, 'status': 'Okay'},
    {'name': 'Ektar', 'experience': 0, 'status': 'Okay'},
    {'name': 'Fandry', 'salary': 70, 'status': 'Okay'},
    {'name': 'Gappu', 'salary': '24', 'experience': 2, 'status': 'Okay'},
    {'name': 'Hari', 'salary': '25', 'experience': 2},
    {'name': 'Imtiyaz', 'experience': 2, 'status': 'Okay'}
]


def CalculateSalary(employeelist):
    for dict1 in employeelist:
        if 'experience' in dict1:
            m = 10 * dict1['experience']
        else:
            continue
        if 'status' in dict1:
            if dict1['status'] == 'Okay' or dict1['status'] == 'okay' or dict1['status'] == 'ok' or dict1['status'] == 'Ok' or dict1['status'] == 'OK':
                m += 5
        dict1['salary'] = m
        dict1['status'] = 'HR Approval'


def CalculateAvgSalary(employeelist):
    sum = 0
    for dict1 in employeelist:
        if 'status' in dict1:
            if dict1['status'] == 'Okay':
                if 'salary' in dict1:
                    sum += dict1['salary']
    return sum / len(employeelist)


CalculateSalary(employeelist)
print(employeelist)
print("Avg Salary :", CalculateAvgSalary(employeelist))
