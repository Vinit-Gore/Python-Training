import json

data = {'4': 5, '6': 7}

# Write to Json File
try:
    with open('json_file.json', 'w') as jsonfile:
        jsonfile.write(json.dumps(data, sort_keys=True, indent=4))
except IOError:
    print("I/O error")

# Read from Json file
try:
    with open('json_file.json', 'r') as jsonfile:
        data = json.load(jsonfile)
except IOError:
    print("I/O error")

# Update Json file
for key, value in data.items():
    if key == '4':
        del(data['4'])
        data['1'] = 2
    if key == '6':
        data['6'] = 8
try:
    with open('json_file.json', 'w') as jsonfile:
        jsonfile.write(json.dumps(data, sort_keys=True, indent=4))
except IOError:
    print("I/O error")
