import csv
dict_data = [
    {'No': 6, 'Name': 'Ven'},
    {'No': 7, 'Country': 'India'},
]
csv_columns = ['No', 'Name', 'Country']
csv_file = "Names.csv"
try:
    with open(csv_file, 'a') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in dict_data:
            writer.writerow(data)
except IOError:
    print("I/O error")

lines = []
with open("Names.csv", 'r') as csvfile:
    reader = csv. DictReader(csvfile)
    for row in reader:
        # print(row)
        lines.append(dict(row))
        for key, value in row.items():
            if not value:
                lines.remove(dict(row))
print(lines)
